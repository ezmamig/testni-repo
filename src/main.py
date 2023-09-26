import subprocess
import time
import json
import os

def retry_git_push_with_metadata(repo_name, working_dir, branch_name="master", max_retries=10, retry_delay=5):
    try:
        # Change the working directory to the metadata directory
        os.chdir(working_dir)
        
        # Load the event_recipe.json file
        with open('event_recipe.json', 'r') as recipe_file:
            event_recipe = json.load(recipe_file)
        
        for retry in range(max_retries):
            try:
                # Pull and rebase before pushing
                subprocess.run(["git", "pull", "--rebase"])
                
                # Iterate through the event_recipe and push files
                for recipe_item in event_recipe:
                    source = recipe_item["source"]
                    target = recipe_item["target"]
                    path = recipe_item["path"]
                    
                    # Create the target path if it doesn't exist
                    os.makedirs(path, exist_ok=True)
                    
                    # Copy the source file to the target path
                    subprocess.run(["cp", source, os.path.join(path, target)])
                
                subprocess.run(["git", "add", "."])
                subprocess.run(["git", "commit", "-m", "Add metadata"])
                subprocess.run(["git", "push", "origin", branch_name])
                break  # If the push is successful, exit the loop
            except subprocess.CalledProcessError as e:
                print(f"Push failed (attempt {retry + 1}/{max_retries}): {e}")
                time.sleep(retry_delay)
        else:
            print("Max retries reached. Push operation failed.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python -m mygitlibrary <REPO_NAME> '<WORKING_DIR>'")
        sys.exit(1)
    
    repo_name = sys.argv[1]
    working_dir = sys.argv[2]
    retry_git_push_with_metadata(repo_name, working_dir)

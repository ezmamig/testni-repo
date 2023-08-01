param (
    [Parameter(Mandatory=$true)]
    [string]$installCFGJsonFilePath
)

# Read the installCFG.json file
$jsonContent = Get-Content -Path $installCFGJsonFilePath -Raw
$jsonObject = ConvertFrom-Json -InputObject $jsonContent

# Obtain the value for the key "SupportedOS"
$supportedOs = $jsonObject.SupportedOS

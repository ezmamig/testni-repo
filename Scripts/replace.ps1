try {
    # Attempt to use Copy-Item
    Copy-Ittem -Path $UnzipDir\* -Destination $TargetDir -Recurse
} catch {
    Write-Host "Copy-Item failed. Using robocopy as an alternative."
    robocopy $UnzipDir $TargetDir /E /DCOPY:DAT /R:10 /W:3 > null
}


$count = jf rt s $urlInstallerPackage --count --user=$ArtifactoryUser --password=$ArtifactoryPassword --url=https://jfrog.hub.vwgroup.com/artifactory

$count = jf rt s $urlInstallerPackage --count --user=$ArtifactoryUser --password=$ArtifactoryPassword --url=https://jfrog.hub.vwgroup.com/artifactory
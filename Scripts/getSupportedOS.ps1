param (
    [Parameter(Mandatory=$true)]
    [string]$installCFGJsonFilePath
)

# Read the installCFG.json file
$jsonContent = Get-Content -Path $installCFGJsonFilePath -Raw
$jsonObject = ConvertFrom-Json -InputObject $jsonContent
echo $jsonObject

# Obtain the value for the key "SupportedOS"
$supportedOs = $jsonObject.SupportedOS -join ', '
$supportedOsArray = @($supportedOs -split ',\s*' | ForEach-Object { "$_" })
$supportedOsJson = ConvertTo-Json $supportedOsArray -Compress -Depth 100 | Out-String
echo $supportedOsJson

Write-Output $supportedOsJson

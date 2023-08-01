param (
    [Parameter(Mandatory=$true)]
    [string]$installCFGJsonFilePath
)

# Read the installCFG.json file
$jsonContent = Get-Content -Path $installCFGJsonFilePath -Raw
$jsonObject = ConvertFrom-Json -InputObject $jsonContent

# Obtain the value for the key "SupportedOS"
$supportedOs = $jsonObject.SupportedOS -join ', '

# Check if SupportedOS is empty or missing
if (-not $supportedOs) {
    # use Windows 10, Windows Server 22 as default supported os
    $supportedOs = "Windows 10, Windows Server 2022"
    Write-Output $supportedOs
} else {
    # Output the value
    Write-Output $supportedOs
}
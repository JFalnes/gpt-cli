Set-Location $PSScriptRoot
# CHANGE THESE TO MATCH YOUR ENVIRONMENT
$projectPath = Join-Path $env:USERPROFILE "Documents\workspace\gpt-cli"

# Activating virtual environment
. (Join-Path $projectPath ".venv\Scripts\Activate.ps1")

# Running the Python script
python (Join-Path $projectPath "src\main.py")

# Deactivating virtual environment
deactivate

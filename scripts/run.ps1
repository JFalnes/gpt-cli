# Assume the script is being run from the 'scripts' directory
# Set the location to the script's parent directory, which is the project root
Set-Location -Path (Resolve-Path "$PSScriptRoot\..")

# Activating virtual environment from the project root
. ".venv\Scripts\Activate.ps1"

# Running the Python script located in the 'src' directory from the project root
python "src\main.py"

# Deactivating virtual environment
deactivate

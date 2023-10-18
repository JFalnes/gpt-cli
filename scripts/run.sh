#!/bin/bash

# Change to the parent directory
cd "$(dirname "$0")/.."

# Get the directory of the currently executing script (which is now the parent directory)
DIR="$(pwd)"

# Activate the virtual environment
source "$DIR/.venv/bin/activate"

# Run the Python script
python3 "$DIR/src/main.py"

# Deactivate the virtual environment
deactivate
#!/bin/bash

# Get the directory of the currently executing script
DIR="$(dirname "$(readlink -f "$0")")"

# Activate the virtual environment
source "$DIR/.venv/bin/activate"

# Run the Python script
python "$DIR/src/main.py"

# Deactivate the virtual environment
deactivate

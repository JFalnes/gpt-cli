#!/bin/bash

# Get the directory of the symlink
LINK_DIR="/usr/local/bin"

# Read the target of the symlink
TARGET="$(readlink "$LINK_DIR/chat")"

# Extract the directory of the target
TARGET_DIR="$(dirname "$TARGET")"

# Calculate the root directory of gpt-cli, which is one directory up from the scripts directory
ROOT_DIR="$(dirname "$TARGET_DIR")"

# Activate the virtual environment
source "$ROOT_DIR/.venv/bin/activate"

# Run the Python script
python3 "$ROOT_DIR/src/main.py"

# Deactivate the virtual environment
deactivate
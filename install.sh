#!/bin/bash

# install.sh

# Check if Poetry is installed
if ! command -v poetry &> /dev/null
then
    echo "Poetry could not be found, installing now..."
    curl -sSL https://install.python-poetry.org | python3 -
else
    echo "Poetry is already installed."
fi

# Ensure Poetry is in PATH
export PATH="$HOME/.local/bin:$PATH"

# Install project dependencies
echo "Installing project dependencies..."
poetry install

# Install Playwright browsers
echo "Installing Playwright browsers..."
poetry run playwright install

echo "Installation complete!"

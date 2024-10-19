#!/bin/bash

# start.sh

# Ensure Poetry is in PATH
export PATH="$HOME/.local/bin:$PATH"

# Function to add --url if not present and ensure https:// is prepended
prepare_args() {
    local args=()
    local url_found=false
    for arg in "$@"; do
        if [[ "$arg" == "--url" ]]; then
            url_found=true
            args+=("$arg")
        elif [[ "$url_found" == true ]]; then
            url_found=false
            if [[ "$arg" != http://* ]] && [[ "$arg" != https://* ]]; then
                arg="https://$arg"
            fi
            args+=("$arg")
        elif [[ "$arg" == http://* ]] || [[ "$arg" == https://* ]]; then
            args+=("--url" "$arg")
        else
            args+=("--url" "https://$arg")
        fi
    done
    echo "${args[@]}"
}

# Prepare arguments
ARGS=$(prepare_args "$@")

# Run the web scraper with prepared arguments
poetry run web-scraper $ARGS

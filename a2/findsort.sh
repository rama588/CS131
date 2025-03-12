#!/bin/bash

# Show help
help_msg() {
    echo "Usage: findsort [options] <directory>"
    echo ""
    echo "Options:"
    echo "  --search <name>    Find files by name."
    echo "  --type <ext>       Find files by extension."
    echo "  --content <text>   Find files containing text."
    echo "  --sort             Categorize files into folders."
    echo "  --help             Show this message."
    exit 0
}

# Handle --help before checking for a directory
if [[ "$1" == "--help" ]]; then
    help_msg
fi

# Ensure a directory is provided
if [[ $# -lt 1 ]]; then
    echo "Error: No directory given."
    help_msg
fi

# Resolve full path correctly
DIR=$(readlink -f "$1")
shift

# Check if directory exists
if [[ ! -d "$DIR" ]]; then
    echo "Error: Directory '$DIR' not found."
    exit 1
fi

# Find files by name
find_name() {
    NAME="$1"
    echo "Searching for '$NAME' in $DIR..."
    find "$DIR" -type f -iname "*$NAME*" 2>/dev/null
}

# Find files by type
find_type() {
    EXT="$1"
    echo "Searching for .$EXT files in $DIR..."
    find "$DIR" -type f -iname "*.$EXT" 2>/dev/null
}

# Find files by content
find_content() {
    TEXT="$1"
    echo "Searching for '$TEXT' inside files in $DIR..."
    grep -rl "$TEXT" "$DIR" 2>/dev/null
}

# Categorize files
sort_files() {
    echo "Sorting files in $DIR..."

    declare -A groups=(
        ["Documents"]="pdf doc docx txt md"
        ["Images"]="jpg png jpeg gif svg"
        ["Archives"]="zip tar.gz rar"
        ["Data"]="csv json xml xlsx"
        ["Scripts"]="sh py js"
    )

    for group in "${!groups[@]}"; do
        for ext in ${groups[$group]}; do
            files=$(find "$DIR" -type f -iname "*.$ext" 2>/dev/null)
            if [[ ! -z "$files" ]]; then
                echo "$group: $ext files found."
                echo "$files"
            fi
        done
    done

    read -p "Move files? (y/n): " confirm
    if [[ "$confirm" == "y" ]]; then
        for group in "${!groups[@]}"; do
            mkdir -p "$DIR/$group"
            for ext in ${groups[$group]}; do
                find "$DIR" -type f -iname "*.$ext" -exec mv {} "$DIR/$group/" \; 2>/dev/null
            done
        done
        echo "Files sorted."
    else
        echo "No changes made."
    fi
}

# Process options
while [[ $# -gt 0 ]]; do
    case "$1" in
        --help)
            help_msg
            ;;
        --search)
            shift
            find_name "$1"
            ;;
        --type)
            shift
            find_type "$1"
            ;;
        --content)
            shift
            find_content "$1"
            ;;
        --sort)
            sort_files
            ;;
        *)
            echo "Error: Unknown option '$1'."
            help_msg
            ;;
    esac
    shift
done


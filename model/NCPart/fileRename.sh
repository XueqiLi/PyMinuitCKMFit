#!/bin/bash

# Counter for the file renaming
COUNTER=1

# Create a temporary directory for modified files
TMP_DIR=$(mktemp -d)

# Iterate over .py files in a sorted order in the current directory
for FILE in $(ls *.py | sort); do
    # Add a comment with the file name at the top
    echo "# Filename: $FILE" > "$TMP_DIR/$FILE"
    cat "$FILE" >> "$TMP_DIR/$FILE"
    
    # Move the modified file back to the original directory
    mv "$TMP_DIR/$FILE" "$FILE"
done

# Clean up the temporary directory
rm -rf "$TMP_DIR"

# Rename files to model1.py, model2.py, etc. in the current directory
for FILE in $(ls *.py | sort); do
    mv "$FILE" "model${COUNTER}.py"
    let COUNTER=COUNTER+1
done


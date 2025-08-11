#!/bin/bash

# Directory containing the model files (current directory by default)
DIR="${1:-.}"

# Check if directory exists
if [ ! -d "$DIR" ]; then
    echo "Error: Directory '$DIR' does not exist"
    exit 1
fi

# Count the number of model files
file_count=$(find "$DIR" -maxdepth 1 -name "model*.py" -type f | wc -l)

if [ "$file_count" -eq 0 ]; then
    echo "No model*.py files found in $DIR"
    exit 1
fi

echo "Found $file_count model files to randomize"

# Create an array with numbers 1 to file_count and shuffle it
echo "Creating shuffled sequence from 1 to $file_count..."

# Initialize array with sequential numbers
sequence=()
for ((i=1; i<=file_count; i++)); do
    sequence+=($i)
done

# Fisher-Yates shuffle algorithm to randomize the sequence
for ((i=file_count-1; i>0; i--)); do
    # Generate random index from 0 to i
    j=$((RANDOM % (i+1)))
    
    # Swap elements at positions i and j
    temp=${sequence[i]}
    sequence[i]=${sequence[j]}
    sequence[j]=$temp
done

echo "Shuffled sequence created"

# First phase: Rename all files to temporary names to avoid conflicts
echo "Phase 1: Renaming to temporary files..."
temp_files=()
counter=0
for file in "$DIR"/model*.py; do
    if [ -f "$file" ]; then
        base_dir=$(dirname "$file")
        # Use timestamp and counter for uniqueness
        timestamp=$(date +%s%N 2>/dev/null || date +%s)
        temp_name="$base_dir/.temp_model_${counter}_${timestamp}_$$.py"
        mv "$file" "$temp_name"
        temp_files+=("$temp_name")
        ((counter++))
    fi
done

# Second phase: Rename temporary files to final randomized names
echo "Phase 2: Applying randomized sequence..."
counter=0
for temp_file in "${temp_files[@]}"; do
    if [ -f "$temp_file" ]; then
        base_dir=$(dirname "$temp_file")
        new_number=${sequence[$counter]}
        final_name="$base_dir/model${new_number}.py"
        mv "$temp_file" "$final_name"
        echo "Renamed to model${new_number}.py"
        ((counter++))
    fi
done

echo "Successfully randomized $counter files"
echo "Files now numbered from 1 to $file_count in random order"
#!/bin/bash

# Output file
output_file="model_outputs321-420.txt"

# Directory containing the model files
model_dir="model321-420"

# Temporary directory for output files
tmp_dir=$(mktemp -d)

# Add the current directory to PYTHONPATH
export PYTHONPATH="$PWD:$PYTHONPATH"

# Clear the output file (if exists) before writing new outputs
> "$output_file"

run_module() {
    module_path=$1
    tmp_output="$tmp_dir/$(basename "$module_path").out"

    # Extract only the file name from the path
    module_file=$(basename "$module_path")

    # Extract the module name by removing the .py extension
    module_name="${module_file%.py}"

    # Print the module name to the temporary output file
    echo "Output for $module_name:" >> "$tmp_output"

    # Run the Python script with the module name (prepended with "model.") and append the output to the file
    gtimeout 1m python3 fit.py "$model_dir.$module_name" >> "$tmp_output"

    # Add a separator line for clarity
    echo -e "\n-----------------------------\n" >> "$tmp_output"
}

export -f run_module

# Process all .py files in parallel
find "$model_dir" -name "*.py" | parallel -j $(nproc) run_module 

# Concatenate all temporary output files into the main output file
cat "$tmp_dir"/*.out >> "$output_file"

# Clean up the temporary directory
rm -rf "$tmp_dir"

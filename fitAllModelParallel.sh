#!/bin/bash

# Directory containing the model files
model_dir="model"

# Output file
output_file="model_outputs.txt"

# Temporary directory for output files in the current working directory with a unique timestamp
tmp_dir="./tmp_output_$(date +%s)"
mkdir -p "$tmp_dir" 
export tmp_dir
export model_dir

# Add the current directory to PYTHONPATH
export PYTHONPATH="$PWD:$PYTHONPATH"

# Clear the output file (if exists) before writing new outputs
> "$output_file"

run_module() {
    module_path=$1

    # Extract only the file name from the path
    module_file=$(basename "$module_path")

    # Extract the module name by removing the .py extension
    module_name="${module_file%.py}"

    tmp_output="$tmp_dir/$module_name.txt"

    # Print the module name to the temporary output file
    echo "Output for $module_name:" >> "$tmp_output"

    # Run the Python script with the module name (prepended with "model.") and append the output to the file
    gtimeout 10m python3 fit-shifted.py "$model_dir.$module_name" >> "$tmp_output"

    # Add a separator line for clarity
    echo -e "\n-----------------------------\n" >> "$tmp_output"
}

export -f run_module

# Process all .py files in parallel
find "$model_dir" -name "*.py" | parallel -j $(nproc) run_module 

# Concatenate all temporary output files into the main output file
cat "$tmp_dir"/*.txt >> "$output_file"

# Clean up the temporary directory safely
if [ -d "$tmp_dir" ] && [[ "$tmp_dir" == tmp_output_* ]]; then
    rm -rf "$tmp_dir"
else
    echo "Error: Unexpected temporary directory name. Manual cleanup might be required."
fi

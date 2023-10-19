#!/bin/bash

# Output file
output_file="model_outputs_321-420.txt"

# Directory containing the model files
model_dir="model321-420"

# Add the current directory to PYTHONPATH
export PYTHONPATH="$PWD:$PYTHONPATH"

# Clear the output file (if exists) before writing new outputs
> "$output_file"

# Iterate through all .py files in the model directory
for module_path in "$model_dir"/*.py; do
    # Extract only the file name from the path
    module_file=$(basename "$module_path")

    # Extract the module name by removing the .py extension
    module_name="${module_file%.py}"

    # Print the module name to the output file
    echo "Output for $module_name:" >> "$output_file"

    # Run the Python script with the module name (prepended with "model.") and append the output to the file
    gtimeout 2m python3 fit.py "$model_dir.$module_name" >> "$output_file"

    # Add a separator line for clarity
    echo -e "\n-----------------------------\n" >> "$output_file"
done

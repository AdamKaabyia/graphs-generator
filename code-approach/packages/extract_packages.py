import os
import re
import json
import yaml

def save_data_to_json(packages, filename="packages.json"):
    """Save package data to a JSON file."""
    with open(filename, 'w') as f:
        json.dump(packages, f, indent=4)


def save_data_to_yaml(packages, filename="packages.yaml"):
    """Save package data to a YAML file."""
    with open(filename, 'w') as f:
        yaml.dump(packages, f, default_flow_style=False)

def extract_package_info(directory):
    """
    Extracts packages and their files from all Go files within the specified directory.
    Returns a dictionary where keys are package names and values are tuples containing the path to the package and a list of files.
    """
    packages = {}  # Dictionary to hold package names and their details

    # Walk through the directory
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.go'):  # Check if the file is a Go file
                file_path = os.path.join(subdir, file)
                with open(file_path, 'rt') as f:
                    content = f.read()
                # Regular expression to find package declarations
                package_matches = re.findall(r'^\s*package\s+(\w+)', content, re.MULTILINE)
                if package_matches:
                    package_name = package_matches[0]
                    if package_name not in packages:
                        packages[package_name] = (os.path.relpath(subdir, directory), [])
                    packages[package_name][1].append(file_path)

    return packages
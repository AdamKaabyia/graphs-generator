import os
import re

def find_structs_and_interfaces(repo_path):
    """Walk through the directory, reading Go files and extracting structs and interfaces."""
    data = {}
    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.endswith('.go'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    content = f.read()
                structs = extract_structs(content)
                interfaces = extract_interfaces(content)
                if structs or interfaces:
                    data[file_path] = {
                        'structs': structs,
                        'interfaces': interfaces
                    }
    return data

def extract_structs(content):
    """Extract structs from file content."""
    pattern = r'type (\w+) struct\s*{([^}]*)}'
    return re.findall(pattern, content, re.MULTILINE | re.DOTALL)

def extract_interfaces(content):
    """Extract interfaces from file content."""
    pattern = r'type (\w+) interface\s*{([^}]*)}'
    return re.findall(pattern, content, re.MULTILINE | re.DOTALL)


def print_extracted_data(data):
    for path, info in data.items():
        print(f"File: {path}")
        for struct_name, struct_fields in info['structs']:
            print(f"  Struct: {struct_name} Fields: {struct_fields}")
        for interface_name, interface_methods in info['interfaces']:
            print(f"  Interface: {interface_name} Methods: {interface_methods}")

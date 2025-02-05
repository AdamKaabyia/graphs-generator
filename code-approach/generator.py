import os
import re
import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout
import matplotlib.pyplot as plt


def extract_go_imports(file_path):
    """ Extracts imported packages from a given Go file """
    imports = set()
    try:
        with open(file_path, 'rt') as file:
            content = file.read()

        # Match single-line imports: import "package"
        single_line_imports = re.findall(r'^\s*import\s+"(.*?)"', content, re.MULTILINE)
        imports.update(single_line_imports)

        # Match multi-line imports: import (\n "package1" \n "package2" \n)
        multi_line_imports = re.findall(r'(?s)import\s*\((.*?)\)', content)
        for block in multi_line_imports:
            packages = re.findall(r'"(.*?)"', block)
            imports.update(packages)

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
        raise
    except Exception as e:
        print(f"An error occurred while processing the file '{file_path}': {e}")
        raise

    return imports


def build_dependency_graph(directory, file_to_process=None):
    """ Builds a dependency graph from either a single Go file or all Go files within the specified directory """
    G = nx.DiGraph()  # Directed graph to represent dependencies

    if file_to_process:  # Process a single file
        file_path = os.path.join(directory, file_to_process)
        print(f"Processing file: {file_path}")  # Debug: print file being processed
        imports = extract_go_imports(file_path)
        go_file = file_to_process  # Use the provided file name as the node name
        for imp in imports:
            G.add_edge(go_file, imp)  # Create an edge from the Go file to the imported package
    else:  # Process all Go files in the directory
        for subdir, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith('.go'):
                    file_path = os.path.join(subdir, file)
                    go_file = os.path.relpath(file_path, directory)  # Relative path for node naming
                    imports = extract_go_imports(file_path)
                    for imp in imports:
                        G.add_edge(go_file, imp)  # Create an edge from the Go file to the imported package

    return G


def draw_graph(G):
    """ Draws the dependency graph using matplotlib and networkx """
    plt.figure(figsize=(12, 12))
    pos = graphviz_layout(G, prog='dot')  # Layout using graphviz 'dot' for hierarchical structure
    nx.draw(G, pos, with_labels=True, node_color='skyblue', font_size=10, node_size=3000, arrows=True)
    plt.title("Go Package Dependency Graph")
    plt.show()


def main():
    """ Main function to run the graph generation for a Go repository or a specific file """
    # Directory where your Go repo is located
    repo_directory = 'nvidia-ci'  # Replace with the path to your Go repo

    # Optionally specify a single file (relative path from the repo directory)
    file_to_process = 'nvidia-ci-main/tests/nvidiagpu/deploy-gpu-test.go'  # Replace with your desired file path

    # Ensure that the file path is correctly set up before proceeding
    file_path = os.path.join(repo_directory, file_to_process)
    if not os.path.isfile(file_path):
        print(f"Error: The file {file_path} does not exist.")
        return

    # Generate the dependency graph for either the repo or the single file
    G = build_dependency_graph(repo_directory, file_to_process=file_to_process)

    # Draw the graph
    draw_graph(G)


# Call the main function to generate and display the dependency graph
if __name__ == "__main__":
    main()

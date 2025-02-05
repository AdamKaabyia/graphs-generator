# Code Structure and Dependency Diagram Generator

## Overview
This directory contains tools and scripts designed to dynamically generate diagrams that describe the dependency relationships within a codebase from another repository. By analyzing and extracting import statements from Python files, the goal is to visually represent how different components of the project are interconnected.

## How It Works
The scripts automatically traverse through the directory of the cloned source code, identifying Python files and extracting all import statements. These imports are used to construct a directed graph, illustrating the dependencies between various files or modules within the codebase.

## Installation
To run the scripts and generate the dependency diagrams, you will need Python and several dependencies installed:

- Graphviz
- NetworkX

### Installing Dependencies
Execute the following commands in your terminal to install the necessary tools and libraries:

```bash
# Install Graphviz
sudo dnf install graphviz

# Install Python dependencies
pip install networkx pygraphviz

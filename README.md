
# **Graphs Generator Project**  

This repository contains tools and scripts for dynamically generating dependency and workflow diagrams from Go code repositories and log files. The project aims to automate the process of visualizing the structure and execution flow of a system by leveraging GitHub repositories and log data.

---

## **Project Structure**
```
graphs-generator/
│
├── code-approach/                  # Generate dependency diagrams from a GitHub repo
│   ├── generator.py                # Main script for traversing Go repo and extracting dependencies
│   ├── get_repo.py                 # Downloads a GitHub repository as a zip file
│   └── README.md                   # Explains the approach for generating diagrams from code
│
├── log-approach/                   # Generate workflow diagrams from log files
│   ├── main.py                     # Processes log files and generates workflow diagrams
│   └── README.md                   # Explains the approach for generating diagrams from log files
│
├── manual-approach/                # Static or initial approaches for generating diagrams
│   ├── initial-diagrams/           # Rudimentary manually created diagrams
│   └── README.md                   # Explanation of why manual approaches were abandoned
│
└── README.md                       # Main project README
```

---

## **Key Features**
1. **Graph Generation from GitHub Repos:**  
   - Automatically download a Go project from a GitHub repository and extract its import dependencies.
   - Generate a dependency diagram showing how different modules and packages interact within the project.  

2. **Workflow Generation from Log Files:**  
   - Extract the flow of execution from system logs.
   - Build workflow diagrams representing key steps and dependencies in the runtime process.
   - This approach builds on the graph generation capability (Step 1) to identify key components involved in execution.  

3. **Abandoned Manual Approaches:**  
   - Early attempts to manually create static diagrams were useful but time-consuming and hard to maintain.
   - With the current dynamic generation approach, diagrams can be automatically generated for every new pull request, drastically reducing manual work.

---

## **How It Works**
- **Step 1:** Use the **code-approach** to automatically download a GitHub repository and extract its dependency graph.  
- **Step 2:** Use the **log-approach** to process log files and generate workflow diagrams that track the execution flow.  
- **Step 3:** Visualize both diagrams dynamically, without needing manual updates, ensuring that new dependencies or changes to the codebase are reflected automatically.

---

## **Why Abandon the Static Approach?**
- Initially, manually creating dependency diagrams was useful but limited.
- Manual updates were tedious and inefficient, especially when new features or changes were made to the repository.
- The current dynamic approach allows diagrams to be automatically generated, making it possible to visualize and understand changes with every pull request without any extra effort.

---

## **Installation**
Make sure you have the following tools and libraries installed:

```bash
# Install Graphviz for diagram generation
sudo dnf install graphviz

# Install required Python libraries
pip install networkx pygraphviz
```

---

## **How to Run**
### **Step 1: Generate Dependency Graph**
1. Navigate to the `code-approach` directory.
2. Run the dependency graph generator:
   ```bash
   python generator.py
   ```
3. This will download the specified repository, analyze its imports, and generate a dependency graph.

### **Step 2: Generate Workflow Diagram**
1. Navigate to the `log-approach` directory.
2. Provide a log file for analysis and run:
   ```bash
   python main.py
   ```
3. The script will generate a workflow diagram representing the flow of execution.

---

## **Future Improvements**
- Expand support for other programming languages.
- Enhance workflow extraction with better log parsing techniques.
- Integrate diagram generation directly into CI/CD pipelines for automatic updates during pull requests.

---

With this project, developers and maintainers can easily visualize the internal structure and runtime behavior of their systems, reducing the time needed for manual analysis and making the process scalable for large projects.
```

You can copy and paste this content into a `README.md` file for your project. Let me know if you need further adjustments!
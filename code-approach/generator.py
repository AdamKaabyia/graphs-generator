from exract_packages import *

def main():
    """ Main function to collect and display all packages with their respective paths and files """
    repo_directory = 'nvidia-ci/nvidia-ci-main'  # Replace with your Go repo path
    packages = extract_package_info(repo_directory)
    print("Package information (Package Name, Path to Package, Files):")
    for package, details in sorted(packages.items()):
        path, files = details
        print(f"{package}: {path}")
        for file in files:
            print(f"  - {file}")

if __name__ == "__main__":
    main()

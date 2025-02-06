
from extract_packages import *


def main():
    """step 1 extract packages from the repository"""
    repo_directory = 'nvidia-ci/nvidia-ci-main'  # Adjust path to your Go repo directory
    packages = extract_package_info(repo_directory)

    """save that data, i tried both yaml and json im sticking with json- better looking"""
    # Save the extracted package data to files
    save_data_to_json(packages)
    #save_data_to_yaml(packages)

    """step 2 use the data we extracted to create packages GUI """




if __name__ == "__main__":
    main()

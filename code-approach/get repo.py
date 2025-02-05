import requests
import zipfile
import os

def download_and_extract_repo(url, extract_to='nvidia-ci'):
    """
    Download a repository from a given URL and extract it into the specified directory.

    :param url: URL to the zip file of the repository.
    :param extract_to: Directory where the contents should be extracted.
    """
    # Ensure the directory exists where the zip will be extracted
    if not os.path.exists(extract_to):
        os.makedirs(extract_to)

    # Get the filename
    local_filename = url.split('/')[-1]

    # Send a HTTP request to the URL
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        # Open a local file to write the downloaded content
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

    # Path to the local zip file
    path_to_zip_file = local_filename

    # Extract the zip file
    with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

    # Clean up the zip file after extraction
    os.remove(path_to_zip_file)
    print(f'Repository downloaded and extracted to {extract_to}')

# Adjust the URL to point directly to the .zip file of the main branch
repo_url = 'https://github.com/rh-ecosystem-edge/nvidia-ci/archive/refs/heads/main.zip'
download_and_extract_repo(repo_url)

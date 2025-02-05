import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import requests
import os

def download_log_file(url, local_filename):
    if not os.path.exists(local_filename):
        response = requests.get(url)
        if response.status_code == 200:
            with open(local_filename, 'w') as file:
                file.write(response.text)
            print("File downloaded successfully.")
        else:
            print("Failed to download the file.")
            return None
    else:
        print("File already exists.")
    return local_filename

def parse_datetime(row):
    try:
        return datetime.strptime(f"{row['date']} {row['time']}", '%Y/%m/%d %H:%M:%S')
    except ValueError:
        return None

def process_log_file(filepath):
    data = pd.read_csv(filepath, sep=" ", header=None, names=['date', 'time', 'info', 'extra'], engine='python', error_bad_lines=False, warn_bad_lines=True)
    data['timestamp'] = data.apply(parse_datetime, axis=1)
    data.drop(['date', 'time'], axis=1, inplace=True)
    data = data[data['timestamp'].notna()]
    return data

def plot_data(data):
    plt.figure(figsize=(10, 8))
    plt.plot(data['timestamp'], pd.Series(range(data.shape[0])), marker='o')
    plt.title('Timeline of Deployment Steps')
    plt.xlabel('Time')
    plt.ylabel('Step')
    plt.yticks(range(data.shape[0]), data['info'], rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def main():
    log_url = "https://gcsweb-ci.apps.ci.l2s4.p1.openshiftapps.com/gcs/test-platform-results/logs/periodic-ci-rh-ecosystem-edge-nvidia-ci-main-4.18-nvidia-gpu-operator-e2e-master/1884398589896036352/artifacts/nvidia-gpu-operator-e2e-master/gpu-operator-e2e/build-log.txt"
    local_filename = "build-log.txt"

    log_file_path = download_log_file(log_url, local_filename)
    if log_file_path:
        data = process_log_file(log_file_path)
        plot_data(data)

if __name__ == "__main__":
    main()

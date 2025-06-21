import hou
import requests
import os
import io
from pathlib import Path


def retrive_gsops_sample_data_info(gsops_data_folder_path_str):
    """Retrieve the paths of data files in the specified folder."""
    gsops_data_folder_path = Path(gsops_data_folder_path_str)
    if not gsops_data_folder_path.exists() or not gsops_data_folder_path.is_dir():
        hou.error(f"Folder path {gsops_data_folder_path_str} does not exist.")
        return []
    download_data_file_path = gsops_data_folder_path / ".download_data.txt"
    if not download_data_file_path.exists():
        print(f"Expected file not found: {download_data_file_path}. Can't retrieve files to download.")
        return []
    
    with open(download_data_file_path, "r") as f:
        download_data = []
        for line in f:
            line = line.strip()
            if not line:
                continue
            rel_path, url = line.split(maxsplit=1)
            dest_path = gsops_data_folder_path / rel_path

            file_id = "__".join(
                rel_path.replace("-", "_").replace(".", "_").split("/")
                )
            download_data.append((file_id, rel_path, url, dest_path))
    
    return download_data


def download_direct_gdrive(url, destination_path, retries=3, chunk_size_mb=8):
    """"Download a file from Google Drive using the url provided"""
    chunk_size = chunk_size_mb * 1024 * 1024  # Convert MB to bytes

    for attempt in range(1, retries + 1):
        try:
            print(f"Starting download attempt {attempt} out of {retries}...")
            with requests.get(url, stream=True, timeout=10) as response:
                response.raise_for_status()

                total_size = int(response.headers.get('Content-Length', 0))
                total_chunks = (total_size + chunk_size - 1) // chunk_size if total_size else None
                chunk_index = 0

                with open(destination_path, "wb") as f:
                    buffered = io.BufferedWriter(f)
                    for chunk in response.iter_content(chunk_size=chunk_size):
                        if chunk:
                            buffered.write(chunk)
                            chunk_index += 1
                            if total_chunks:
                                print(f"{destination_path} : Downloaded chunk {chunk_index} out of {total_chunks}")
                            else:
                                print(f"{destination_path} : Downloaded chunk {chunk_index} out of unknown total")
                    buffered.flush()

            print(f"File downloaded to: {destination_path}")
            return True
        except Exception as e:
            print(f"Attempt {attempt} failed: {e}")

    print("Download failed after multiple attempts.")
    return False


def download(download_data_file_path, output_dir):
    """"
    Download files from a list of URLs provided in a file.
    Returns True/False based on whether download took place and
    True/False if there was an error. (downloaded, error)
    """
    if not os.path.exists(download_data_file_path):
        print(f"File not found: {download_data_file_path}. Exiting download process.")
        return False, True # nothing downloaded, error
    
    os.makedirs(output_dir, exist_ok=True)

    download_data = []
    with open(download_data_file_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            rel_path, url = line.split(maxsplit=1)
            dest_path = os.path.join(output_dir, rel_path)

            if os.path.exists(dest_path):
                print(f"Skipping {rel_path}, already downloaded.")
                continue

            download_data.append((rel_path, url, dest_path))

    total = len(download_data)
    if total == 0:
        print("Nothing to download.")
        return False, False # nothing downloaded, no error

    # TODO: explore download without locking UI
    file_downloads_count = 0
    file_download_errors_count = 0
    with hou.InterruptableOperation("Downloading Files", long_operation_name="Downloading...", open_interrupt_dialog=True) as operation:
        for i, (rel_path, url, dest_path) in enumerate(download_data):
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)

            message = f"Downloading {rel_path} ({i+1}/{total})"
            progress = float(i) / total
            operation.updateLongProgress(progress, message)
            
            print(f"Progress: {int(progress * 100)}% {message}")

            download_success = download_direct_gdrive(url, dest_path)
            if download_success:
                 file_downloads_count = file_downloads_count + 1
            else:
                file_download_errors_count = file_download_errors_count + 1

        operation.updateLongProgress(1.0, "All downloads complete.")

    print("Done.")
    return file_downloads_count > 0, file_download_errors_count > 0 # downloaded stuff?, errors?

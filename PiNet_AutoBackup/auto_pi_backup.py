import os
import shutil
import datetime
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

def auto_pi_backup(backup_folder, storage_account_name, storage_account_key, container_name):
    # Create a BlobServiceClient object
    blob_service_client = BlobServiceClient(account_url=f"https://{storage_account_name}.blob.core.windows.net", credential=storage_account_key)

    # Create a ContainerClient object
    container_client = blob_service_client.get_container_client(container_name)

    # Get the current date and time
    current_date_time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

    # Create a backup folder if it doesn't exist
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)

    # Copy the Pi Network data to the backup folder
    shutil.copytree("path/to/pi/network/data", f"{backup_folder}/pi_network_data_{current_date_time}")

    # Upload the backup folder to the container
    for root, dirs, files in os.walk(backup_folder):
        for file in files:
            with open(os.path.join(root, file), "rb") as data:
                blob_client = container_client.get_blob_client(os.path.relpath(os.path.join(root, file), backup_folder))
                blob_client.upload_blob(data, overwrite=True)

    # Delete the local backup folder
    shutil.rmtree(backup_folder)

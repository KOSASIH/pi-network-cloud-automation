import os
import boto3
import time

class PiCloudBackup:
    def __init__(self, bucket_name, local_backup_dir):
        self.bucket_name = bucket_name
        self.local_backup_dir = local_backup_dir
        self.s3 = boto3.client('s3')

    def upload_to_s3(self, file_path):
        file_name = os.path.basename(file_path)
        self.s3.upload_file(file_path, self.bucket_name, file_name)
        print(f"{file_name} has been uploaded to {self.bucket_name}")

    def backup_files(self, file_paths):
        if not os.path.exists(self.local_backup_dir):
            os.makedirs(self.local_backup_dir)

        for file_path in file_paths:
            local_file_path = os.path.join(self.local_backup_dir, os.path.basename(file_path))
            self.upload_to_s3(file_path=file_path, file_name=local_file_path)

    def schedule_backups(self, file_paths, interval):
        while True:
            self.backup_files(file_paths=file_paths)
            print(f"Backups have been scheduled for an interval of {interval} seconds")
            time.sleep(interval)

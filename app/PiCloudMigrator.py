import os
import time
import shutil
import boto3

class PiCloudMigrator:
    def __init__(self, source_dir, target_bucket):
        self.source_dir = source_dir
        self.target_bucket = target_bucket
        self.s3 = boto3.client('s3')

    def migrate(self):
        # Create a temporary directory for staging files
        temp_dir = 'temp_' + self.source_dir
        os.mkdir(temp_dir)

        # Copy files from source directory to temporary directory
        for item in os.listdir(self.source_dir):
            src_file = os.path.join(self.source_dir, item)
            dst_file = os.path.join(temp_dir, item)
            shutil.copy2(src_file, dst_file)

        # Upload files from temporary directory to S3 bucket
        for item in os.listdir(temp_dir):
            src_file = os.path.join(temp_dir, item)
            self.s3.upload_file(src_file, self.target_bucket, item)

        # Remove temporary directory
        shutil.rmtree(temp_dir)

# Example usage
migrator = PiCloudMigrator('/path/to/local/directory', 'my-s3-bucket')
migrator.migrate()

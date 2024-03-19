import boto3
import os
import json

def pi_cloud_sync(bucket_name, local_directory):
    # Create an S3 client
    s3 = boto3.client('s3')

    # List all files in the local directory
    for root, dirs, files in os.walk(local_directory):
        for file in files:
            # Create a full path to the file
            local_path = os.path.join(root, file)

            # Upload the file to the S3 bucket
            s3.upload_file(local_path, bucket_name, local_path)

            print(f"Uploaded {local_path} to {bucket_name}")

# Example usage
pi_cloud_sync('my-bucket-name', '/home/pi/my-directory')

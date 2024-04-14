import os
import boto3

def create_ec2_instance():
    """
    Create a new EC2 instance on AWS.
    """
    ec2 = boto3.resource('ec2')

    # Create a new EC2 instance
    instance = ec2.create_instances(
        ImageId='ami-0c94855ba95c574c8',  # Amazon Linux 2 AMI ID
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        KeyName='my-key-pair',
        SecurityGroupIds=['sg-0123456789abcdef0']
    )[0]

    # Wait for the instance to start
    instance.wait_until_running()

    # Print the instance ID and public IP address
    print(f'Created instance with ID {instance.id} and public IP {instance.public_ip_address}')

if __name__ == '__main__':
    create_ec2_instance()

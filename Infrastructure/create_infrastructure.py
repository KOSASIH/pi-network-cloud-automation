import boto3

def create_infrastructure(instance_type, ami_id, key_pair_name, security_group_id, subnet_id):
    """
    This function creates the necessary infrastructure in the cloud.
    It includes creating and managing virtual machines, setting up networking, and configuring security settings.
    """
    ec2 = boto3.resource('ec2')

    # Create a new EC2 instance
    instance = ec2.create_instances(
        ImageId=ami_id,
        MinCount=1,
        MaxCount=1,
        InstanceType=instance_type,
        KeyName=key_pair_name,
        SecurityGroupIds=[
            security_group_id,
        ],
        SubnetId=subnet_id,
    )

    # Wait for the instance to be in the running state
    instance[0].wait_until_running()

    # Print the instance ID and public IP address
    print(f"Instance ID: {instance[0].id}")
    print(f"Public IP address: {instance[0].public_ip_address}")

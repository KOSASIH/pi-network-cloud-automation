import boto3
import json

def create_ec2_instance(instance_type, ami_id, key_pair_name):
    ec2 = boto3.resource('ec2')
    instances = ec2.create_instances(
        ImageId=ami_id,
        MinCount=1,
        MaxCount=1,
        InstanceType=instance_type,
        KeyName=key_pair_name,
        SecurityGroupIds=[
            'sg-12345678',  # replace with your security group ID
        ],
        SubnetId='subnet-12345678',  # replace with your subnet ID
    )
    return instances[0].id

def create_ecs_cluster(cluster_name):
    ecs = boto3.client('ecs')
    response = ecs.create_cluster(
        clusterName=cluster_name
    )
    return response['cluster']['clusterName']

def create_ecs_service(service_name, cluster_name, task_definition_arn, desired_count):
    ecs = boto3.client('ecs')
    response = ecs.create_service(
        serviceName=service_name,
        cluster=cluster_name,
        taskDefinition=task_definition_arn,
        desiredCount=desired_count
    )
    return response['service']['serviceName']

def create_ecs_task_definition(task_definition_name, container_definition_json):
    ecs = boto3.client('ecs')
    response = ecs.register_task_definition(
        family=task_definition_name,
        containerDefinitions=container_definition_json,
        networkMode='bridge',
        requiresCompatibilities=[
            'EC2',
        ],
        cpu='256',
        memory='512'
    )
    return response['taskDefinition']['taskDefinitionArn']

def create_cloud_pi_orchestrator(instance_type, ami_id, key_pair_name, cluster_name, service_name, task_definition_name, container_definition_json):
    # Create EC2 instance
    instance_id = create_ec2_instance(instance_type, ami_id, key_pair_name)
    print(f'Created EC2 instance with ID: {instance_id}')

    # Create ECS cluster
    cluster_arn = create_ecs_cluster(cluster_name)
    print(f'Created ECS cluster with ARN: {cluster_arn}')

    # Create ECS task definition
    task_definition_arn = create_ecs_task_definition(task_definition_name, container_definition_json)
    print(f'Created ECS task definition with ARN: {task_definition_arn}')

    # Create ECS service
    service_arn = create_ecs_service(service_name, cluster_arn, task_definition_arn, 1)
    print(f'Created ECS service with ARN: {service_arn}')

    return instance_id, cluster_arn, task_definition_arn, service_arn

# Example usage
container_definition_json = [
    {
        'name': 'pi-container',
        'image': 'pi-network-image:latest',
        'cpu': 128,
        'memory': 256,
        'essential': True,
        'portMappings': [
            {
                'containerPort': 80,
                'hostPort': 80,
                'protocol': 'tcp'
            }
        ]
    }
]

instance_id, cluster_arn, task_definition_arn, service_arn = create_cloud_pi_orchestrator(
    instance_type='t2.micro',
    ami_id='ami-12345678',
    key_pair_name='pi-key-pair',
    cluster_name='pi-cluster',
    service_name='pi-service',
    task_definition_name='pi-task-definition',
    container_definition_json=container_definition_json
)

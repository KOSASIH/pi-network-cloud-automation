import boto3

def get_ec2_instances():
    ec2 = boto3.resource('ec2')
    instances = ec2.instances.all()
    return instances

def get_ec2_instance_data(instance):
    data = {
        'id': instance.id,
        'state': instance.state['Name'],
        'instance_type': instance.instance_type['Name'],
        'launch_time': instance.launch_time,
        'public_ip': instance.public_ip_address,
        'private_ip': instance.private_ip_address
    }
    return data

def optimize_ec2_instances(instances):
    optimized_instances = []
    for instance in instances:
        instance_data = get_ec2_instance_data(instance)
        if instance_data['state'] == 'running':
            if instance_data['instance_type'] not in ['t2.micro', 't2.small']:
                optimized_instances.append(instance_data)
                instance.modify_attribute(InstanceType={'Value': 't2.micro'})
                print(f"Optimized instance {instance_data['id']} from {instance_data['instance_type']} to t2.micro")
            else:
                optimized_instances.append(instance_data)
        else:
            print(f"Skipped instance {instance_data['id']} due to its state: {instance_data['state']}")
    return optimized_instances

def pi_net_resource_optimizer():
    instances = get_ec2_instances()
    optimized_instances = optimize_ec2_instances(instances)
    return optimized_instances

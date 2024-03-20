import boto3
import time

def get_ec2_client():
    return boto3.client('ec2')

def get_autoscaling_client():
    return boto3.client('autoscaling')

def get_ec2_instances(client):
    response = client.describe_instances()
    instances = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instances.append(instance)
    return instances

def get_autoscaling_groups(client):
    response = client.describe_auto_scaling_groups()
    groups = response['AutoScalingGroups']
    return groups

def get_autoscaling_group_by_name(client, name):
    groups = get_autoscaling_groups(client)
    for group in groups:
        if group['AutoScalingGroupName'] == name:
            return group
    return None

def update_autoscaling_group_desired_capacity(client, group_name, desired_capacity):
    group = get_autoscaling_group_by_name(client, group_name)
    if group:
        client.update_auto_scaling_group(
            AutoScalingGroupName=group_name,
            DesiredCapacity=desired_capacity
        )

def scale_up(client, group_name, scale_up_count):
    group = get_autoscaling_group_by_name(client, group_name)
    if group:
        current_capacity = group['DesiredCapacity']
        new_capacity = current_capacity + scale_up_count
        update_autoscaling_group_desired_capacity(client, group_name, new_capacity)

def scale_down(client, group_name, scale_down_count):
    group = get_autoscaling_group_by_name(client, group_name)
    if group:
        current_capacity = group['DesiredCapacity']
        new_capacity = current_capacity - scale_down_count
        if new_capacity >= group['MinSize']:
            update_autoscaling_group_desired_capacity(client, group_name, new_capacity)

def get_ec2_server_count(client, tag_name, tag_value):
    instances = get_ec2_instances(client)
    count = 0
    for instance in instances:
        if instance['State']['Name'] == 'running':
            for tag in instance['Tags']:
                if tag['Key'] == tag_name and tag['Value'] == tag_value:
                    count += 1
                    break
    return count

def main():
    client_ec2 = get_ec2_client()
    client_as = get_autoscaling_client()

    while True:
        time.sleep(60)
        running_servers_count = get_ec2_server_count(client_ec2, 'type', 'pi_server')
        desired_servers_count = 10

        if running_servers_count < desired_servers_count:
            scale_up(client_as, 'pi-servers', desired_servers_count - running_servers_count)
        elif running_servers_count > desired_servers_count:
            scale_down(client_as, 'pi-servers', running_servers_count - desired_servers_count)

if __name__ == '__main__':
    main()

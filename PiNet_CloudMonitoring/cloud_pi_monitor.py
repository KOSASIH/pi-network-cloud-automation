import boto3
import time

def cloud_pi_monitor(region, instance_id, monitoring_interval):
    """
    Monitors Pi Network performance and activities on cloud infrastructure.
    
    Parameters:
    region (str): AWS region where the instance is located.
    instance_id (str): ID of the instance to monitor.
    monitoring_interval (int): Time interval in seconds between monitoring checks.
    
    Returns:
    None
    """
    
    # Initialize boto3 client for EC2
    ec2_client = boto3.client('ec2', region_name=region)
    
    # Initialize monitoring variables
    previous_cpu_utilization = 0
    previous_network_in = 0
    previous_network_out = 0
    
    # Monitoring loop
    while True:
        # Get current CPU utilization and network statistics
        current_cpu_utilization = get_cpu_utilization(instance_id, ec2_client)
        current_network_in, current_network_out = get_network_statistics(instance_id, ec2_client)
        
        # Calculate CPU utilization delta and network throughput
        cpu_utilization_delta = current_cpu_utilization - previous_cpu_utilization
        network_throughput = current_network_in + current_network_out - previous_network_in - previous_network_out
        
        # Print monitoring results
        print(f"CPU Utilization: {current_cpu_utilization}% ({cpu_utilization_delta}% change)")
        print(f"Network Throughput: {network_throughput} bytes/s")
        
        # Update previous monitoring values
        previous_cpu_utilization = current_cpu_utilization
        previous_network_in = current_network_in
        previous_network_out = current_network_out
        
        # Wait for the next monitoring interval
        time.sleep(monitoring_interval)

def get_cpu_utilization(instance_id, ec2_client):
    """
    Gets the current CPU utilization of thespecified instance.
    
    Parameters:
    instance_id (str): ID of the instance to get CPU utilization for.
    ec2_client (boto3.client): Boto3 EC2 client.
    
    Returns:
    float: Current CPU utilization of the instance.
    """
    
    # Get instance metrics
    metrics_response = ec2_client.describe_instances(InstanceIds=[instance_id])
    instance_metrics = metrics_response['Reservations'][0]['Instances'][0]['Metrics']
    
    # Find CPU utilization metric
    cpu_utilization_metric = next((m for m in instance_metrics if m['Name'] == 'CPUUtilization'), None)
    
    if cpu_utilization_metric is None:
        raise ValueError("Could not find CPU utilization metric for instance")
    
    # Get latest CPU utilization value
    cpu_utilization_values = cpu_utilization_metric['Values']
    latest_cpu_utilization = cpu_utilization_values[-1]
    
    return latest_cpu_utilization

def get_network_statistics(instance_id, ec2_client):
    """
    Gets the current network statistics of the specified instance.
    
    Parameters:
    instance_id (str): ID of the instance to get network statistics for.
    ec2_client (boto3.client): Boto3 EC2 client.
    
    Returns:
    tuple: Current network in and out bytes of the instance.
    """
    
    # Get instance network statistics
    network_stats_response = ec2_client.describe_instances(InstanceIds=[instance_id])
    instance_network_stats = network_stats_response['Reservations'][0]['Instances'][0]['NetworkInterfaces'][0]['Statistics']
    
    # Find network in and out bytes
    network_in_bytes = next((s['PacketsReceived']['Packets'] * s['PacketsReceived']['Bytes'] for s in instance_network_stats if s['Name'] == 'PacketsReceived'), 0)
    network_out_bytes = next((s['PacketsSent']['Packets'] * s['PacketsSent']['Bytes'] for sin instance_network_stats if s['Name'] == 'PacketsSent'), 0)
    
    return network_in_bytes, network_out_bytes

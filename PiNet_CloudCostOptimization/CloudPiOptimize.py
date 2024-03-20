import boto3
import pandas as pd
from datetime import datetime, timedelta

def get_ec2_instances(region):
    ec2 = boto3.client('ec2', region_name=region)
    response = ec2.describe_instances()
    instances = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instances.append(instance)
    return instances

def get_ec2_cost(instances):
    total_cost = 0
    for instance in instances:
        instance_type = instance['InstanceType']
        price = get_ec2_price(instance_type)
        total_cost += price
    return total_cost

def get_ec2_price(instance_type):
    ec2_pricing = boto3.client('pricing', region_name='us-east-1')
    response = ec2_pricing.get_products(
        ServiceCode='AmazonEC2',
        Filters=[
            {'Type': 'TERM_MATCH', 'Field': 'instanceType', 'Value': instance_type},
            {'Type': 'TERM_MATCH', 'Field': 'operatingSystem', 'Value': 'Linux'},
            {'Type': 'TERM_MATCH', 'Field': 'preInstalledSw', 'Value': 'NA'},
            {'Type': 'TERM_MATCH', 'Field': 'tenancy', 'Value': 'Shared'},
            {'Type': 'TERM_MATCH', 'Field': 'capacitystatus', 'Value': 'Used'},
        ]
    )
    price = float(response['PriceList'][0]['terms']['OnDemand'][instance_type]['priceDimensions']['1']['pricePerUnit']['USD'])
    return price

def optimize_ec2_instances(region):
    instances = get_ec2_instances(region)
    current_cost = get_ec2_cost(instances)
    optimized_instances = []
    for instance in instances:
        instance_type = instance['InstanceType']if instance_type == 't3.micro':
            continue
        else:
            optimized_instances.append(instance)
    optimized_cost = get_ec2_cost(optimized_instances)
    return optimized_instances, optimized_cost

def lambda_handler(event, context):
    region = 'us-east-1'
    start_time = datetime.now()
    instances_to_stop = get_idle_instances(region)
    stop_instances(instances_to_stop, region)
    instances_to_start = get_busy_instances(region)
    start_instances(instances_to_start, region)
    instances, cost = optimize_ec2_instances(region)
    end_time = datetime.now()
    print("Optimization time: " + str(end_time - start_time))
    print("Cost after optimization: $" + str(cost))

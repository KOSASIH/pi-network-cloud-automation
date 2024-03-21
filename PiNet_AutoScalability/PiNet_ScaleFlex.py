import boto3
import time

def PiNet_ScaleFlex(ec2_client, asg_name, min_instances, max_instances, desired_instances):
    """
    Implements dynamic scaling solutions for Pi Network infrastructure based on demand fluctuations.
    
    Parameters:
    ec2_client (boto3.client): Boto3 EC2 client.
    asg_name (str): Auto Scaling Group name.
    min_instances (int): Minimum number of instances in the Auto Scaling Group.
    max_instances (int): Maximum number of instances in the Auto Scaling Group.
    desired_instances (int): Desired number of instances in the Auto Scaling Group.
    
    Returns:
    None
    """
    
    # Get the current Auto Scaling Group details
    asg = ec2_client.describe_auto_scaling_groups(AutoScalingGroupNames=[asg_name])['AutoScalingGroups'][0]
    
    # Check if the current desired capacity is within the specified range
    if asg['DesiredCapacity'] < min_instances:
        # If the current desired capacity is less than the minimum, set it to the minimum
        ec2_client.update_auto_scaling_group(AutoScalingGroupName=asg_name, MinSize=min_instances, MaxSize=max_instances, DesiredCapacity=min_instances)
    elif asg['DesiredCapacity'] > max_instances:
        # If the current desired capacity is greater than the maximum, set it to the maximum
        ec2_client.update_auto_scaling_group(AutoScalingGroupName=asg_name, MinSize=min_instances, MaxSize=max_instances, DesiredCapacity=max_instances)
    else:
        # If the current desired capacity is within the specified range, do nothing
        pass
    
    # Wait for the scaling activity to complete
    while True:
        scaling_activities = ec2_client.describe_scaling_activities(AutoScalingGroupName=asg_name, ActivityIds=[asg['Activities'][0]['ActivityId']])
        if scaling_activities['ScalingActivities'][0]['Status'] == 'Successful':
            # If the scaling activity is successful, break out of the loop
            break
        else:
            # If the scaling activity is not successful, wait for 30 seconds and try again
            time.sleep(30)

    # Check if the current desired capacity is equal to the specified desired capacity
    if asg['DesiredCapacity'] != desired_instances:
        # If the current desired capacity is not equal to the specified desired capacity, update the Auto Scaling Group to reach the desired capacity
        ec2_client.update_auto_scaling_group(AutoScalingGroupName=asg_name, MinSize=min_instances, MaxSize=max_instances, DesiredCapacity=desired_instances)

    # Wait for the scaling activity to complete
    while True:
        scaling_activities = ec2_client.describe_scaling_activities(AutoScalingGroupName=asg_name, ActivityIds=[asg['Activities'][0]['ActivityId']])
        if scaling_activities['ScalingActivities'][0]['Status'] == 'Successful':
            # If the scaling activity is successful, print a message
            print(f"Auto Scaling Group '{asg_name}' has been updated with {desired_instances} instances.")
            break
        else:
            # If the scaling activity is not successful, wait for 30 seconds and try again
            time.sleep(30)

    
if __name__ == '__main__':
    ec2 = boto3.client('ec2')
    PiNet_ScaleFlex(ec2, 'PiNetworkASG', 2, 10, 5)

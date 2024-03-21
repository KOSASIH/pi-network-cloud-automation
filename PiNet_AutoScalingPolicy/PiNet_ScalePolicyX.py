import boto3

def PiNet_ScalePolicyX(policy_name, resource_id, scaling_type, threshold, action, cooldown=60):
    """
    Defines and implements policies for auto-scaling Pi Network resources based on predefined criteria.
    
    Parameters:
    policy_name (str): The name of the scaling policy.
    resource_id (str): The unique identifier of the resource to scale.
    scaling_type (str): The type of scaling to apply. Options: 'up', 'down'.
    threshold (int): The threshold value that triggers the scaling action.
    action (str): The action to take when the threshold is met. Options: 'add', 'remove'.
    cooldown (int): The number of seconds to wait between scaling actions. Default: 60.
    
    Returns:
    None
    """
    
    # Initialize the Auto Scaling client
    client = boto3.client('autoscaling')
    
    # Define the scaling policy
    policy = {
        'PolicyName': policy_name,
        'ResourceId': resource_id,
        'ScalingType': scaling_type,
        'Threshold': threshold,
        'Action': action,
        'Cooldown': cooldown
    }
    
    # Create the scaling policy
    response = client.put_scaling_policy(**policy)
    
    # Return the response
    return response

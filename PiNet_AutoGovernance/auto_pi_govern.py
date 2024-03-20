import boto3
import json

def auto_pi_govern(event, context):
    # Load the configuration from the event
    config = event['config']
    
    # Initialize the AWS client
    client = boto3.client('ec2')
    
    # Define the governance policies
    policies = [
        {
            'name': 'pi_network_security_group',
            'description': 'Security group for Pi Network',
            'rules': [
                {
                    'protocol': 'tcp',
                    'from_port': 22,
                    'to_port': 22,
                    'cidr_ip': '0.0.0.0/0',
                    'action': 'allow'
                },
                {
                    'protocol': 'tcp',
                    'from_port': 80,
                    'to_port': 80,
                    'cidr_ip': '0.0.0.0/0',
                    'action': 'allow'
                },
                {
                    'protocol': 'tcp',
                    'from_port': 443,
                    'to_port': 443,
                    'cidr_ip': '0.0.0.0/0',
                    'action': 'allow'
                }
            ]
        },
        {
            'name': 'pi_network_instance_type',
            'description': 'Instance type for Pi Network',
            'instance_type': 't2.micro'
        }
    ]
    
    # Apply the governance policies
    for policy in policies:
        if policy['name'] == 'pi_network_security_group':
            # Create the security group
            response = client.create_security_group(
                GroupName=policy['name'],
                Description=policy['description']
            )
            
            # Apply the security group rules
            for rule in policy['rules']:
                client.authorize_security_group_ingress(
                    GroupName=policy['name'],
                    IpProtocol=rule['protocol'],
                    FromPort=rule['from_port'],
                    ToPort=rule['to_port'],
                    CidrIp=rule['cidr_ip']
                )
            
        elif policy['name'] == 'pi_network_instance_type':
            # Create the instance
            response = client.run_instances(
                ImageId='ami-0c55b159cbfafe1f0',
                MinCount=1,
                MaxCount=1,
                InstanceType=policy['instance_type'],
                KeyName='pi-key-pair',
                SecurityGroupIds=[
                    'sg-0123456789abcdef0'
                ]
            )
            
    # Return the response
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Governance policies applied'
        })
    }

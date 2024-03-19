import boto3
import requests
from requests.exceptions import RequestException

def PiNetCloudPilot(operation, cloud_platform, network_config):
    """
    Pilots Pi Network operations on cloud platforms with precision automation.

    Parameters:
    operation (str): The operation to perform on the Pi Network.
    cloud_platform (str): The cloud platform to perform the operation on.
    network_config (dict): The network configuration for the operation.

    Returns:
    dict: The result of the operation.
    """

    # Initialize the cloud platform client
    if cloud_platform == "aws":
        client = boto3.client("ec2")
    elif cloud_platform == "azure":
        client = requests.Session()
        client.headers.update({"Authorization": "Bearer " + network_config["azure_token"]})
    elif cloud_platform == "gcp":
        client = requests.Session()
        client.headers.update({"Authorization": "Bearer " + network_config["gcp_token"]})
    else:
        raise ValueError("Unsupported cloud platform")

    # Perform the operation
    if operation == "create_vpc":
        if cloud_platform == "aws":
            response = client.create_vpc(CidrBlock=network_config["cidr_block"])
        elif cloud_platform == "azure":
            response = client.post("https://management.azure.com/subscriptions/" + network_config["subscription_id"] + "/resourceGroups/" + network_config["resource_group"] + "/providers/Microsoft.Network/virtualNetworks/" + network_config["vpc_name"] + "?api-version=2021-02-01", json={"location": network_config["location"], "properties": {"addressSpace": {"addressPrefixes": [network_config["cidr_block"]]}}})
        elif cloud_platform == "gcp":
            response = client.post("https://compute.googleapis.com/compute/v1/projects/" + network_config["project_id"] + "/global/networks", json={"name": network_config["vpc_name"], "autoCreateSubnetworks": True})
        return response
    elif operation == "create_subnet":
        if cloud_platform == "aws":
            response = client.create_subnet(VpcId=network_config["vpc_id"], CidrBlock=network_config["subnet_cidr_block"], AvailabilityZone=network_config["availability_zone"])
        elif cloud_platform == "azure":
            response = client.post("https://management.azure.com/subscriptions/" + network_config["subscription_id"] + "/resourceGroups/" + network_config["resource_group"] + "/providers/Microsoft.Network/virtualNetworks/" + network_config["vpc_name"] + "/subnets/" + network_config["subnet_name"] + "?api-version=2021-02-01", json={"location": network_config["location"], "properties": {"addressPrefixes": [network_config["subnet_cidr_block"]]}})
        elif cloud_platform == "gcp":
            response = client.post("https://compute.googleapis.com/compute/v1/projects/" + network_config["project_id"] + "/regions/" + network_config["region"] + "/subnetworks", json={"name": network_config["subnet_name"], "ipCidrRange": network_config["subnet_cidr_block"], "region": network_config["region"], "network": "projects/" + network_config["project_id"] + "/global/networks/" + network_config["vpc_name"]})
        return response
    elif operation == "create_security_group":
        if cloud_platform == "aws":
            response = client.create_security_group(VpcId=network_config["vpc_id"], GroupName=network_config["security_group_name"])
            client.authorize_security_group_ingress(GroupId=response["GroupId"], IpProtocol="tcp", FromPort=22, ToPort=22, CidrIp=network_config["allowed_cidr_block"])
        elif cloud_platform == "azure":
            response = client.post("https://management.azure.com/subscriptions/" + network_config["subscription_id"] + "/resourceGroups/" + network_config["resource_group"] + "/providers/Microsoft.Network/networkSecurityGroups/" + network_config["security_group_name"] + "?api-version=2021-02-01", json={"location": network_config["location"], "properties": {"securityRules": [{"name": "ssh", "properties": {"protocol": "Tcp", "sourcePortRange": "*", "destinationPortRange": "22", "sourceAddressPrefix": "*", "destinationAddressPrefix": "*", "access": "Allow", "priority": 100}}]}})
        elif cloud_platform == "gcp":
            response = client.post("https://compute.googleapis.com/compute/v1/projects/" + network_config["project_id"] + "/global/firewalls", json={"name": network_config["security_group_name"], "allowed": [{"IPProtocol": "tcp", "ports": ["22"]}], "sourceRanges": [network_config["allowed_cidr_block"]]})
        return response
    else:
        raise ValueError("Unsupported operation")

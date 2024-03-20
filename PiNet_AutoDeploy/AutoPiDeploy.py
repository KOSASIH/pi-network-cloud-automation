import os
import json
import requests

def AutoPiDeploy(config_file_name, resource_type, resource_name, resource_data):
    """
    Facilitates automatic deployment of Pi Network resources on cloud environments.
    
    Parameters:
    config_file_name (str): The name of the configuration file.
    resource_type (str): The type of the resource to be deployed (e.g., 'instance', 'network').
    resource_name (str): The name of the resource to be deployed.
    resource_data (dict): The data for the resource to be deployed.
    
    Returns:
    None
    """
    
    # Load the configuration data from the configuration file
    with open(config_file_name, 'r') as config_file:
        config_data = json.load(config_file)
    
    # Set the API key and network ID from the configuration data
    api_key = config_data['api_key']
    network_id = config_data['network_id']
    
    # Set the base URL for the Pi Network API
    base_url = 'https://api.pinet.io/v1'
    
    # Set the headers for the API request
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }
    
    # Set the URL for the API request
    url = f'{base_url}/networks/{network_id}/{resource_type}'
    
    # Set the data for the API request
    data = {
        'name': resource_name,
        'data': resource_data
    }
    
    # Send the API request to deploy the resource
    response = requests.post(url, headers=headers, json=data)
    
    # Check if the API request was successful
    if response.status_code == 201:
        print(f'Successfully deployed {resource_type} {resource_name}.')
    else:
        print(f'Failed to deploy {resource_type} {resource_name}. Error: {response.text}')

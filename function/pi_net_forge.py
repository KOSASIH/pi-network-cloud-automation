import requests
import json

def pi_net_forge(api_key, network_id, operation, data=None):
    """
    Automates seamless automation solutions for Pi Network cloud operations.
    
    :param api_key: Your Pi Network API key.
    :param network_id: The ID of the network you want to perform the operation on.
    :param operation: The operation you want to perform (e.g., 'create', 'update', 'delete').
    :param data: Any additional data required for the operation.
    
    :return: The response from the Pi Network API.
    """
    
    base_url = 'https://api.pinet.io/v1/'
    headers = {'Authorization': f'Bearer {api_key}', 'Content-Type': 'application/json'}
    
    if operation == 'create':
        url = f'{base_url}networks/{network_id}/{operation}'
        response = requests.post(url, headers=headers, json=data)
    elif operation == 'update':
        url = f'{base_url}networks/{network_id}/{operation}'
        response = requests.put(url, headers=headers, json=data)
    elif operation == 'delete':
        url = f'{base_url}networks/{network_id}/{operation}'
        response = requests.delete(url, headers=headers)
    else:
        raise ValueError(f"Invalid operation '{operation}'. Valid operations are 'create', 'update', and 'delete'.")
    
    return response.json()

import requests
import json

def pi_net_swift(api_key, api_url, network_id, operation, data=None):
    """
    Function to perform cloud operations for Pi Network using PiNetSwift.
    
    Parameters:
    api_key (str): API key for authentication.
    api_url (str): Base URL for the API.
    network_id (str): ID of the Pi Network.
    operation (str): Operation to perform (e.g., 'list_devices', 'create_device', etc.).
    data (dict): Data to be sent with the request (optional).
    
    Returns:
    dict: Response from the API.
    """
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }
    
    if data:
        data = json.dumps(data)
    
    response = requests.request(
        method=operation.upper(),
        url=f'{api_url}/networks/{network_id}/{operation}',
        headers=headers,
        data=data
    )
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f'Error {response.status_code}: {response.text}')

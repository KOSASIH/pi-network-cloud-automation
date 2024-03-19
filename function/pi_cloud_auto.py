import os
import requests
import json

def pi_cloud_auto(device_id, action):
    """
    Automate cloud system management for Pi devices.

    Parameters:
    device_id (str): The unique identifier for the Pi device.
    action (str): The action to perform on the Pi device.

    Returns:
    dict: The response from the cloud system management API.
    """

    # Replace with your actual API key and API endpoint
    api_key = 'your_api_key'
    api_endpoint = 'https://your_api_endpoint.com/api/v1/devices'

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }

    data = {
        'device_id': device_id,
        'action': action
    }

    response = requests.post(api_endpoint, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f'Error: {response.status_code} - {response.text}')

# Example usage
device_id = 'your_device_id'
action = 'reboot'
response = pi_cloud_auto(device_id, action)
print(response)

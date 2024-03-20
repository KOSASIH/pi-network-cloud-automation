import requests
import json
import time

def auto_pi(api_key, network_id, operation, data=None):
    """
    Automates Pi Network cloud operations.

    :param api_key: The API key for the Pi Network.
    :param network_id: The network ID for the Pi Network.
    :param operation: The operation to perform (e.g., 'list_devices', 'create_device', 'delete_device').
    :param data: The data to send with the operation (e.g., for creating a device).
    :return: The response from the operation.
    """
    base_url = f'https://api.pinet.io/v1/networks/{network_id}/'
    headers = {'Authorization': f'Bearer {api_key}', 'Content-Type': 'application/json'}

    if operation == 'list_devices':
        response = requests.get(base_url + 'devices/', headers=headers)
    elif operation == 'create_device':
        response = requests.post(base_url + 'devices/', headers=headers, data=json.dumps(data))
    elif operation == 'delete_device':
        response = requests.delete(base_url + f'devices/{data["device_id"]}/', headers=headers)
    elif operation == 'update_device':
        response = requests.put(base_url + f'devices/{data["device_id"]}/', headers=headers, data=json.dumps(data))
    elif operation == 'list_device_types':
        response = requests.get(base_url + 'device_types/', headers=headers)
    elif operation == 'create_device_type':
        response = requests.post(base_url + 'device_types/', headers=headers, data=json.dumps(data))
    elif operation == 'delete_device_type':
        response = requests.delete(base_url + f'device_types/{data["device_type_id"]}/', headers=headers)
    elif operation == 'list_messages':
        response = requests.get(base_url + 'messages/', headers=headers)
    elif operation == 'create_message':
        response = requests.post(base_url + 'messages/', headers=headers, data=json.dumps(data))
    elif operation == 'delete_message':
        response = requests.delete(base_url + f'messages/{data["message_id"]}/', headers=headers)
    else:
        print(f'Invalid operation: {operation}')
        return None

    if response.status_code == 200:
        return response.json()
    else:
        print(f'Error: {response.status_code}')
        return None

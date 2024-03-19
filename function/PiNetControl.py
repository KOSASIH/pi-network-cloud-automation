import requests
import json

def PiNetControl(api_key, network_id, operation, data=None):
    """
    Takes charge of Pi Network cloud operations with automated precision.
    
    Parameters:
    api_key (str): Your Pi Network API key.
    network_id (str): The ID of the network you want to control.
    operation (str): The operation you want to perform.
    data (dict): Optional data to send with the operation.
    
    Returns:
    dict: The response from the Pi Network API.
    """
    
    base_url = "https://api.pinet.io/v1/"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    
    if operation == "get_network_info":
        response = requests.get(f"{base_url}networks/{network_id}", headers=headers)
    elif operation == "create_device":
        response = requests.post(f"{base_1}networks/{network_id}/devices", headers=headers, json=data)
    elif operation == "update_device":
        device_id = data.pop("device_id")
        response = requests.put(f"{base_url}networks/{network_id}/devices/{device_id}", headers=headers, json=data)
    elif operation == "delete_device":
        device_id = data["device_id"]
        response = requests.delete(f"{base_url}networks/{network_id}/devices/{device_id}", headers=headers)
    else:
        raise ValueError("Invalid operation")
    
    return response.json()

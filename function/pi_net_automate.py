import requests
import json

def pi_net_automate(api_key, network_id, action):
    """
    Empowers Pi Network users with automated cloud management capabilities.
    
    :param api_key: The API key for the Pi Network.
    :param network_id: The ID of the Pi Network.
    :param action: The action to perform on the Pi Network.
    
    :return: The response from the API.
    """
    
    base_url = "https://api.pinet.io/v1/"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    
    if action == "create_device":
        url = f"{base_url}networks/{network_id}/devices"
        response = requests.post(url, headers=headers)
    elif action == "delete_device":
        device_id = input("Enter the ID of the device you want to delete: ")
        url = f"{base_url}networks/{network_id}/devices/{device_id}"
        response = requests.delete(url, headers=headers)
    elif action == "update_device":
        device_id = input("Enter the ID of the device you want to update: ")
        data = {"name": input("Enter the new name for the device: ")}
        url = f"{base_url}networks/{network_id}/devices/{device_id}"
        response = requests.put(url, headers=headers, data=json.dumps(data))
    elif action == "list_devices":
        url = f"{base_url}networks/{network_id}/devices"
        response = requests.get(url, headers=headers)
    else:
        raise ValueError("Invalid action. Please choose from 'create_device', 'delete_device', 'update_device', or 'list_devices'.")
    
    return response.json()

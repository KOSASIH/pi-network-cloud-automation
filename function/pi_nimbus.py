import requests
import json

def pi_nimbus(api_key, device_id, operation):
    """
    Automate cloud management tasks for Raspberry Pi setups.

    :param api_key: Your Nimbus API key.
    :param device_id: The ID of the device you want to manage.
    :param operation: The operation you want to perform.
    """

    base_url = "https://api.nimbus.io/v1/"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

    if operation == "start":
        url = f"{base_url}devices/{device_id}/start"
        response = requests.post(url, headers=headers)
    elif operation == "stop":
        url = f"{base_url}devices/{device_id}/stop"
        response = requests.post(url, headers=headers)
    elif operation == "restart":
        url = f"{base_url}devices/{device_id}/restart"
        response = requests.post(url, headers=headers)
    elif operation == "sync":
        url = f"{base_url}devices/{device_id}/sync"
        response = requests.post(url, headers=headers)
    elif operation == "update":
        url = f"{base_url}devices/{device_id}/update"
        response = requests.post(url, headers=headers)
    elif operation == "status":
        url = f"{base_url}devices/{device_id}/status"
        response = requests.get(url, headers=headers)
    else:
        raise ValueError("Invalid operation. Choose from 'start', 'stop', 'restart', 'sync', 'update', or 'status'.")

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")

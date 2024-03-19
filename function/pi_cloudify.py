import requests
import json

def pi_cloudify(pi_network_id, cloud_platform, api_key):
    """
    Simplifies Pi Network management on cloud platforms through automation.
    
    Parameters:
    pi_network_id (str): The unique identifier for the Pi Network.
    cloud_platform (str): The cloud platform to manage the Pi Network.
    api_key (str): The API key for the cloud platform.
    
    Returns:
    dict: The result of the automation process.
    """
    
    # Define the base URL for the cloud platform API
    base_url = f"https://api.{cloud_platform}.com/v1/"
    
    # Define the headers for the API request
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    # Define the payload for the API request
    payload = {
        "pi_network_id": pi_network_id
    }
    
    # Send the API request to the cloud platform
    response = requests.post(
        f"{base_url}pi_networks/",
        headers=headers,
        data=json.dumps(payload)
    )
    
    # Check if the API request was successful
    if response.status_code == 200:
        # Return the result of the automation process
        return response.json()
    else:
        # Return an error message if the API request was not successful
        return {
            "error": f"API request failed with status code {response.status_code}."
        }

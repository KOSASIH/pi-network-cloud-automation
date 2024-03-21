import requests
import json

def PiNet_IssueResolver(network_data):
    """
    Automatically detects and resolves issues within Pi Network infrastructure deployed on the cloud.
    
    Parameters:
    network_data (dict): A dictionary containing the network configuration and infrastructure details.
    
    Returns:
    dict: A dictionary containing the resolved issues and their corresponding solutions.
    """
    
    # Define the API endpoint for the PiNet issue resolver
    api_endpoint = "https://api.pinet.io/issue-resolver"
    
    # Send a POST request to the API endpoint with the network data
    response = requests.post(api_endpoint, json=network_data)
    
    # Check if the request was successful
    if response.status_code == 200:
        # If successful, return the resolved issues and their solutions
        return response.json()
    else:
        # If unsuccessful, return an error message
        return {"error": "Failed to resolve issues. Please check your network data and try again."}

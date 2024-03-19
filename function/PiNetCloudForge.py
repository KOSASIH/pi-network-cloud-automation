import requests
import json

def PiNetCloudForge(cloud_platform, api_key, app_id):
    """
    Forges a seamless connection between Pi Network and cloud platforms through automation.
    
    Parameters:
    cloud_platform (str): The cloud platform to connect to.
    api_key (str): The API key for the cloud platform.
    app_id (str): The ID of the app to connect.
    
    Returns:
    dict: The response from the cloud platform.
    """
    
    # Define the base URL for the cloud platform
    base_url = {
        'aws': 'https://aws.amazon.com/',
        'azure': 'https://azure.microsoft.com/',
        'google_cloud': 'https://cloud.google.com/'
    }
    
    # Define the API endpoint for the cloud platform
    api_endpoint = {
        'aws': 'https://api.aws.amazon.com/',
        'azure': 'https://api.azure.com/',
        'google_cloud': 'https://api.google.com/'
    }
    
    # Check if the cloud platform is supported
    if cloud_platform not in base_url:
        return {'error': 'Unsupported cloud platform'}
    
    # Create the headers for the API request
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }
    
    # Create the payload for the API request
    payload = {
        'app_id': app_id
    }
    
    # Send the API request to the cloud platform
    response = requests.post(
        f'{api_endpoint[cloud_platform]}/forge',
        headers=headers,
        data=json.dumps(payload)
    )
    
    # Return the response from the cloud platform
    return response.json()

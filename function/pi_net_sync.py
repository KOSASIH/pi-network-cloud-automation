import requests
import json

def pi_net_sync(pi_network_id, source_cloud_platform, destination_cloud_platform, api_key):
    """
    Synchronizes Pi Network tasks effortlessly across cloud environments.
    
    Parameters:
    pi_network_id (str): The unique identifier for the Pi Network.
    source_cloud_platform (str): The source cloud platform to synchronize tasks from.
    destination_cloud_platform (str): The destination cloud platform to synchronize tasks to.
    api_key (str): The API key for the cloud platforms.
    
    Returns:
    dict: The result of the synchronization process.
    """
    
    # Define the base URL for the source cloud platform API
    source_base_url = f"https://api.{source_cloud_platform}.com/v1/"
    
    # Define the headers for the source API request
    source_headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    # Define the payload for the source API request
    source_payload = {
        "pi_network_id": pi_network_id
    }
    
    # Send the source API request to the source cloud platform
    source_response = requests.get(
        f"{source_base_url}pi_networks/{pi_network_id}/tasks/",
        headers=source_headers,
        data=json.dumps(source_payload)
    )
    
    # Check if the source API request was successful
    if source_response.status_code == 200:
        # Get the tasks from the source cloud platform
        tasks = source_response.json()
        
        # Define the base URL for the destination cloud platform API
        destination_base_url = f"https://api.{destination_cloud_platform}.com/v1/"
        
        # Define the headers for the destination API request
        destination_headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
}
        
        # Send the destination API request to the destination cloud platform
        for task in tasks:
            destination_response = requests.post(
                f"{destination_base_url}pi_networks/{pi_network_id}/tasks/",
                headers=destination_headers,
                data=json.dumps(task)
            )
            
            # Check if the destination API request was successful
            if destination_response.status_code == 200:
                # Return the result of the synchronization process
                return {
                    "result": "success"
                }
            else:
                # Return an error message if the destination API request was not successful
                return {
                    "error": f"Destination API request failed with status code {destination_response.status_code}."
                }
    else:
        # Return an error message if the source API request was not successful
        return {
            "error": f"Source API request failed with status code {source_response.status_code}."
        }

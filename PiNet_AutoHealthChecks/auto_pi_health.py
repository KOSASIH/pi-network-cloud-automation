import requests
import json

def auto_pi_health(pi_network_url, api_key, cloud_service_url):
    """
    Conducts automated health checks and diagnostics for Pi Network systems on the cloud.
    
    Parameters:
    pi_network_url (str): URL of the Pi Network.
    api_key (str): API key for the Pi Network.
    cloud_service_url (str): URL of the cloud service.
    
    Returns:
    dict: A dictionary containing the health check results.
    """
    
    # Get the list of Pi Network components
    response = requests.get(f"{pi_network_url}/components", headers={"Authorization": f"Bearer {api_key}"})
    components = response.json()
    
    # Initialize the health check results dictionary
    health_check_results = {"healthy": [], "unhealthy": []}
    
    # Iterate through the Pi Network components
    for component in components:
        # Check the health of the component
        health_check_url = f"{cloud_service_url}/health/{component['id']}"
        health_check_response = requests.get(health_check_url)
        
        # If the health check is successful, add the component to the healthy list
        if health_check_response.status_code == 200:
            health_check_results["healthy"].append(component)
        # If the health check is unsuccessful, add the component to the unhealthy list
        else:
            health_check_results["unhealthy"].append(component)
    
    return health_check_results

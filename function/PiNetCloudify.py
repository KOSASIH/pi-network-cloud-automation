import requests
import json

def PiNetCloudify(api_key, management_url, cloud_automation_url):
    """
    Transforms Pi Network management into a streamlined cloud automation process.
    
    Parameters:
    api_key (str): Your Pi Network API key.
    management_url (str): The URL of your Pi Network management system.
    cloud_automation_url (str): The URL of your cloud automation system.
    
    Returns:
    dict: The transformed data from Pi Network management into a streamlined cloud automation process.
    """
    
    # Get data from Pi Network management system
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.get(management_url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
    else:
        raise Exception(f"Error: {response.status_code}")
    
    # Transform data into streamlined cloud automation process
    transformed_data = {}
    
    for item in data:
        transformed_item = {}
        
        for key, value in item.items():
            if key == "id":
                transformed_item["cloud_id"] = value
            elif key == "name":
                transformed_item["cloud_name"] = value
            elif key == "status":
                transformed_item["cloud_status"] = value
            elif key == "ip_address":
                transformed_item["cloud_ip_address"] = value
            elif key == "management_url":
                transformed_item["cloud_management_url"] = value
            elif key == "cloud_automation_url":
                transformed_item["cloud_automation_url"] = cloud_automation_url
        
        transformed_data[transformed_item["cloud_id"]] = transformed_item
    
    return transformed_data

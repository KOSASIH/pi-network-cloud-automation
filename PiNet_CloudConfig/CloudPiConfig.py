import os
import json

def CloudPiConfig(config_file_name, config_data):
    """
    Contains configuration files for setting up Pi Network operations on cloud platforms.
    
    Parameters:
    config_file_name (str): The name of the configuration file.
    config_data (dict): The configuration data to be stored in the configuration file.
    
    Returns:
    None
    """
    
    # Create the configuration file path
    config_file_path = os.path.join(os.getcwd(), config_file_name)
    
    # Write the configuration data to the configuration file
    with open(config_file_path, 'w') as config_file:
        json.dump(config_data, config_file, indent=4)

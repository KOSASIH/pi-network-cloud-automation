import json

def AutoPiConfig(resources, config_templates, config_parameters):
    """
    Automates the configuration management process for Pi Network components on the cloud.
    
    Parameters:
    resources (list): A list of resources to configure.
    config_templates (dict): A dictionary containing configuration templates for each resource.
    config_parameters (dict): A dictionary containing configuration parameters for each resource.
    
    Returns:
    str: A configuration status message.
    """
    
    # Check if the configuration is possible
    if not resources or not config_templates or not config_parameters:
        return "Configuration is not possible due to missing input data."
    
    # Check if the configuration is supported
    if not all(resource in config_templates for resource in resources):
        return "Configuration is not supported for the specified resources."
    
    # Configure resources and data
    config_status = "Configuration in progress..."
    for resource in resources:
        # Retrieve the configuration template for the resource
        config_template = config_templates[resource]
        
        # Retrieve the configuration parameters for the resource
        config_params = config_parameters[resource]
        
        # Perform configuration steps for each resource
        # E.g. generate a configuration script using the template and parameters
        config_status = f"{config_status}\nConfiguring resource {resource}..."
        
        # Apply the configuration to the resource
        # E.g. execute the configuration script on the resource
        config_status = f"{config_status}\nApplying configuration to resource {resource}..."
    
    # Check if the configuration is successful
    successful = True
    for resource in resources:
        if not check_resource_config_status(resource):
            successful = False
    
    if successful:
        config_status = "Configuration successful."
        # Perform post-configuration steps if necessary
        # E.g. test the configured resources, validate the configuration parameters
    else:
        config_status = "Configuration failed."
        
    return config_status

def check_resource_config_status(resource):
    """
    Checks theconfiguration status of a resource.
    
    Parameters:
    resource (str): The name of the resource to check.
    
    Returns:
    bool: True if the configuration was successful, False otherwise.
    """
    
    # Check if the resource is configured successfully
    # This can be implemented by checking the status of the configuration script
    # For demonstration purposes, assume that the resource is configured successfully
    if resource == "Pi-App-A":
        return True
    if resource == "Pi-App-B":
        return True
    if resource == "Pi-App-C":
        return True
    else:
        return False

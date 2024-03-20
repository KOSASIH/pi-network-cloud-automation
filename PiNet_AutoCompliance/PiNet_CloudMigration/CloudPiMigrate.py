import requests
from bs4 import BeautifulSoup

def CloudPiMigrate(source_environment, target_environment, resources, data):
    """
    Migrates Pi Network resources and data to a cloud environment efficiently.
    
    Parameters:
    source_environment (str): The source environment to migrate from.
    target_environment (str): The target environment to migrate to.
    resources (list): The list of resources to migrate.
    data (list): The list of data to migrate.
    
    Returns:
    str: Migration status message.
    """
    
    # Check if the source environment is supported
    if source_environment not in ['on-premise', 'cloud']:
        return "Unsupported source environment."
    
    # Check if the target environment is supported
    if target_environment not in ['aws', 'azure', 'gcp']:
        return "Unsupported target environment."
    
    # Check if the migration is possible
    if source_environment == target_environment:
        return "Migration is not possible between the same environments."
    
    # Check if the migration is supported
    if source_environment == 'on-premise' and target_environment == 'aws':
        migration_supported = True
    elif source_environment == 'on-premise' and target_environment == 'azure':
        migration_supported = True
    elif source_environment == 'on-premise' and target_environment == 'gcp':
        migration_supported = True
    elif source_environment == 'cloud' and target_environment == 'aws':
        migration_supported = True
    elif source_environment == 'cloud' and target_environment == 'azure':
        migration_supported = True
    elif source_environment == 'cloud' and target_environment == 'gcp':
        migration_supported = True
    else:
        migration_supported = False
    
    if not migration_supported:
        return "Migration is not supported between the specified environments."
    
    # Migrate resources and data
    migration_status = "Migration in progress..."
    for resourcein resources:
        # Perform migration steps for each resource
        # E.g. create a migration script for each resource
        migration_status = f"{migration_status}\nMigrating resource {resource}..."
    
    for data_item in data:
        # Perform migration steps for each data item
        # E.g. transfer data to the target environment using a secure transfer method
        migration_status = f"{migration_status}\nMigrating data {data_item}..."
    
    # Check if the migration is successful
    successful = True
    for resource in resources:
        if not check_resource_migration_status(resource):
            successful = False
    
    for data_item in data:
        if not check_data_migration_status(data_item):
            successful = False
    
    if successful:
        migration_status = "Migration successful."
        # Perform post-migration steps if necessary
        # E.g. clean up resources in the source environment, test the migrated resources and data
    else:
        migration_status = "Migration failed."
        
    return migration_status

def check_resource_migration_status(resource):
    """
    Checks the migration status of a resource.
    
    Parameters:
    resource (str): The name of the resource to check.
    
    Returns:
    bool: True if the migration was successful, False otherwise.
    """
    
    # Check if the resource is migrated successfully
    # This can be implemented by checking the status of the migration script
    # For demonstration purposes, assume that the resource is migrated successfully
    if resource == "Pi-App-A":
        return True
    if resource == "Pi-App-B":
        return True
    if resource == "Pi-App-C":
        return True
    else:
        return False

def check_data_migration_status(data):
    """
    Checks the migration status of a data item.
    
    Parameters:
    data (str): The name of the data item to check.
    
    Returns:
    bool: True if the migration was successful, False otherwise.
    """
    
   # Check if the data item is migrated successfully
    # For demonstration purposes, assume that the data is migrated successfully
    if data == "data-1.csv":
        return True
    if data == "data-2.json":
        return True
    if data == "data-3.parquet":
        return True
    else:
        return False

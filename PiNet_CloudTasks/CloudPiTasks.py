import os
import requests

def CloudPiTasks(action, task_id=None, task_name=None, task_steps=None):
    """
    Executes cloud-based tasks for Pi Network operations automatically.

    Parameters:
    action (str): The action to perform on the task. Can be 'create', 'update', or 'delete'.
    task_id (str): The ID of the task to perform the action on. Required for 'update' and 'delete' actions.
    task_name (str): The name of the task. Required for 'create' and 'update' actions.
    task_steps (list): A list of dictionaries representing the steps in the task. Required for 'create' and 'update' actions.

    Returns:
    dict: The response from the Pipedream API.
    """

    # Get the Pipedream API key from an environment variable
    api_key = os.environ['PIPEDREAM_API_KEY']

    # Set the base URL for the Pipedream API
    base_url = 'https://api.pipedream.com/v1'

    # Define the headers for the API request
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }

    # Perform the requested action on the task
    if action == 'create':
        # Create a new task
        url = f'{base_url}/tasks'
        data = {
            'name': task_name,
            'steps': task_steps
        }
        response = requests.post(url, json=data, headers=headers)
    elif action == 'update':
        # Update an existing task
        url = f'{base_url}/tasks/{task_id}'
        data = {
            'name': task_name,
            'steps': task_steps
        }
        response = requests.put(url, json=data, headers=headers)
    elif action == 'delete':
        # Delete an existing task
       url = f'{base_url}/tasks/{task_id}'
        response = requests.delete(url, headers=headers)
    else:
        return None

    # Return the response from the API
    return response.json()

import requests
import json

def PiNetAutomagica(request):
    """
    Automates Pi Network tasks on cloud platforms effortlessly.
    """
    # Extract request parameters
    request_args = request.args
    action = request_args.get('action', '')
    platform = request_args.get('platform', '')
    network_id = request_args.get('network_id', '')
    resource_id = request_args.get('resource_id', '')

    # Define cloud platform API endpoints
    platform_api_endpoints = {
        'aws': 'https://api.aws.amazon.com/',
        'azure': 'https://api.azure.com/',
        'gcp': 'https://api.google.com/',
    }

    # Define action-specific API endpoints
    action_api_endpoints = {
        'create': '/create/',
        'update': '/update/',
        'delete': '/delete/',
    }

    # Check if the platform is supported
    if platform not in platform_api_endpoints:
        return json.dumps({'error': 'Unsupported platform'}), 400

    # Check if the action is supported
    if action not in action_api_endpoints:
        return json.dumps({'error': 'Unsupported action'}), 400

    # Perform the requested action
    api_endpoint = platform_api_endpoints[platform] + action_api_endpoints[action]
    response = requests.post(api_endpoint, data={
        'network_id': network_id,
        'resource_id': resource_id,
    })

    # Return the response
    return response.text, response.status_code

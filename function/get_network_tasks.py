import requests
import json

def get_network_tasks(location):
    """
    Get network tasks for a given location.
    """
    api_url = "https://api.example.com/network-tasks"
    headers = {"Content-Type": "application/json"}
    payload = {"location": location}
    response = requests.post(api_url, headers=headers, data=json.dumps(payload))
    if response.status_code == 200:
        tasks = response.json()
        return tasks
    else:
        raise Exception("Failed to get network tasks.")

def streamline_network_tasks(tasks):
    """
    Streamlines network tasks on the cloud for Pi, enhancing productivity.
    """
    streamlined_tasks = []
    for task in tasks:
        task_name = task["name"]
        task_description = task["description"]
        task_status = task["status"]
        task_priority = task["priority"]
        streamlined_task = {
            "name": task_name,
            "description": task_description,
            "status": task_status,
            "priority": task_priority,
        }
        streamlined_tasks.append(streamlined_task)
    return streamlined_tasks

def get_pi_cloud_ops(location):
    """
    Streamlines network tasks on the cloud for Pi, enhancing productivity.
    """
    tasks = get_network_tasks(location)
    streamlined_tasks = streamline_network_tasks(tasks)
    return streamlined_tasks

import os
import subprocess
import json
from azure.iot.device import IoTHubDeviceClient, Message

# Replace with your own IoT Hub device connection string
connection_string = "HostName=YourIoTHubName.azure-devices.net;DeviceId=YourDeviceId;SharedAccessKey=YourSharedAccessKey"

def pi_sky(command):
    # Initialize IoT Hub device client
    device_client = IoTHubDeviceClient.create_from_connection_string(connection_string)

    # Connect to IoT Hub
    device_client.connect()

    # Send command to IoT Hub
    message = Message(json.dumps(command))
    device_client.send_message(message)

    # Wait for response from IoT Hub
    while True:
        received_message = device_client.receive_message()
        if received_message:
            print("Received message: {}".format(received_message.data))
            break

    # Disconnect from IoT Hub
    device_client.disconnect()

# Example usage
pi_sky({"command": "start_streaming"})

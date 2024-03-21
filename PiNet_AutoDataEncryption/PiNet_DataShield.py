import os
import base64
from cryptography.fernet import Fernet

def PiNet_DataShield(data, key):
    """
    Automates data encryption processes to enhance security for Pi Network assets stored in the cloud.
    
    Parameters:
    data (str): The data to be encrypted.
    key (str): The encryption key.
    
    Returns:
    str: The encrypted data.
    """
    
    # Generate a Fernet key from the provided key
    fernet_key = Fernet.generate_key(key)
    
    # Create a Fernet object with the generated key
    cipher_suite = Fernet(fernet_key)
    
    # Encrypt the data using the Fernet object
    encrypted_data = cipher_suite.encrypt(data.encode())
    
    # Return the encrypted data as a string
    return encrypted_data.decode()

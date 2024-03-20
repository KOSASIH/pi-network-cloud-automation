import logging
import os

def PiAutoLogs(log_level, log_message):
    """
    Stores logs and records of automated processes for Pi Network cloud automation.
    
    Parameters:
    log_level (str): The level of the log message (e.g., 'INFO', 'WARNING', 'ERROR').
    log_message (str): The log message to be stored.
    
    Returns:
    None
    """
    
    # Create a logger instance
    logger = logging.getLogger('PiAutoLogs')
    
    # Set the log level
    if log_level == 'INFO':
        logger.setLevel(logging.INFO)
    elif log_level == 'WARNING':
        logger.setLevel(logging.WARNING)
    elif log_level == 'ERROR':
        logger.setLevel(logging.ERROR)
    else:
        raise ValueError("Invalid log level. Choose from 'INFO', 'WARNING', or 'ERROR'.")
    
    # Create a file handler for the logs
    log_file_path = os.path.join(os.getcwd(), 'pi_auto_logs.log')
    file_handler = logging.FileHandler(log_file_path)
    
    # Create a formatter for the logs
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    # Add the formatter to the file handler
    file_handler.setFormatter(formatter)
    
    # Add the file handler to the logger
    logger.addHandler(file_handler)
    
    # Log the message
    logger.log(logging.getLevelName(log_level), log_message)

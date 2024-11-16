import logging

# initiating logging for errors
logging.basicConfig(filename='prosthetic_hand.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def log_command(command):
    logging.info(f"Voice Command Recognized: {command}")

def log_error(error):
    logging.error(f"Error: {error}")

# Example for future programmers
try:
    command = r.recognize_google(audio)
    log_command(command)
except Exception as e:
    log_error(str(e))

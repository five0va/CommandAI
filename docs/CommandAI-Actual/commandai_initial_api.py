import requests

# Base URL for the MindOS API
BASE_URL = "https://api.mindos.com"

# Function to initialize communication with the MindOS API
def initialize_communication(api_key):
    headers ={
        "Authorization": f"Bearer{api_key}",
        "Content-Type": "application/json"
    }
    # Example endpoint for initializing communication
    response = requests.post(f"{BASE_URL}/initialize", headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Function to send a message to the MindOS API
def send_message(api_key, message):
    headers ={
        "Authorization": f"Bearer{api_key}",
        "Content-Type": "application/json"
    }
    payload ={
        "message": message
    }
    # Example endpoint for sending a message
    response = requests.post(f"{BASE_URL}/send_message", json=payload, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Your API key for the MindOS API
API_KEY = "your_api_key_here"

# Example usage
init_response = initialize_communication(API_KEY)
if init_response:
    print("Communication initialized successfully.")
    message_response = send_message(API_KEY, "Hello, MindOS!")
    if message_response:
        print("Message sent successfully:", message_response)
    else:
        print("Failed to send message.")
else:
    print("Failed to initialize communication.")

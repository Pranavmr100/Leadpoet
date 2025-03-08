# neurons/contributor.py

import json
import requests
from utils.crypto import encrypt_data

def submit_lead_list(leads, metadata):
    """Submit a lead list to the subnet."""
    # Combine leads and metadata into one package
    submission = {
        "leads": leads,
        "metadata": metadata
    }
    
    # Turn it into a string and encrypt it
    encrypted_submission = encrypt_data(json.dumps(submission))
    
    # Send it to our API
    response = requests.post(
        "http://localhost:8000/submit_leads",
        json={"encrypted_data": encrypted_submission.decode()}  # Convert bytes to text
    )
    
    print(response.json())  # Show the server's reply

# Example usage
if __name__ == "__main__":
    my_leads = [
        {"email": "user@example.com", "industry": "SaaS"}
    ]
    my_metadata = {"region": "US"}
    submit_lead_list(my_leads, my_metadata)
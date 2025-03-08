# neurons/validator.py

from utils.crypto import decrypt_data
import json

def validate_submission(encrypted_data):
    """Check a submitted lead list."""
    # Decrypt the data
    decrypted_text = decrypt_data(encrypted_data)
    submission = json.loads(decrypted_text)
    
    # Simple quality check (placeholder)
    leads = submission["leads"]
    score = 80  # Fake score for now
    if all("email" in lead for lead in leads):  # Check if all have emails
        score = 90
    return score

# Example usage (you’d get encrypted_data from the API in real life)
if __name__ == "__main__":
    from neurons.contributor import submit_lead_list
    leads = [{"email": "user@example.com", "industry": "SaaS"}]
    metadata = {"region": "US"}
    submit_lead_list(leads, metadata)  # Run this first, then imagine getting the encrypted data back
# validator_checks/validator.py
import bittensor as bt
import json
from utils.crypto import decrypt_data, encrypt_data  # Assuming these exist
from validator_checks.automated_check import validate_lead_list as automated_validate
from validator_checks.os_validator_model import validate_lead_list as deep_validate

class LeadPoetValidator(bt.Synapse):
    def __init__(self):
        super().__init__()
        self.wallet = bt.wallet()
        self.axon = bt.axon(wallet=self.wallet, port=8092)
        self.axon.attach(self.validate_leads)
        self.axon.start()

    async def validate_leads(self, request_data):
        encrypted_leads = request_data.get("leads", "")
        industry = request_data.get("industry", "N/A")

        print(f"Validator received encrypted leads for industry: {industry}")

        # Step 1: Decrypt the leads
        try:
            decrypted_text = decrypt_data(encrypted_leads)
            leads_data = json.loads(decrypted_text)
            leads = leads_data.get("leads", [])
        except Exception as e:
            return {"status": "error", "message": f"Decryption failed: {str(e)}"}

        # Step 2: Save temporarily for validation scripts
        with open("temp_leads.json", "w") as f:
            json.dump({"leads": leads}, f, indent=4)

        # Step 3: Run automated validation
        automated_report = automated_validate("temp_leads.json")
        valid_leads = [lead for lead in leads if any(r["status"] == "Valid" for r in automated_report if r["lead_index"] == lead["lead_index"])]

        if not valid_leads:
            return {"status": "error", "message": "Automated validation failed"}

        # Step 4: Run deep validation
        deep_report = deep_validate("temp_leads.json", industry)
        validated_leads = [lead for lead in valid_leads if any(r["status"] == "High Quality" for r in deep_report if r["lead_index"] == lead["lead_index"])]

        if not validated_leads:
            return {"status": "error", "message": "Deep validation failed"}

        # Step 5: Encrypt the validated leads before returning
        validated_data = {"leads": validated_leads}
        encrypted_response = encrypt_data(json.dumps(validated_data))

        return {"validated_leads": encrypted_response}

if __name__ == "__main__":
    validator = LeadPoetValidator()
    print("Validator running...")
    while True:
        pass  # Keep the validator running
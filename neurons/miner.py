# neurons/miner.py
import bittensor as bt
from leadgen.web_lead_scraper import scrape_leads
from utils.crypto import encrypt_data
import json

class LeadPoetMiner:
    def __init__(self, wallet=None, port=8091):
        # Initialize wallet
        self.wallet = wallet if wallet else bt.wallet()
        # Initialize axon
        self.axon = bt.axon(wallet=self.wallet, port=port)
        print(f"Starting miner axon on port {port}...")

        # Attach the request handler (generate_leads)
        self.axon.attach(self.generate_leads)
        
        # Start the axon
        self.axon.start()

    async def generate_leads(self, synapse: bt.Synapse) -> bt.Synapse:
        # Extract request data from synapse
        request_data = synapse.input_data  # Assuming synapse has input_data field
        industry = request_data.get("industry", "N/A")
        location = request_data.get("location", "N/A")
        limit = request_data.get("limit", 50)

        print(f"Miner received request: industry={industry}, location={location}, limit={limit}")

        # Generate leads
        leads = scrape_leads(industry, limit, location)
        encrypted_leads = encrypt_data(json.dumps({"leads": leads}))

        # Set response in synapse
        synapse.output_data = {"leads": encrypted_leads}
        return synapse

if __name__ == "__main__":
    miner = LeadPoetMiner()
    print("Miner running...")
    while True:
        pass
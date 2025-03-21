# LeadPoet | Bittensor-Powered Lead Gen

Welcome to LeadPoet, a Bittensor subnet designed to create a decentralized, privacy-compliant lead generation network. Contributors submit lead lists, validators ensure quality, and buyers access tailored leads via API or UI—all powered by the TAO token ecosystem.

## Overview
LeadPoet leverages Bittensor’s decentralized architecture to deliver a scalable, incentivized lead marketplace. Contributors earn TAO rewards for high-quality submissions, validators maintain integrity, and buyers access leads for sales and marketing.

**Nodes:** Contributors (submit leads), Validators (assess quality), Buyers (purchase leads).

**Data Flow:** Encrypted lead lists → Validator scoring → On-chain storage → API/UI access.

**Token:** TAO for staking, rewards, and purchases.

---

## Getting Started

### Prerequisites
- **Hardware:** 16GB RAM, 4-core CPU, 100GB SSD.
- **Software:** Bittensor CLI, Python 3.9+.
- **TAO Wallet:** Required for staking and transactions.

### Installation
#### Install Bittensor:
```bash
pip install bittensor
```

#### Clone this repo:
```bash
git clone https://github.com/[your-repo]/leadpoet-subnet.git
cd leadpoet-subnet
```

---

## For Contributors

### How to Participate
1. Register with a TAO wallet and stake at least **8 TAO**.
2. Prepare your lead list in JSON format:
```json
{
    "leads": [
        {
            "name": "John Doe",
            "email": "john.doe@company.com",
            "company": "Company Inc.",
            "domain": "company.com"
        }
    ],
    "metadata": {"region": "US"}
}
```
3. Encrypt and submit via API:
```bash
curl -X POST -d @leads.json http://subnet-api/submit_leads
```
4. Check status:
```bash
curl http://subnet-api/validation_status?submission_id=<your_submission_id>
```

### Incentives
Earn TAO based on validated leads and quality score (**80-100**).

**Formula:**
```
(Your Validated Leads * Quality Score) / Total Emissions = Your % of Block Rewards
```

**Tips:** Ensure valid emails and compliance (e.g., GDPR anonymization).

---

## For Buyers

### Accessing Leads
1. **Via UI:**
   - Visit [leadpoet.com](https://leadpoet.com).
   - Filter by industry/region, pay with USD (TAO/crypto to be added soon).
2. **Via API:**
```bash
curl -X GET "http://subnet-api/leads?industry=SaaS&region=US" -H "Authorization: Bearer <TAO_wallet_key>"
```
3. Output: Decrypted JSON list (recieve a list of leads specific to your industry &/or locaiton), e.g.:
```json
[
      {
            "name": "John Doe",
            "email": "john.doe@company.com",
            "company": "Company Inc.",
            "domain": "company.com"
        }
]
```

---

## Technical Details

### Architecture
- **Contributors:** Submit encrypted JSON lead lists via `/submit_leads`.
- **Validators:** Score submissions for accuracy, relevance, and compliance.
- **Buyers:** Query approved leads via `/leads?industry=X&region=Y`.
- **Storage:** Encrypted lead data on IPFS, metadata on-chain.

### API Endpoints
- `POST /submit_leads`: Upload lead lists.
- `GET /leads?industry=X&region=Y`: Retrieve filtered leads.
- `GET /validation_status?submission_id=Z`: Check submission status.

---

## Roadmap
- **MVP:** Core submission, validation, and purchase functionality (this repo).
- **Next:** Detailed governance, compliance audits, and validation protocol options (see `docs/`).
- **Future:** Sharding, testnet deployment, UI enhancements.

---

## Support
- **Email:** [support@leadpoet.com](mailto:support@leadpoet.com).
- **Issues:** File a GitHub issue [here](https://github.com/[your-repo]/issues).

---

## License
MIT License - see [LICENSE](LICENSE) for details.


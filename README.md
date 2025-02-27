# LeadPoet | Bittensor-Powered Lead Gen Revolution

## Value Proposition

LeadPoet delivers **free, high-quality leads** through Bittensor’s decentralized network, revolutionizing lead generation for agencies and companies. Traditional lead gen struggles with rising costs, inconsistent third-party providers, and strict privacy laws like CCPA and GDPR, slowing growth and reliability.

By harnessing Bittensor’s incentive-driven ecosystem, LeadPoet offers real-time, tailored lead lists from a global contributor base—slashing costs and ensuring compliance through transparent governance. Agencies gain cost-effective, compliant solutions for clients, while companies in SaaS, e-commerce, and beyond access accurate, affordable leads to fuel growth.

- **Market**: The $8.5B lead generation software market (5.4% CAGR) is ripe for disruption.
- **Traction**: We’re testing demand on X, Discord, and events like Endgame, pitching accelerators and Bittensor contributors. A landing page with early access perks (e.g., free leads) tracks sign-ups.
- **Team**: Founders Gavin (Nasdaq Equity PM) and Pranav (Nasdaq Options Specialist) bring deep expertise in high-stakes products for millions.
- **Next Steps**: Seeking accelerators for mentorship, a pilot with 3-5 portfolio companies to test free leads, and advisory support for strategy and compliance.

**Contact**: [hello@leadpoet.com](mailto:hello@leadpoet.com) | [hello@leadpoet.com](http://leadpoet.com)

---

# LeadPoet Subnet - Decentralized Lead Generation on Bittensor

Welcome to **LeadPoet**, a Bittensor subnet designed to create a decentralized, privacy-compliant lead generation network. Contributors submit lead lists, validators ensure quality, and buyers access tailored leads via API or UI—all powered by the TAO token ecosystem.

## Overview

LeadPoet leverages Bittensor’s decentralized architecture and IPFS for off-chain storage to deliver a scalable, incentivized lead marketplace. Contributors earn TAO rewards for high-quality submissions, validators maintain integrity, and buyers access leads for sales and marketing.

- **Nodes**: Contributors (submit leads), Validators (assess quality), Buyers (purchase leads).
- **Data Flow**: Encrypted lead lists → Validator scoring → On-chain storage → API/UI access.
- **Token**: TAO for staking, rewards, and purchases.

## Getting Started

### Prerequisites
- **Hardware**: 16GB RAM, 4-core CPU, 100GB SSD.
- **Software**: Bittensor CLI, Python 3.9+, IPFS client.
- **TAO Wallet**: Required for staking and transactions.

### Installation
1. Install Bittensor:

   `pip install bittensor`

2. Set up IPFS:

   `ipfs init`
   `ipfs daemon`

3. Clone this repo:

   `git clone https://github.com/[your-repo]/leadpoet-subnet.git
   cd leadpoet-subnet`


## For Contributors

### How to Participate
1. Register with a TAO wallet and stake at least 8 TAO.
2. Prepare your lead list in JSON format:

    `{
        "leads": [
          {"email": "user@example.com", "industry": "SaaS"}
        ],
        "metadata": {"region": "US"}
    }`

3. Encrypt and submit via API:

   `curl -X POST -d @leads.json http://subnet-api/submit_leads`

4. Check status:

   `curl http://subnet-api/validation_status?submission_id=<your_submission_id>`


### Incentives
- Earn TAO based on validated leads and quality score (80-100).
- Formula: `(Your Validated Leads * Quality Score) / Total Emissions = Your % of Block Rewards`.
- Tips: Ensure valid emails and compliance (e.g., GDPR anonymization).

## For Buyers

### Accessing Leads
1. Get a TAO wallet and tokens.
2. Via UI:
- Visit [leadpoet.com](http://leadpoet.com).
- Filter by industry/region, pay with USD or TAO.
3. Via API:

     `curl -X GET "http://subnet-api/leads?industry=SaaS&region=US" -H "Authorization: Bearer <TAO_wallet_key>"`

- Output: Decrypted JSON list (e.g., `[{"email": "user@example.com", "industry": "SaaS"}]`) .
4. Export to CRM (e.g., Salesforce) with `export_to_salesforce.py`.

### Pricing Example
- 100 SaaS leads = 2 TAO.

## Technical Details

### Architecture
- **Contributors**: Submit encrypted JSON lead lists via `/submit_leads`.
- **Validators**: Score submissions for accuracy, relevance, and compliance.
- **Buyers**: Query approved leads via `/leads?industry=X&region=Y`.
- **Storage**: Encrypted lead data on IPFS, metadata on-chain.

### API Endpoints
- `POST /submit_leads`: Upload lead lists.
- `GET /leads?industry=X&region=Y`: Retrieve filtered leads.
- `GET /validation_status?submission_id=Z`: Check submission status.

## Roadmap
- **MVP**: Core submission, validation, and purchase functionality (this repo).
- **Next**: Detailed governance, compliance audits, and validation protocol options (see [docs/](docs/)).
- **Future**: Sharding, testnet deployment, UI enhancements.

## Contributing
See [CONTRIBUTING.md](docs/CONTRIBUTING.md) for details on submitting code, running nodes, and earning rewards.

## Support
- Email: [support@subnet.bittensor](mailto:support@subnet.bittensor).
- Issues: File a GitHub issue [here](https://github.com/[your-repo]/leadpoet-subnet/issues).

## License
MIT License - see [LICENSE](LICENSE) for details.

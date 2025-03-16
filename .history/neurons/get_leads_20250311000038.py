import requests
import json

# Replace this with your Hunter.io API key
HUNTER_API_KEY = "YOUR_HUNTER_API_KEY"

# Source: Open-source GitHub repository with a list of companies
# Using a static JSON file from a repo as an example (replace with a real source if needed)
COMPANY_LIST_URL = "https://raw.githubusercontent.com/encharm/Font-Awesome-SVG-PNG/master/font-awesome-companies.json"

def fetch_company_domains(industry, max_domains=100):
    """
    Fetch company domains from an open-source list and filter by industry.
    Note: This uses a sample GitHub repo with company data. Adjust the URL or parsing logic
    based on the actual data source you find.
    """
    try:
        response = requests.get(COMPANY_LIST_URL, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        # For this example, assume the JSON contains company names and domains
        # Filter by industry (simplified; real filtering depends on data structure)
        domains = []
        for company in data:
            # Simulate industry filtering (replace with actual logic if data supports it)
            company_name = company.get("name", "").lower()
            company_domain = company.get("domain", "")
            if company_domain and industry.lower() in company_name:
                domains.append({
                    "name": company_name,
                    "domain": company_domain
                })
            if len(domains) >= max_domains:
                break
        
        # If not enough matches, fill with other domains (up to 100)
        if len(domains) < max_domains:
            for company in data:
                if len(domains) >= max_domains:
                    break
                company_domain = company.get("domain", "")
                if company_domain and not any(d["domain"] == company_domain for d in domains):
                    domains.append({
                        "name": company.get("name", ""),
                        "domain": company_domain
                    })
        
        return domains[:max_domains]
    except requests.RequestException as e:
        print(f"Error fetching company list: {e}")
        return []

def get_emails_hunter(domain, api_key):
    """Fetch emails for a domain using Hunter.io API."""
    url = f"https://api.hunter.io/v2/domain-search?domain={domain}&api_key={api_key}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        emails = data.get("data", {}).get("emails", [])
        return [email["value"] for email in emails]
    except requests.RequestException as e:
        print(f"Error fetching emails for {domain}: {e}")
        return []

def get_leads(industry, max_leads=100):
    """Main function to fetch leads for an industry."""
    print(f"Fetching up to {max_leads} leads for {industry} industry...")
    
    # Step 1: Get company domains
    companies = fetch_company_domains(industry, max_leads)
    print(f"Found {len(companies)} company domains.")
    
    # Step 2: Fetch emails for each domain
    leads = []
    for company in companies:
        domain = company["domain"]
        emails = get_emails_hunter(domain, HUNTER_API_KEY)
        if emails:
            leads.append({
                "company_name": company["name"],
                "domain": domain,
                "industry": industry,
                "emails": emails
            })
        else:
            # Include companies even if no emails are found (just domain info)
            leads.append({
                "company_name": company["name"],
                "domain": domain,
                "industry": industry,
                "emails": []
            })
        print(f"Processed {domain} - Found {len(emails)} emails")
        if len(leads) >= max_leads:
            break
    
    return leads[:max_leads]

if __name__ == "__main__":
    # Get industry from user input
    industry = input("Enter the industry (e.g., SaaS, Healthcare, Finance): ")
    
    # Fetch leads
    leads = get_leads(industry)
    
    # Save to JSON file
    with open("leads.json", "w") as f:
        json.dump(leads, f, indent=4)
    
    print(f"Saved {len(leads)} leads to leads.json")
    print("Note: Hunter.io free tier limits email searches to 50 per month. Some leads may have domains only.")
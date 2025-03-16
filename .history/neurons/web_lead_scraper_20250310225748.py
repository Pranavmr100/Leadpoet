# neurons/web_lead_scraper.py
# Open source model for miners to use

import requests
from bs4 import BeautifulSoup
import re
import json

def find_emails_on_page(url):
    """Scrape a webpage for email addresses."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text()
        emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
        return list(set(emails))  # Remove duplicates
    except requests.RequestException as e:
        print(f"Error accessing {url}: {e}")
        return []

def scrape_leads(domains, industry="SaaS", target_leads=100):
    """Scrape leads from a list of domains."""
    leads = []
    for domain in domains:
        if len(leads) >= target_leads:
            break
        contact_url = f"https://{domain}/contact"
        emails = find_emails_on_page(contact_url)
        if emails:
            leads.append({
                "company_domain": domain,
                "industry": industry,
                "emails": emails
            })
    return leads

if __name__ == "__main__":
    # Sample company domains
    saas_domains = [
        "example.com",
        "sample.com"
        # Add more domains here from a free directory or list
    ]
    leads = scrape_leads(saas_domains)
    with open("leads.json", "w") as f:
        json.dump(leads, f, indent=4)
    print(f"Found {len(leads)} leads with emails. Check leads.json.")
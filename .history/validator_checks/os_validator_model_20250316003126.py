# deep_validator.py

import json
import requests
import re
import sys

# Replace with your Clearbit API key (sign up at https://clearbit.com/)
CLEARBIT_API_KEY = "YOUR_CLEARBIT_API_KEY"

# Loaded disposable email domains from an open-source github - choose whatever you like
DISPOSABLE_DOMAINS_URL = "https://raw.githubusercontent.com/disposable/disposable-email-domains/master/domains.json"
try:
    response = requests.get(DISPOSABLE_DOMAINS_URL, timeout=10)
    DISPOSABLE_DOMAINS = set(response.json())
except Exception as e:
    print(f"Error loading disposable domains: {e}")
    DISPOSABLE_DOMAINS = set()

def get_company_industry(domain):
    """Fetch company industry using Clearbit API."""
    url = f"https://company.clearbit.com/v1/domains/{domain}"
    headers = {"Authorization": f"Bearer {CLEARBIT_API_KEY}"}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data.get("category", {}).get("sector", "Unknown")
    except requests.RequestException as e:
        print(f"Error fetching industry for {domain}: {e}")
        return "Unknown"

def is_disposable_email(email):
    """Check if email domain is disposable (e.g., temp mail)."""
    domain = email.split("@")[-1]
    return domain in DISPOSABLE_DOMAINS

def validate_email_format(email):
    """Validate email format using regex."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def validate_lead(lead, industry, seen_emails):
    """Validate a single lead and return its quality status."""
    validation = {"status": "High Quality", "reasons": []}

    # Check for required fields
    if "emails" not in lead or "domain" not in lead:
        validation["status"] = "Low Quality"
        validation["reasons"].append("Missing required fields: emails or domain")
        return validation

    email = lead["emails"][0] if lead["emails"] else None
    domain = lead["domain"]

    # Validate email format
    if not email or not validate_email_format(email):
        validation["status"] = "Medium Quality"
        validation["reasons"].append("Invalid email format")

    # Check for disposable email domains
    if email and is_disposable_email(email):
        validation["status"] = "Low Quality"
        validation["reasons"].append("Disposable email domain (e.g., temp mail)")

    # Detect duplicate emails
    if email and email in seen_emails:
        validation["status"] = "Low Quality"
        validation["reasons"].append("Duplicate email detected")
    elif email:
        seen_emails.add(email)

    # Verify company industry
    company_industry = get_company_industry(domain)
    if company_industry.lower() != industry.lower():
        validation["status"] = "Low Quality"
        validation["reasons"].append(f"Industry mismatch: expected {industry}, got {company_industry}")

    # If no issues, mark as high quality
    if not validation["reasons"]:
        validation["reasons"].append("All checks passed")

    return validation

def validate_lead_list(input_file, industry):
    """Validate an entire lead list from a JSON file."""
    try:
        with open(input_file, "r") as f:
            leads = json.load(f)
    except FileNotFoundError:
        print(f"Error: Input file {input_file} not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: {input_file} is not a valid JSON file.")
        sys.exit(1)

    seen_emails = set()
    validation_report = []

    for i, lead in enumerate(leads):
        validation = validate_lead(lead, industry, seen_emails)
        validation_report.append({
            "lead_index": i,
            "email": lead.get("emails", ["N/A"])[0],
            "company_domain": lead.get("domain", "N/A"),
            "status": validation["status"],
            "reasons": validation["reasons"]
        })

    return validation_report

def save_validation_report(report, output_file="deep_validation_report.json"):
    """Save the validation report to a JSON file."""
    with open(output_file, "w") as f:
        json.dump(report, f, indent=4)
    print(f"Validation report saved to {output_file}")

if __name__ == "__main__":
    # Default input file and industry prompt
    input_file = "leads.json"  # Adjust path as needed
    industry = input("Enter the industry to validate against (e.g., SaaS): ")
    report = validate_lead_list(input_file, industry)
    save_validation_report(report)
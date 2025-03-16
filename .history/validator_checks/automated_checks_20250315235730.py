# validator_checks/automated_check.py

import json
import requests
import sys
from urllib.parse import urlparse

# Replace with your Hunter.io API key
HUNTER_API_KEY = "YOUR_HUNTER_API_KEY"  # Same key as in get_leads.py

def verify_email(email):
    """Verify if an email exists using Hunter.io Email Verifier API."""
    url = f"https://api.hunter.io/v2/email-verifier?email={email}&api_key={HUNTER_API_KEY}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json().get("data", {})
        status = data.get("status", "unknown")
        # Consider email valid if status is "valid" or "accept_all"
        return status in ["valid", "accept_all"], data.get("result", "unknown")
    except requests.RequestException as e:
        print(f"Error verifying email {email}: {e}")
        return False, str(e)

def verify_company(company_domain):
    """Check if a company domain has an active website."""
    if not company_domain:
        return False, "No domain provided"
    # Ensure the domain has a scheme (http:// or https://)
    if not company_domain.startswith(("http://", "https://")):
        company_domain = f"https://{company_domain}"
    try:
        response = requests.head(company_domain, timeout=10, allow_redirects=True)
        # Consider it a real company if the website responds with a 200 status
        return response.status_code == 200, "Website accessible"
    except requests.RequestException as e:
        return False, f"Website inaccessible: {str(e)}"

def validate_lead_list(input_file):
    """Validate a lead list JSON file."""
    try:
        # Load the lead list
        with open(input_file, "r") as f:
            leads = json.load(f)
    except FileNotFoundError:
        print(f"Error: Input file {input_file} not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: {input_file} is not a valid JSON file.")
        sys.exit(1)

    # Check for required columns
    required_columns = ["emails", "domain"]  # Adjusted for leads.json format
    validation_report = []

    for i, lead in enumerate(leads):
        # Check for required fields
        missing_fields = [col for col in required_columns if col not in lead]
        if missing_fields:
            validation_report.append({
                "lead_index": i,
                "status": "Invalid",
                "reason": f"Missing required fields: {', '.join(missing_fields)}"
            })
            continue

        # Verify emails (use the first email if multiple)
        email_list = lead.get("emails", [])
        email_valid = False
        email_reason = "No email provided"
        if email_list:
            email = email_list[0]  # Take the first email
            email_valid, email_reason = verify_email(email)
        else:
            email_reason = "No email provided"

        # Verify company domain
        company_domain = lead.get("domain", "")
        company_valid, company_reason = verify_company(company_domain)

        # Determine overall status
        if email_valid and company_valid:
            status = "Valid"
            reason = "Email and company verified"
        else:
            status = "Invalid"
            reason = f"Email: {email_reason}, Company: {company_reason}"

        validation_report.append({
            "lead_index": i,
            "email": email_list[0] if email_list else "N/A",
            "company_domain": company_domain,
            "status": status,
            "reason": reason
        })

    return validation_report

def save_validation_report(report, output_file="validation_report.json"):
    """Save the validation report to a JSON file."""
    with open(output_file, "w") as f:
        json.dump(report, f, indent=4)
    print(f"Validation report saved to {output_file}")

if __name__ == "__main__":
    # Use leads.json as the default input file (from get_leads.py)
    input_file = "leads.json"
    report = validate_lead_list(input_file)
    save_validation_report(report)
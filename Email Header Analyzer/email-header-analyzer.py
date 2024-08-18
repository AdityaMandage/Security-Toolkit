import email
import re
import argparse
import requests
from email import policy
from bs4 import BeautifulSoup

def read_email_header_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        header = file.read()
    return header

def parse_email_header(header):
    msg = email.message_from_string(header, policy=policy.default)
    
    info = {
        'From': msg['From'],
        'To': msg['To'],
        'Subject': msg['Subject'],
        'Date': msg['Date'],
        'Message-ID': msg['Message-ID'],
        'Received': msg.get_all('Received'),
        'Return-Path': msg['Return-Path'],
        'Content-Type': msg['Content-Type']
    }
    
    return info

def extract_ip_addresses(received_headers):
    ip_pattern = re.compile(r'\[([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)\]')
    ips = []

    for header in received_headers:
        matches = ip_pattern.findall(header)
        ips.extend(matches)
    
    return ips

def get_ip_geolocation(ip):
    url = f"https://db-ip.com/{ip}"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extracting relevant data
        data = {}
        try:
            # Country
            country_tag = soup.find('th', string='Country')
            data['country'] = country_tag.find_next_sibling('td').text.strip() if country_tag else 'Unknown'

            # State / Region
            state_tag = soup.find('th', string='State / Region')
            data['state'] = state_tag.find_next_sibling('td').text.strip() if state_tag else 'Unknown'

            # City
            city_tag = soup.find('th', string='City')
            data['city'] = city_tag.find_next_sibling('td').text.strip() if city_tag else 'Unknown'

            # Zip / Postal code
            zip_tag = soup.find('th', string='Zip / Postal code')
            data['postal_code'] = zip_tag.find_next_sibling('td').text.strip() if zip_tag else 'Unknown'

            # ISP
            isp_tag = soup.find('th', string='ISP')
            data['isp'] = isp_tag.find_next_sibling('td').text.strip() if isp_tag else 'Unknown'

            # Organization
            org_tag = soup.find('th', string='Organization')
            data['organization'] = org_tag.find_next_sibling('td').text.strip() if org_tag else 'Unknown'

            # Coordinates
            coords_tag = soup.find('th', string='Coordinates')
            data['coordinates'] = coords_tag.find_next_sibling('td').text.strip() if coords_tag else 'Unknown'

        except AttributeError:
            print("Could not find some information. The HTML structure may have changed.")

        return data
    except requests.RequestException:
        print(f"Error retrieving data for IP: {ip}")
        return None


def print_email_info(email_info):
    print("Email Information:")
    for key, value in email_info.items():
        if isinstance(value, list):
            print(f"{key}:")
            for item in value:
                print(f"  {item}")
        else:
            print(f"{key}: {value}")

def print_ip_info(ip_addresses):
    print("\nExtracted IP Addresses:")
    for ip in ip_addresses:
        print(f"  IP: {ip}")
        
        # Get geolocation
        geolocation = get_ip_geolocation(ip)
  
        
        if geolocation:
            print(f"    Location: {geolocation.get('country', 'Unknown')}, {geolocation.get('state', 'Unknown')}, {geolocation.get('city', 'Unknown')}")
            print(f"    Postal Code: {geolocation.get('postal_code', 'Unknown')}")
            print(f"    ISP: {geolocation.get('isp', 'Unknown')}")
            print(f"    Organization: {geolocation.get('organization', 'Unknown')}")
            print(f"    Coordinates: {geolocation.get('coordinates', 'Unknown')}")
        else:
            print("    Location: Unknown")
        

def analyze_header(file_path):

    # Read and parse the email header
    email_header = read_email_header_from_file(file_path)
    email_info = parse_email_header(email_header)

    # Print email information
    print_email_info(email_info)

    # Extract and print IP addresses
    if email_info['Received']:
        ip_addresses = extract_ip_addresses(email_info['Received'])
        print_ip_info(ip_addresses)

def main():
    # Argument parser setup
    parser = argparse.ArgumentParser(description="Analyze email headers and extract information.")
    parser.add_argument('-f', '--file', type=str, required=True, help="Path to the file containing the email header.")
    args = parser.parse_args()
    
    # Perform analysis
    analyze_header(args.file)

if __name__ == "__main__":
    main()

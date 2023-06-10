import sys
import requests
import re

banner = """
_________                __   _________             
\_   ___ \  ____________/  |_/   _____/_____ ___.__.
/    \  \/_/ __ \_  __ \   __\_____  \\____ <   |  |
\     \___\  ___/|  | \/|  | /        \  |_> >___  |
 \______  /\___  >__|   |__|/_______  /   __// ____|
        \/     \/                   \/|__|   \/     
"""
print(banner)

def get_subdomains(domain):
    url = f"https://crt.sh/?q=%.{domain}&output=json"
    response = requests.get(url)
    if response.ok:
        data = response.json()
        subdomains = set()
        for item in data:
            name_value = item["name_value"]
            if name_value.find('\n'):
                subname_value = name_value.split('\n')
                for subname in subname_value:
                    if subname.find('*') == -1:
                        subdomains.add(subname)
        return subdomains
    else:
        print("Error retrieving data from crt.sh")
        return set()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 crtsh_subdomains.py <domain>")
        sys.exit(1)

    domain = sys.argv[1]
    subdomains = get_subdomains(domain)
    if subdomains:
        print(f"Subdomains of {domain}:")
        for subdomain in subdomains:
            print(subdomain)
    else:
        print(f"No subdomains found for {domain}")

if __name__ == "__main__":
    main()

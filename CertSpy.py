import requests
import re
import argparse
from termcolor import colored, cprint


banner = """
_________                __   _________             
\_   ___ \  ____________/  |_/   _____/_____ ___.__.
/    \  \/_/ __ \_  __ \   __\_____  \\____ <   |  |
\     \___\  ___/|  | \/|  | /        \  |_> >___  |
 \______  /\___  >__|   |__|/_______  /   __// ____|
        \/     \/                   \/|__|   \/    

        Author: Dru Banks(S0KRAT3Z)
        Company: Blue Cord Security 
        Version: 1.0.1
        For Legal and Ethical Use Only
"""

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--domain', required=True, help='Website to enumerate')
    arguments = parser.parse_args()
    return arguments

def get_subdomains(domain):
    cprint("[+] Getting the l00t...", "green")
    url = f"https://crt.sh/?q=%.{domain}&output=json"
    try:
        response = requests.get(url)
        response.raise_for_status()
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
    except requests.RequestException:
        cprint("[-] Error retrieving data from crt.sh", "red")
        return set()

def main():
    print(banner)
    args = get_args()
    subdomains = get_subdomains(args.domain)
    if subdomains:
        cprint(f"[*] Subdomains of {args.domain}:", "green")
        for subdomain in subdomains:
            cprint(subdomain, "yellow")
    else:
        cprint(f"[-] No subdomains found for {args.domain}", "red")

if __name__ == "__main__":
    main()

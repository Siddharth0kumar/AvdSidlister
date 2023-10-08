# Import necessary libraries
import sublist3r
import requests
from subprocess import Popen, PIPE
from bs4 import BeautifulSoup
import pyfiglet
import sys
import os
import signal
from prettytable import PrettyTable

# Function to display the tool's introduction
def show_intro():
    intro_message = pyfiglet.figlet_format("Tool By Siddharth Kumar", font="mini", justify="center")
    intro_message = f"\033[91m{intro_message}\033[0m"

    p1 = Popen(["fortune"], stdout=PIPE)
    p2 = Popen(["cowsay", "-f", "dragon"], stdin=p1.stdout, stdout=PIPE)
    p1.stdout.close()
    output = p2.communicate()[0]
    print(output.decode("utf-8"))
    print(intro_message)

# Function to find subdomains
def find_subdomains(domain):
    subdomains = set()
    
    try:
        url = f'https://crt.sh/?q=%.{domain}&output=json'
        response = requests.get(url)
        data = response.json()
        
        # Stage 1: Fetching subdomains from crt.sh
        for entry in data:
            subdomain = entry['name_value']
            subdomains.add(subdomain)
    except Exception as e:
        print(f"Error: {e}")
    
    return subdomains

# Main function
def main():
    try:
        os.system('clear')  # Clear the terminal
        show_intro()
        
        # Input prompts for domain and output file
        domain = input("Enter the domain name without protocol names (http/https): ")
        if not domain:
            print("Please provide a domain name.")
            return
        
        output_file = input("Enter the name of the output file (e.g., subdomain_results.html): ")
        if not output_file:
            print("Please provide an output file name.")
            return
        
        subdomains1 = sublist3r.main(domain, 40, None, None, False, False, False, None)
        subdomains2 = find_subdomains(domain)
        
        subdomains_combined = subdomains1.union(subdomains2)
        
        # Stage 2: Creating a PrettyTable
        table = PrettyTable()
        table.field_names = ["#", "Subdomain"]
        
        # Populate the table with sorted subdomains
        sorted_subdomains = sorted(subdomains_combined)
        for index, subdomain in enumerate(sorted_subdomains, start=1):
            table.add_row([index, subdomain])
        
        # Print the table to the terminal
        print(table)
        
        # Save the table to the output file
        with open(output_file, 'w') as file:
            file.write(table.get_html_string())
        
        # Save the normal output to a backup file
        with open("HackBack", 'w') as backup_file:
            for subdomain in sorted_subdomains:
                backup_file.write(subdomain + "\n")
        
        print(f"Results saved to {output_file}")
        print(f"Normal output saved to HackBack.txt")
    
    except KeyboardInterrupt:
        print("\033[91mGoodbye\033[0m")
        sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_IGN)  # Ignore Ctrl+C during program execution
    main()

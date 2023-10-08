#!/bin/bash

# Update package lists
sudo apt update

# Install Python 3 and pip
sudo apt install -y python3 python3-pip

# Install necessary Python packages
pip3 install sublist3r requests beautifulsoup4 pyfiglet prettytable

# Install fortune and cowsay for the intro message
sudo apt install -y fortune cowsay

# Save the code to a Python file with the name AdvSidlister.py
cat <<EOL > AdvSidlister.py
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

# ... (Copy your Python code here)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_IGN)  # Ignore Ctrl+C during program execution
    main()
EOL

# Make the Python script executable
chmod +x AdvSidlister.py

# Open the "Manual.html" file in the default web browser
xdg-open Manual.html

echo "Setup for AdvSidlister complete. You can run the tool using './AdvSidlister.py'"

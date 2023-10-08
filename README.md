## AvdSidlister ----->

![github-header-image](https://github.com/Siddharth0kumar/AvdSidlister/assets/89460704/d6d0b47b-4329-47c5-90bf-6139a6ae1878)


Certainly, here's a README.md file for "AdvSidlister" tool based on the provided code:

![AvdSidlister](https://github.com/Siddharth0kumar/AvdSidlister/assets/89460704/31137e5e-b2c5-4937-a0a1-f07acdb58b3c)

Certainly, here's the complete README.md file for your "AdvSidlister" tool based on your provided information:

  markdown
# AdvSidlister - Subdomain Finder Tool

AdvSidlister is a Python-based subdomain finder tool created by [siddharth0kumar](https://github.com/siddharth0kumar). It is designed to simplify the process of finding subdomains for a given domain. AdvSidlister combines the capabilities of various libraries and tools to provide you with a comprehensive list of subdomains.

![AdvSidlister](adv-sidlister.png)

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Introduction

AdvSidlister is a tool created by [siddharth0kumar](https://github.com/siddharth0kumar) to streamline the process of subdomain enumeration. It leverages popular subdomain discovery techniques to provide you with a structured list of subdomains for your target domain.

## Features

- **Multi-Source Subdomain Enumeration:** AdvSidlister fetches subdomains from multiple sources, including crt.sh, to ensure comprehensive results.
- **Interactive Table:** It generates an interactive table with subdomain results, making it easy to explore and analyze the data.
- **HTML Export:** AdvSidlister provides an option to save the subdomain results in an HTML file for easy sharing and reference.
- **Backup:** A backup of the subdomain results is created in a text file for additional data security.

## Getting Started

### Prerequisites

Before using AdvSidlister, ensure you have the following prerequisites installed:

- Python 3
- pip (Python package manager)
- fortune and cowsay (optional for the intro message)

You can install these prerequisites on a Debian-based system (like Ubuntu) using the provided setup script.

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/siddharth0kumar/AdvSidlister.git
   ```

2. Change directory to the AdvSidlister folder:

   ```bash
   cd AdvSidlister
   ```

3. Run the setup script to install dependencies and set up the tool:

   ```bash
   bash AvdSidup.sh
   ```

## Usage

To use AdvSidlister to find subdomains for a domain, follow these steps:

1. Open a terminal.

2. Navigate to the AdvSidlister directory:

   ```bash
   cd /path/to/AdvSidlister
   ```

3. Run the tool:

   ```bash
   python3 AvdSidlister.py
   ```

4. Follow the on-screen prompts to enter the domain name and output file name.

## Results

After running AdvSidlister, you will have two output files:

- Your subdomain results in an HTML file (e.g., subdomain_results.html).
- A backup of the results in a text file (HackBack).

You can open the HTML file in a web browser to view the subdomain results in a table format.

## Contributing

If you'd like to contribute to AdvSidlister or report issues, please feel free to create a pull request or issue on the [GitHub repository](https://github.com/siddharth0kumar/AdvSidlister).

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/siddharth0kumar/AdvSidlister/blob/main/LICENSE) file for details.

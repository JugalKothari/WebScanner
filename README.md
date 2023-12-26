# Domain Information Gatherer

This Python project is designed to gather information about a given domain, including its domain name, IP address, Nmap scan results, robots.txt content, and WHOIS information.

## Project Structure

- **domain_name.py:** Obtains the domain name from a given URL using the `tld` library.
- **general.py:** Provides general utility functions such as creating directories and writing files.
- **ip_address.py:** Retrieves the IP address of a domain using the `nslookup` command.
- **main.py:** Orchestrates the information gathering process, prompts the user for input, and creates a report for a specified domain.
- **nmap.py:** Executes an Nmap scan on a given IP address using the `nmap` command-line tool.
- **robots_txt.py:** Fetches the content of the `robots.txt` file for a specified domain.
- **whois.py:** Retrieves WHOIS information for a given domain.

## Getting Started

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo

2. **Install dependencies:**
   ```bash
   pip install tld

3. **Run the Main Script:**
   ```bash
   python main.py

The main.py script prompts the user for the name and URL of the target domain. It then utilizes the other scripts to gather and store relevant information in a dedicated directory within the 'companies' folder.

## Acknowledgments

- **tld:** Python library for parsing and extracting information from domain names.
- **Beautiful Soup:** Library for pulling data out of HTML and XML files.

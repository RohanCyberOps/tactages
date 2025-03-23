import os
import subprocess
import sys
from colorama import Fore, Style

# Function to display a message with color
def print_color(message, color=Fore.WHITE):
    print(color + message + Style.RESET_ALL)

# Function to run shell commands
def run_command(command, description):
    print_color(f"\n{description}...", Fore.YELLOW)
    try:
        subprocess.run(command, check=True, shell=True)
        print_color(f"{description} completed successfully!", Fore.GREEN)
    except subprocess.CalledProcessError as e:
        print_color(f"Error during {description}: {e}", Fore.RED)
        sys.exit(1)

# Function to install tools
def install_tools():
    print_color("Starting tool installation...", Fore.BLUE)

    # Provide manual installation instructions
    print_color("Please install the following tools manually:", Fore.CYAN)
    print("1. Nmap - https://nmap.org/download.html")
    print("2. Metasploit Framework - https://docs.metasploit.com/docs/using-metasploit/getting-started/nightly-installers.html")
    print("3. Wireshark - https://www.wireshark.org/download.html")
    print("4. Hydra - https://github.com/vanhauser-thc/thc-hydra")
    print("5. Tshark (part of Wireshark) - https://www.wireshark.org/download.html")
    print("6. Net-tools - https://sourceforge.net/projects/net-tools/")
    print("7. Netcat - https://eternallybored.org/misc/netcat/")
    print("8. John the Ripper - https://www.openwall.com/john/")
    print("9. SQLMap - https://sqlmap.org/")
    print("10. Nikto - https://cirt.net/Nikto2")
    print("11. Burp Suite - https://portswigger.net/burp/communitydownload")

    print_color("\nAfter installing the tools, ensure they are added to your system's PATH.", Fore.YELLOW)

# Main function
def main():
    print_color("Welcome to the Tactages Toolkit Installer!", Fore.CYAN)
    print_color("This script will guide you to install the following tools:", Fore.CYAN)
    print("1. Nmap - Network Scanning")
    print("2. Metasploit Framework - Exploitation")
    print("3. Wireshark - Traffic Capture")
    print("4. Hydra - Brute Force")
    print("5. Tshark - Packet Capture and Filtering")
    print("6. Net-tools - Network Utilities")
    print("7. Netcat - Network Communication")
    print("8. John the Ripper - Password Cracking")
    print("9. SQLMap - SQL Injection Testing")
    print("10. Nikto - Web Server Scanning")
    print("11. Burp Suite - Web Application Security Testing")

    response = input("\nDo you want to proceed with the installation instructions? (yes/no): ").strip().lower()
    if response == "yes":
        install_tools()
    else:
        print_color("Installation canceled.", Fore.RED)

if __name__ == "__main__":
    main()
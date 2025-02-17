import subprocess
import sys
import os
from datetime import datetime

from colorama import Fore, init, Style

init(autoreset=True)

def print_banner():
    banner = f"""
    {Fore.RED}████████╗ █████╗  ██████╗████████╗ █████╗  ██████╗ ███████╗███████╗
    {Fore.RED}╚══██╔══╝██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔════╝ ██╔════╝██╔════╝
    {Fore.RED}   ██║   ███████║██║        ██║   ███████║██║  ███╗█████╗  ███████╗
    {Fore.RED}   ██║   ██╔══██║██║        ██║   ██╔══██║██║   ██║██╔══╝  ╚════██║
    {Fore.RED}   ██║   ██║  ██║╚██████╗   ██║   ██║  ██║╚██████╔╝███████╗███████║
    {Fore.RED}   ╚═╝   ╚═╝  ╚═════╝   ╚═╝   ╚═╝  ╚═════╝ ╚══════╝╚══════╝
    {Fore.CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    {Fore.YELLOW}  🚀 TACTAGES- The Ultimate Pentesting Interface 🚀
    {Fore.GREEN}  🔹 A Multi-Tool Interface for Ethical Hacking & Cybersecurity 🔹
    {Fore.GREEN}  🔹 Tools: {Fore.RED}Nmap{Fore.GREEN}, {Fore.RED}Metasploit{Fore.GREEN}, {Fore.RED}Wireshark{Fore.GREEN}, {Fore.RED}Hydra{Fore.GREEN}, {Fore.RED}John the Ripper{Fore.GREEN}, etc. 🔹
    {Fore.CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    {Style.RESET_ALL}
    """
    print(banner)

def log_output(tool_name, stdout, stderr):
    if not os.path.exists("log"):
        os.makedirs("log")
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    stdout_filename = f"log/{tool_name}_stdout_{timestamp}.txt"
    stderr_filename = f"log/{tool_name}_stderr_{timestamp}.txt"
    with open(stdout_filename, "w") as stdout_file:
        stdout_file.write(stdout)
    with open(stderr_filename, "w") as stderr_file:
        stderr_file.write(stderr)

def run_nmap():
    target = input(f"{Fore.YELLOW}[?] Enter the target IP or hostname: ")
    command = f"nmap -sV -sC -oA nmap_scan {target}"
    print(f"{Fore.BLUE}[*] Running Nmap scan on {target}...")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(f"{Fore.GREEN}[+] Nmap scan completed!")
    log_output("nmap", result.stdout, result.stderr)

def run_metasploit():
    print(f"{Fore.BLUE}[*] Launching Metasploit Framework...")
    result = subprocess.run("msfconsole", shell=True, capture_output=True, text=True)
    print(f"{Fore.GREEN}[+] Metasploit session ended.")
    log_output("metasploit", result.stdout, result.stderr)

def run_wireshark():
    print(f"{Fore.BLUE}[*] Launching Wireshark...")
    result = subprocess.run("wireshark", shell=True, capture_output=True, text=True)
    print(f"{Fore.GREEN}[+] Wireshark closed.")
    log_output("wireshark", result.stdout, result.stderr)

def run_hydra():
    target = input(f"{Fore.YELLOW}[?] Enter the target IP: ")
    service = input(f"{Fore.YELLOW}[?] Enter the service to attack (e.g., ssh, ftp): ")
    userlist = input(f"{Fore.YELLOW}[?] Enter the path to the username list: ")
    passlist = input(f"{Fore.YELLOW}[?] Enter the path to the password list: ")
    command = f"hydra -L {userlist} -P {passlist} {target} {service}"
    print(f"{Fore.BLUE}[*] Running Hydra on {target}...")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(f"{Fore.GREEN}[+] Hydra attack completed!")
    log_output("hydra", result.stdout, result.stderr)

def run_sqlmap():
    target = input(f"{Fore.YELLOW}[?] Enter the target URL: ")
    command = f"sqlmap -u {target} --batch"
    print(f"{Fore.BLUE}[*] Running sqlmap on {target}...")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(f"{Fore.GREEN}[+] SQLMap scan completed!")
    log_output("sqlmap", result.stdout, result.stderr)

def main_menu():
    print_banner()
    try:
        while True:
            print(f"\n{Fore.CYAN}Main Menu:")
            print(f"{Fore.YELLOW}1. Run Nmap Scan")
            print(f"{Fore.YELLOW}2. Launch Metasploit Framework")
            print(f"{Fore.YELLOW}3. Launch Wireshark")
            print(f"{Fore.YELLOW}4. Run Hydra Attack")
            print(f"{Fore.YELLOW}5. Run SQLMap Scan")
            print(f"{Fore.YELLOW}6. Exit")
            choice = input(f"{Fore.YELLOW}[?] Select an option: ")

            if choice == "1":
                run_nmap()
            elif choice == "2":
                run_metasploit()
            elif choice == "3":
                run_wireshark()
            elif choice == "4":
                run_hydra()
            elif choice == "5":
                run_sqlmap()
            elif choice == "6":
                print(f"{Fore.RED}[*] Exiting Terminal . Goodbye!")
                sys.exit(0)
            else:
                print(f"{Fore.RED}[!] Invalid option. Please try again.")
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[*] Exiting Terminal  Goodbye!")
        sys.exit(0)

if __name__ == "__main__":
    main_menu()
import subprocess
import sys

from colorama import Fore, init, Style

init(autoreset=True)


init(autoreset=True)
def print_banner():
    banner = f"""
    {Fore.RED}████████╗ █████╗  ██████╗████████╗ █████╗  ██████╗ ███████╗███████╗
    {Fore.RED}╚══██╔══╝██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔════╝ ██╔════╝██╔════╝
    {Fore.RED}   ██║   ███████║██║        ██║   ███████║██║  ███╗█████╗  ███████╗
    {Fore.RED}   ██║   ██╔══██║██║        ██║   ██╔══██║██║   ██║██╔══╝  ╚════██║
    {Fore.RED}   ██║   ██║  ██║╚██████╗   ██║   ██║  ██║╚██████╔╝███████╗███████║
    {Fore.RED}   ╚═╝   ╚═╝  ╚═╝ ╚═════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝
    {Fore.CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    {Fore.YELLOW}  🚀 Terminal TacticalZero - The Ultimate Pentesting Interface 🚀
    {Fore.CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    {Fore.GREEN}  🔹 A Multi-Tool Interface for Ethical Hacking & Cybersecurity 🔹
    {Fore.GREEN}  🔹 Tools: {Fore.RED}Nmap{Fore.GREEN}, {Fore.RED}Metasploit{Fore.GREEN}, {Fore.RED}Wireshark{Fore.GREEN}, {Fore.RED}Hydra{Fore.GREEN}, {Fore.RED}John the Ripper{Fore.GREEN}, etc. 🔹
    {Fore.CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    {Style.RESET_ALL}
    """
    print(banner)

def run_nmap():
    target = input(f"{Fore.YELLOW}[?] Enter the target IP or hostname: ")
    command = f"nmap -sV -sC -oA nmap_scan {target}"
    print(f"{Fore.BLUE}[*] Running Nmap scan on {target}...")
    subprocess.run(command, shell=True)
    print(f"{Fore.GREEN}[+] Nmap scan completed!")

def run_metasploit():
    print(f"{Fore.BLUE}[*] Launching Metasploit Framework...")
    subprocess.run("msfconsole", shell=True)
    print(f"{Fore.GREEN}[+] Metasploit session ended.")

def run_wireshark():
    print(f"{Fore.BLUE}[*] Launching Wireshark...")
    subprocess.run("wireshark", shell=True)
    print(f"{Fore.GREEN}[+] Wireshark closed.")

def run_hydra():
    target = input(f"{Fore.YELLOW}[?] Enter the target IP: ")
    service = input(f"{Fore.YELLOW}[?] Enter the service to attack (e.g., ssh, ftp): ")
    userlist = input(f"{Fore.YELLOW}[?] Enter the path to the username list: ")
    passlist = input(f"{Fore.YELLOW}[?] Enter the path to the password list: ")
    command = f"hydra -L {userlist} -P {passlist} {target} {service}"
    print(f"{Fore.BLUE}[*] Running Hydra on {target}...")
    subprocess.run(command, shell=True)
    print(f"{Fore.GREEN}[+] Hydra attack completed!")

def main_menu():
    print_banner()
    while True:
        print(f"\n{Fore.CYAN}Main Menu:")
        print(f"{Fore.YELLOW}1. Run Nmap Scan")
        print(f"{Fore.YELLOW}2. Launch Metasploit Framework")
        print(f"{Fore.YELLOW}3. Launch Wireshark")
        print(f"{Fore.YELLOW}4. Run Hydra Attack")
        print(f"{Fore.YELLOW}5. Exit")
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
            print(f"{Fore.RED}[*] Exiting Terminal TacticalZero. Goodbye!")
            sys.exit()
        else:
            print(f"{Fore.RED}[!] Invalid option. Please try again.")

if __name__ == "__main__":
    main_menu()
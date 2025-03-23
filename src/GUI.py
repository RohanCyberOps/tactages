import tkinter as tk
from tkinter import messagebox, simpledialog
import subprocess
import os

class TactagesToolkitGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tactages Toolkit")
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Select a tool to use:").pack(pady=10)

        tools = [
            ("Nmap - Network Scanning", self.run_nmap),
            ("Metasploit - Exploitation", self.run_metasploit),
            ("Wireshark - Traffic Capture", self.run_wireshark),
            ("Hydra - Brute Force", self.run_hydra),
            ("Tshark - Packet Capture and Filtering", self.run_tshark),
            ("Netcat - Network Communication", self.run_netcat),
            ("John the Ripper - Password Cracking", self.run_john),
            ("SQLMap - SQL Injection Testing", self.run_sqlmap),
            ("Nikto - Web Server Scanning", self.run_nikto),
            ("Burp Suite - Web Application Security Testing", self.run_burpsuite)
        ]

        for tool, command in tools:
            tk.Button(self.root, text=tool, command=command).pack(fill=tk.X, padx=20, pady=5)

        tk.Button(self.root, text="Exit", command=self.root.quit).pack(pady=10)

    def run_command(self, command):
        try:
            subprocess.run(command, check=True, shell=True)
            messagebox.showinfo("Success", f"{command} completed successfully!")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Error during {command}: {e}")

    def run_nmap(self):
        target = self.get_input("Enter the target IP or range (e.g., 192.168.1.1 or 192.168.1.0/24):")
        if target:
            self.run_command(f"nmap {target}")

    def run_metasploit(self):
        self.run_command("msfconsole")

    def run_wireshark(self):
        self.run_command("wireshark")

    def run_hydra(self):
        target = self.get_input("Enter the target IP or hostname:")
        service = self.get_input("Enter the service to attack (e.g., ssh, ftp):")
        username = self.get_input("Enter the username:")
        wordlist = self.get_input("Enter the path to the wordlist file:")
        if target and service and username and wordlist:
            self.run_command(f"hydra -l {username} -P {wordlist} {target} {service}")

    def run_tshark(self):
        self.run_command("tshark")

    def run_netcat(self):
        target = self.get_input("Enter the target IP or hostname:")
        port = self.get_input("Enter the port number:")
        if target and port:
            self.run_command(f"nc {target} {port}")

    def run_john(self):
        password_file = self.get_input("Enter the path to the password file:")
        if password_file:
            self.run_command(f"john {password_file}")

    def run_sqlmap(self):
        url = self.get_input("Enter the URL to test for SQL injection:")
        if url:
            self.run_command(f"sqlmap -u {url}")

    def run_nikto(self):
        target = self.get_input("Enter the target URL:")
        if target:
            self.run_command(f"nikto -host {target}")

    def run_burpsuite(self):
        self.run_command("burpsuite")

    def get_input(self, prompt):
        return simpledialog.askstring("Input", prompt)

if __name__ == "__main__":
    root = tk.Tk()
    app = TactagesToolkitGUI(root)
    root.mainloop()
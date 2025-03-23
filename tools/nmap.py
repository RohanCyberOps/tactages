import subprocess

def scan_network(target):
    """
    Perform an Nmap scan on the target network.
    """
    command = f"nmap -sP {target}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout

if __name__ == "__main__":
    target = input("Enter the target IP or range (e.g., 192.168.1.1 or 192.168.1.0/24): ")
    print("\nScanning network...")
    result = scan_network(target)
    print(result)
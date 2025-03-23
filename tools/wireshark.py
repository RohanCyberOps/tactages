import subprocess

def capture_traffic(interface="eth0", duration=10):
    """
    Capture network traffic using Wireshark.
    """
    command = f"tshark -i {interface} -a duration:{duration}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout

if __name__ == "__main__":
    interface = input("Enter the network interface (e.g., eth0): ")
    duration = input("Enter the capture duration in seconds (e.g., 10): ")
    print("\nCapturing traffic...")
    result = capture_traffic(interface, int(duration))
    print(result)
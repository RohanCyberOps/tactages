import subprocess
import os

def capture_packets(interface="eth0", count=10, output_file=None):
    """
    Capture a specified number of packets from the network interface.
    Optionally save the output to a file.
    """
    try:
        # Check if tcpdump is installed
        if not os.path.exists("/usr/sbin/tcpdump"):
            return "Error: tcpdump is not installed. Please install it first."

        # Build the command
        command = f"tcpdump -i {interface} -c {count}"
        if output_file:
            command += f" -w {output_file}"

        print(f"Starting packet capture on interface {interface}...")
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        if result.returncode != 0:
            return f"Error: {result.stderr}"

        if output_file:
            return f"Packet capture complete. Saved to {output_file}."
        else:
            return result.stdout

    except Exception as e:
        return f"Error capturing packets: {e}"
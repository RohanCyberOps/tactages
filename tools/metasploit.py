import subprocess

def exploit(target, payload, lhost=None, lport=None):
    """
    Execute a Metasploit exploit with custom options.
    """
    try:
        # Validate payload format
        if not payload.startswith("exploit/"):
            return "Error: Payload must start with 'exploit/'."

        # Build the msfconsole command
        command = f"msfconsole -q -x 'use {payload}; set RHOSTS {target};"
        if lhost:
            command += f" set LHOST {lhost};"
        if lport:
            command += f" set LPORT {lport};"
        command += " run'"

        print(f"Executing Metasploit exploit on {target} with payload {payload}...")
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        if result.returncode != 0:
            return f"Exploit failed: {result.stderr}"
        return result.stdout

    except Exception as e:
        return f"Error executing Metasploit: {e}"
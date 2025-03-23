import subprocess

def run_netcat(target, port):
    try:
        result = subprocess.run(['nc', '-zv', target, port], capture_output=True, text=True)
        return result.stdout if result.returncode == 0 else result.stderr
    except Exception as e:
        return str(e)
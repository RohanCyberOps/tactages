import subprocess

def run_john(password_file):
    try:
        result = subprocess.run(['john', password_file], capture_output=True, text=True)
        return result.stdout if result.returncode == 0 else result.stderr
    except Exception as e:
        return str(e)
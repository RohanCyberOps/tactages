import subprocess

def run_burpsuite():
    try:
        subprocess.run("burpsuite", check=True, shell=True)
        print("Burp Suite launched successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error launching Burp Suite: {e}")

if __name__ == "__main__":
    run_burpsuite()
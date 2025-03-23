import subprocess

def run_nikto(target):
    try:
        subprocess.run(f"nikto -host {target}", check=True, shell=True)
        print("Nikto scan completed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error during Nikto scan: {e}")

if __name__ == "__main__":
    target = input("Enter the target URL: ")
    run_nikto(target)
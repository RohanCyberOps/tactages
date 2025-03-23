import subprocess

def run_sqlmap(url):
    try:
        subprocess.run(f"sqlmap -u {url}", check=True, shell=True)
        print("SQLMap scan completed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error during SQLMap scan: {e}")

if __name__ == "__main__":
    url = input("Enter the URL to test for SQL injection: ")
    run_sqlmap(url)
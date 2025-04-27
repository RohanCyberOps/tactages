import time
import sys
import os
import threading
import itertools
import logging
from colorama import Fore, Style

# Create logs directory if it doesn't exist
log_directory = 'logs'
os.makedirs(log_directory, exist_ok=True)

# Set log file path
log_file = os.path.join(log_directory, 'application.log')

# Configure logging to both file and console
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(name)s - %(funcName)s:%(lineno)d - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)

# Example logging
logging.info('Logger initialized successfully.')

# Function for implementing the loading animation
def load_animation():
    # String to be displayed when the application is loading
    load_str = "starting your console application..."
    ls_len = len(load_str)

    # String for creating the rotating line
    animation = "|/-\\"
    anicount = 0

    # used to keep the track of
    # the duration of animation
    counttime = 0

    # pointer for travelling the loading string
    i = 0

    while (counttime != 100):

        # used to change the animation speed
        # smaller the value, faster will be the animation
        time.sleep(0.075)

        # converting the string to list
        # as string is immutable
        load_str_list = list(load_str)

        # x->obtaining the ASCII code
        x = ord(load_str_list[i])

        # y->for storing altered ASCII code
        y = 0

        # if the character is "." or " ", keep it unaltered
        # switch uppercase to lowercase and vice-versa
        if x != 32 and x != 46:
            if x > 90:
                y = x - 32
            else:
                y = x + 32
            load_str_list[i] = chr(y)

        # for storing the resultant string
        res = ''
        for j in range(ls_len):
            res = res + load_str_list[j]

        # displaying the resultant string
        sys.stdout.write("\r" + res + animation[anicount])
        sys.stdout.flush()

        # Assigning loading string
        # to the resultant string
        load_str = res

        anicount = (anicount + 1) % 4
        i = (i + 1) % ls_len
        counttime = counttime + 1

    # for windows OS
    if os.name == "nt":
        os.system("cls")

    # for linux / Mac OS
    else:
        os.system("clear")

class Spinner:
    def __init__(self):
        self.spinner = itertools.cycle(["⣾", "⣽", "⣻", "⢿", "⡿", "⣟", "⣯", "⣷"])
        self.running = False
        self.spinner_thread = None

    def spin(self):
        while self.running:
            sys.stdout.write(Fore.GREEN + next(self.spinner) + Style.RESET_ALL)  # Write the next spinner character
            sys.stdout.flush()
            time.sleep(0.1)
            sys.stdout.write("\b")  # Move the cursor back

    def start(self):
        self.running = True
        self.spinner_thread = threading.Thread(target=self.spin)
        self.spinner_thread.start()

    def stop(self):
        self.running = False
        if self.spinner_thread:
            self.spinner_thread.join()
        sys.stdout.write("\b \b")  # Clear the spinner
        sys.stdout.flush()

def progress_bar(duration):
    """Display a progress bar for a given duration."""
    for i in range(duration):
        percent = (i + 1) / duration * 100
        bar = "[" + "=" * int(percent // 2) + " " * (50 - int(percent // 2)) + "]"
        print(f"\r{bar} {percent:.1f}%", end="")
        time.sleep(1)
    print()

def typewriter(text, delay=0.05):
    """Display text with a typewriter effect."""
    for char in text:
        print(Fore.BLUE + char + Style.RESET_ALL, end="", flush=True)
        time.sleep(delay)
    print()

def countdown(seconds):
    """Display a countdown timer."""
    for i in range(seconds, 0, -1):
        print(f"\rStarting in {Fore.RED}{i}{Style.RESET_ALL}...", end="")
        time.sleep(1)
    print("\rStarting now!   ")

def main():
    # Display loading animation at the start
    load_animation()

    typewriter("Welcome to Tactages Toolkit!", delay=0.05)
    print("""
        ⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⣄⡖⠶⠰⠛⠛⠛⠛⠛⠓⠖⠖⢦⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠲⠛⠉⣁⣀⡀⠀⢰⠂⠁⠀⢸⠎⣲⠀⠀⣀⣀⣈⠉⠻⠦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠮⠋⠀⢰⠀⠈⢧⠼⢥⠀⠸⡏⢁⠀⣸⠹⣆⠀⢰⠃⠀⠀⡷⠀⠀⡈⠙⢖⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⠚⠢⣼⠀⠀⠨⠧⠚⢀⢀⣉⢥⢤⢬⢤⣈⣀⠈⠣⠤⠴⠋⠀⣴⢋⣱⠀⠈⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⣠⡺⠁⡰⠊⠀⠀⠀⠀⠓⣀⡤⡲⡫⡪⡣⡣⡣⡣⡣⡣⡪⡪⡹⡱⡲⣄⡀⠚⠀⠉⠁⢠⡔⢄⠈⢷⢄⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⣰⠎⠀⠀⠹⣄⣀⡠⠃⣠⢞⢪⢜⢜⢌⢎⡎⣪⡼⣬⢮⣎⣆⢇⡣⡣⡣⡱⣙⢳⢄⠀⢆⢨⡇⠈⠀⠀⠹⣢⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⣼⠊⠀⠀⠀⠀⠀⠈⣠⢞⢕⢕⠕⡕⢜⢜⣵⣫⢻⣽⣯⣿⣳⢟⢝⣽⢎⠎⡎⡪⡪⡪⡳⣄⠁⠀⠀⠀⠀⠀⠸⣦⠀⠀⠀⠀
    ⠀⠀⠀⡰⠇⠀⠀⠀⠀⠀⠀⣴⣫⣳⣵⢥⣣⢭⡸⣐⣿⡽⣳⢽⡾⣻⣟⣞⡯⣿⡇⡇⣇⡵⡵⣕⣿⣵⡦⠀⠀⠀⠀⠀⠀⠸⡆⠀⠀⠀
    ⠀⠀⢠⡻⠀⡀⣜⣀⣀⠀⣸⡿⣽⣯⣿⣿⣽⣻⣿⢾⢿⡱⣝⣵⣿⢾⣳⢵⡹⡽⣿⣻⣯⣿⣟⣿⣿⣽⣿⣅⠀⣀⡠⡆⡀⡀⢿⡀⠀⠀
    ⠀⠀⢘⠅⠀⢘⠕⢪⠀⢐⣿⣻⣿⣽⣿⢾⣿⣻⣾⡻⣕⡝⡖⣟⣞⣯⢿⡕⡽⣸⢝⣿⣟⣯⢿⣻⣾⣟⣾⣷⡁⠀⡖⠭⡅⠀⠨⡃⠀⠀
    ⠀⠀⣿⠀⠀⠀⠀⠀⠀⣼⢿⣟⣿⣽⣾⣿⣿⣻⢯⡺⣪⢞⢽⣿⣳⣯⣿⡯⣫⢮⡳⣝⢿⣽⣿⣟⣿⣟⣯⣿⣣⠀⠀⠀⠀⠀⠈⣿⠀⠀
    ⠀⠀⣿⠀⠀⠀⠀⠀⠀⣿⢿⣿⣿⢿⣿⣽⡿⣕⢗⢧⡳⣝⢽⣿⣻⣾⣿⣽⣪⡳⣕⢗⣝⢿⣟⣯⣷⣿⢿⣿⣳⠀⠀⠀⠀⠀⠀⣿⠀⠀
    ⠀⠀⢿⠀⠀⠀⠀⠀⠀⢫⢭⢹⢑⢻⢑⢍⢪⠸⡘⡔⡜⡮⣻⣟⣿⣯⣷⣿⢲⡱⡘⡌⡆⡣⡙⡍⡝⡜⡝⡜⡕⠀⠀⠀⠀⠀⠀⡿⠀⠀
    ⠀⠀⢸⡅⠀⢂⠞⠁⠀⠘⣎⢎⢎⡪⢪⢨⠪⡘⡌⡆⡣⡫⣟⣿⣾⢷⣟⣿⡕⡜⢌⢪⠢⡑⠥⡱⢸⢸⢸⢸⠅⠀⡖⠤⢄⠀⢨⡇⠀⠀
    ⠀⠀⠘⣖⠀⠠⠍⢓⡀⠀⢳⡱⡱⡘⡌⢆⠕⢜⢌⠪⡢⢝⣿⣻⣽⣿⢿⣿⣝⢌⢎⠢⡣⠱⡑⡅⡣⡱⣸⡊⠀⢐⠀⠀⡀⠀⣞⠀⠀⠀
    ⠀⠀⠀⠸⡆⠀⢜⠁⢈⠄⠀⠳⡱⡨⢪⢘⢌⠪⡂⡇⣎⢟⡷⣿⢿⣿⣻⢷⣗⢵⢸⠨⣊⢪⢘⢌⢪⢸⠎⠀⢠⢈⠒⠒⠀⡰⠇⠀⠀⠀
    ⠀⠀⠀⠀⠻⡆⠀⠘⢈⢤⠂⠀⠙⢮⢪⠸⣐⢕⣕⢧⡳⣻⣟⣾⢿⡷⣿⣻⢷⣝⢎⢯⡢⡕⢅⢣⠵⠋⠀⡠⠉⠒⠔⠀⡰⡛⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠹⣆⠈⠁⡜⠔⢀⠄⠀⠙⢮⡢⡣⡒⡕⡍⢮⠸⡣⡹⡩⡪⡓⣝⢪⠹⡰⡘⣜⠼⠃⠀⡠⢨⡈⠓⠄⠀⣰⠏⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠘⢵⡀⠀⠔⠁⢨⠒⠄⠀⠈⠓⠎⢦⣃⡇⡇⡇⡇⡣⡣⡣⣪⡢⡣⠧⠋⠁⢀⣀⠸⣀⢀⠁⠀⢠⠮⠃⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⡀⠀⠁⢠⠋⠈⡢⢀⣀⠀⠀⠉⠉⠚⠙⠓⠓⠉⠁⠈⠀⠀⡄⢢⠑⢖⠤⠄⠁⣀⡶⠋⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢗⣄⡀⠑⠒⠁⡞⡖⠁⠀⢀⢲⠀⠤⡀⠠⠰⡀⠑⡄⠀⠈⡅⠀⠈⢀⣠⠞⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠚⠵⣦⣀⡀⠀⠀⠀⠂⠉⠆⠸⠈⠒⠀⠇⠒⠀⠀⢀⡠⡴⠎⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠳⠖⠦⢦⣤⣤⣤⣤⡴⠔⠶⠺⠙⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

         """)

    while True:
        print("\nSelect a tool to use:")
        print("1. Nmap - Network Scanning")
        print("2. Metasploit - Exploitation")
        print("3. Wireshark - Traffic Capture")
        print("4. Hydra - Brute Force")
        print("5. Utils - Packet Capture and Filtering")
        print("6. John the Ripper - Password Cracking")
        print("7. Netcat - Network Communication")
        print("8. SQLMap - SQL Injection Testing")
        print("9. Nikto - Web Server Scanning")
        print("10. Burp Suite - Web Application Security Testing")
        print("11. Exit")

        choice = input("Enter your choice (1-11): ")

        if choice == "1":
            target = input("Enter the target IP or range (e.g., 192.168.1.1 or 192.168.1.0/24): ")
            print("\nScanning network...")
            spinner = Spinner()
            spinner.start()
            # Simulate a long-running task
            time.sleep(5)
            spinner.stop()
            print("Scan complete!")

        elif choice == "2":
            target = input("Enter the target IP or hostname: ")
            payload = input("Enter the payload (e.g., windows/meterpreter/reverse_tcp): ")
            print("\nRunning exploit...")
            progress_bar(10)  # Simulate a 10-second exploit
            print("Exploit complete!")

        elif choice == "3":
            interface = input("Enter the network interface (e.g., eth0): ")
            duration = int(input("Enter the capture duration in seconds (e.g., 10): "))
            print("\nCapturing traffic...")
            countdown(5)  # 5-second countdown
            print("Traffic capture complete!")

        elif choice == "4":
            target = input("Enter the target IP or hostname: ")
            service = input("Enter the service to attack (e.g., ssh, ftp): ")
            username = input("Enter the username: ")
            wordlist = input("Enter the path to the wordlist file: ")
            print("\nRunning brute force attack...")
            spinner = Spinner()
            spinner.start()
            # Simulate a long-running task
            time.sleep(5)
            spinner.stop()
            print("Brute force attack complete!")

        elif choice == "5":
            print("\nUtils - Packet Capture and Filtering")
            interface = input("Enter the network interface (e.g., eth0): ")
            count = int(input("Enter the number of packets to capture (e.g., 10): "))
            print("\nCapturing packets...")
            progress_bar(10)  # Simulate a 10-second capture
            print("Packet capture complete!")

        elif choice == "6":
            password_file = input("Enter the path to the password file: ")
            print("\nRunning John the Ripper...")
            spinner = Spinner()
            spinner.start()
            # Simulate a long-running task
            time.sleep(5)
            spinner.stop()
            print("Password cracking complete!")

        elif choice == "7":
            target = input("Enter the target IP or hostname: ")
            port = input("Enter the port number: ")
            print("\nRunning Netcat...")
            spinner = Spinner()
            spinner.start()
            # Simulate a long-running task
            time.sleep(5)
            spinner.stop()
            print("Netcat operation complete!")

        elif choice == "8":
            url = input("Enter the URL to test for SQL injection: ")
            print("\nRunning SQLMap...")
            spinner = Spinner()
            spinner.start()
            # Simulate a long-running task
            time.sleep(5)
            spinner.stop()
            print("SQL injection testing complete!")

        elif choice == "9":
            target = input("Enter the target URL: ")
            print("\nRunning Nikto...")
            spinner = Spinner()
            spinner.start()
            # Simulate a long-running task
            time.sleep(5)
            spinner.stop()
            print("Web server scanning complete!")

        elif choice == "10":
            print("\nLaunching Burp Suite...")
            spinner = Spinner()
            spinner.start()
            # Simulate launching Burp Suite
            os.system("burpsuite")  # Ensure 'burpsuite' is in your PATH or provide the full path
            spinner.stop()
            print("Burp Suite launched!")

        elif choice == "11":
            typewriter("Exiting Tactages Toolkit. Goodbye!", delay=0.05)
            break

        else:
            print(Fore.RED + "Invalid choice. Please select a valid option." + Style.RESET_ALL)


if __name__ == "__main__":
    main()
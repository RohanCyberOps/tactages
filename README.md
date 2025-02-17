![TACTAGES](image.png)

# 🚀 TACTAGES: TacticalZero Multi-Tool Interface

[![GitHub Stars](https://img.shields.io/github/stars/RohanCyberOps/tactages?style=for-the-badge)](https://github.com/RohanCyberOps/tactages/stargazers) [![GitHub Forks](https://img.shields.io/github/forks/RohanCyberOps/tactages?style=for-the-badge)](https://github.com/RohanCyberOps/tactages/network/members) [![GitHub License](https://img.shields.io/github/license/RohanCyberOps/tactages?style=for-the-badge)](LICENSE)

**TACTAGES** is a powerful, terminal-based multi-tool interface designed for ethical hacking, penetration testing, and cybersecurity analysis. It seamlessly integrates essential cybersecurity tools like **Nmap**, **Metasploit Framework**, **Wireshark**, **Hydra**, and more into a streamlined, user-friendly interface. Whether you're a professional security analyst or an enthusiast, TACTAGES enhances your workflow and efficiency.

---

## ✨ Features

✅ **All-in-One Interface** – Access multiple security tools from a single dashboard.  
✅ **User-Friendly Navigation** – Simplified terminal menu for effortless use.  
✅ **Highly Customizable** – Add or remove tools based on your specific needs.  
✅ **Cross-Platform Support** – Runs on Windows, Linux, and macOS (dependencies required).  
✅ **Enhanced Terminal Output** – Includes colored text, banners, and improved readability.  

---

## 🛠️ Tools Included

| Tool                 | Functionality                                  |
|----------------------|----------------------------------------------|
| **Nmap**            | Network scanning and reconnaissance          |
| **Metasploit**      | Exploitation and post-exploitation tasks     |
| **Wireshark**       | Packet capture and network analysis         |
| **Hydra**           | Brute-force and password cracking attacks   |
| **John the Ripper** | Password cracking (coming soon)             |
| **Extendable**      | Easily add more tools as needed             |

---

## ⚡ Installation

### Prerequisites
- Python 3.x
- Required tools installed on your system:
  - Nmap
  - Metasploit Framework
  - Wireshark
  - Hydra

### Installation Steps
```bash
# Clone the repository
git clone https://github.com/RohanCyberOps/tactages.git
cd tactages

# Install dependencies
pip install colorama

# Run the tool
python tz.py
```

---

## 🖥️ Usage

### Launch TACTAGES
```bash
python tz.py
```

### Main Menu
```bash
████████╗ █████╗  ██████╗████████╗ █████╗  ██████╗ ███████╗███████╗
╚══██╔══╝██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔════╝ ██╔════╝██╔════╝
   ██║   ███████║██║        ██║   ███████║██║  ███╗█████╗  ███████╗
   ██║   ██╔══██║██║        ██║   ██╔══██║██║   ██║██╔══╝  ╚════██║
   ██║   ██║  ██║╚██████╗   ██║   ██║  ██║╚██████╔╝███████╗███████║
   ╚═╝   ╚═╝  ╚═╝ ╚═════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  🚀 TACTAGES - The Ultimate Pentesting Interface 🚀 @TacticalZero
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  🔹 A Multi-Tool Interface for Ethical Hacking & Cybersecurity 🔹
  🔹 Tools: Nmap, Metasploit, Wireshark, Hydra, John the Ripper, etc. 🔹
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Main Menu:
1. Run Nmap Scan
2. Launch Metasploit Framework
3. Launch Wireshark
4. Run Hydra Attack
5. Exit
[?] Select an option:
```

---

## 🔧 Adding New Tools

Want to add a new tool? Follow these steps:
1. Create a new function in `tz.py` (e.g., `run_sqlmap()`).
2. Add the tool to the main menu.
3. Implement logic to call the function when selected.

### Example: Adding SQLMap
```python
import subprocess
from colorama import Fore

def run_sqlmap():
    target = input(f"{Fore.YELLOW}[?] Enter the target URL: ")
    command = f"sqlmap -u {target} --batch"
    print(f"{Fore.BLUE}[*] Running sqlmap on {target}...")
    subprocess.run(command, shell=True)
    print(f"{Fore.GREEN}[+] SQLMap scan completed!")
```

Now, update the menu:
```python
print(f"{Fore.YELLOW}6. Run SQLMap Scan")
elif choice == "6":
    run_sqlmap()
```

---

## 🤝 Contributing

Contributions are welcome! If you'd like to enhance TACTAGES, follow these steps:
1. **Fork the repository**.
2. **Create a feature branch** (`git checkout -b feature/YourFeatureName`).
3. **Commit your changes** (`git commit -m 'Add new feature'`).
4. **Push to your branch** (`git push origin feature/YourFeatureName`).
5. **Submit a pull request**.

---

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## ⚠️ Disclaimer

This tool is strictly for **ethical hacking** and **educational purposes**. Misuse for unauthorized activities is prohibited, and the developers hold no responsibility for any misuse.

---

## 💬 Support

For issues, suggestions, or feedback, open an issue on the [GitHub repository](https://github.com/RohanCyberOps/tactages/issues).

---

### **Happy Hacking!** 🚀


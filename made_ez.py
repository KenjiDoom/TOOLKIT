# This script will automate begging tasks for a ctf
import subprocess
import os
# 45.33.32.156
# Test IP, Permission given by nmap



def main():
    IP = input("Enter IP: ")
    subprocess.run(["nmap", "-A", "-sC", "-sV", "-oN", "nmap_scan_results.txt", IP])
    subprocess.run(["nikto", "-o", "nikto_scan_resutls.txt", "-h", IP])





if __name__ == "__main__":
    main()

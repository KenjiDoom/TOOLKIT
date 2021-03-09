# This script will automate begging tasks for a ctf
import subprocess
import os
# 45.33.32.156
# Test IP, Permission given by nmap

def brute():
    pass



def enum():
    IP = input("Enter IP: ")
    subprocess.run(["nmap", "-A", "-sC", "-sV", "-oN", "nmap_scan_results.txt", IP])
    subprocess.run(["nikto", "-o", "nikto_scan_resutls.txt", "-h", IP])
    subprocess.run(["enum4linux", "-a", IP])



if __name__ == "__main__":
    enum()

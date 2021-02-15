# This script will automate begging tasks for a ctf
import subprocess
import os

def main():
    IP = input("Enter IP: ")
    print ("Scanning on " + IP) 
    #subprocess.run(["nmap", "-A" + IP])
    os.system(f"nmap -A {IP}")






if __name__ == "__main__":
    main()

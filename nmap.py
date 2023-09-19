import os

def nmapFunc():
    nmap = input("Subnet (CIDR) or IP: ")
    nmapComm = os.system("nmap -sC -A -Pn "+ nmap)
    print(nmapComm)
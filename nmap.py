import os

def nmapFunc():
    
    logo = """

 _ __  _ __ ___   __ _ _ __  
| '_ \| '_ ` _ \ / _` | '_ \ 
| | | | | | | | | (_| | |_) |
|_| |_|_| |_| |_|\__,_| .__/ 
                      |_|    
                                          
"""

    print(logo + "\n")

    nmap = input("Subnet (CIDR) or IP: ")
    
    if nmap == "0":
        input("\n Press any key to exit...")

    else:
        nmapComm = os.system("nmap -sC -A -Pn "+ nmap)
        print(nmapComm)

        input("\n Press any key to exit...")
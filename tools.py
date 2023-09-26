import ipinfo
import webbrowser
from cryptography.fernet import Fernet
import random
import string
import os

clear = lambda: os.system('cls')

try:

    def ipTrackerFunc():

        logo = """

     ___ ____ _____ ____      _    ____ _  _______ ____  
    |_ _|  _ \_   _|  _ \    / \  / ___| |/ / ____|  _ \ 
     | || |_) || | | |_) |  / _ \| |   | ' /|  _| | |_) |
     | ||  __/ | | |  _ <  / ___ \ |___| . \| |___|  _ < 
    |___|_|    |_| |_| \_\/_/   \_\____|_|\_\_____|_| \_\


        """    

        print(logo)    

        token = "TOKEN HERE"   # Token can be found at https://ipinfo.io/ after signing in.

        access_token = token
        handler = ipinfo.getHandler(access_token)

        ip_address = input(" Enter an IP address: ")

        details = handler.getDetails(ip_address)

        print("\n Location of IP address {}:".format(ip_address))
        print(" Hostname: {}".format(details.hostname))
        print(" City: {}".format(details.city))
        print(" Region: {}".format(details.region))
        print(" Postal: {}".format(details.postal))
        print(" Country: {}".format(details.country_name))
        print(" Latitude: {}".format(details.latitude))
        print(" Longitude: {}".format(details.longitude))
        print(" ISP: {}".format(details.org))
        print(" Timezone: {}".format(details.timezone))
        
        info = input("\n Do you want to see more info? (Y/N): ")

        if info == "N" or info == "n":
            input("\n Press any key to exit...")
        else:
            webbrowser.open("https://www.shodan.io/host/" + ip_address)
            input("\n Press any key to exit...")

    def ipInfoFunc():

        logo = """

     ___ ____ ___ _   _ _____ ___  
    |_ _|  _ \_ _| \ | |  ___/ _ \ 
     | || |_) | ||  \| | |_ | | | |
     | ||  __/| || |\  |  _|| |_| |
    |___|_|  |___|_| \_|_|   \___/ 

        """ 

        print(logo)

        option = 1

        while option != 0:

            def menuIP():
                print(" [1] IPCONFIG")
                print(" [2] DHCP RENEW")
                print(" [3] NETSTAT")
                print(" [4] TRACERT")
                print(" [0] Exit")

            print()
            menuIP()

            option = int(input("\n Choose option: "))

            if option == 1:
                os.system("ipconfig/all")

            elif option == 2:
                os.system("ipconfig/release")
                os.system("ipconfig/renew")

            elif option == 3:
                os.system("netstat -a")

            elif option == 4:
                tracertComm = input("\n IP address: ")
                os.system("tracert " + tracertComm)

    def passGenFunc():
        option = 1

        while option != 0:
        
            logo = """

     _____         _____ _____  _____ ______ _   _
    |  __ \ /\    / ____/ ____|/ ____|  ____| \ | |
    | |__) /  \  | (___| (___ | |  __| |__  |  \| |
    |  ___/ /\ \  \___ \\___  \| | |_ |  __| | . ` |
    | |  / ____ \ ____) |___) | |__| | |____| |\  |
    |_| /_/    \_\_____/_____/ \_____|______|_| \_|

              """

            print(logo)
            def menu():
            
                print(" [1] Password")
                print(" [2] Encryption")
                print(" [0] Exit")

            print()
            menu()

            option = int(input("\n Choose option: "))

            if option == 1:
            
                def menu():
                
                    print(" [1] Generate password")
                    print(" [2] Read passList")
                    print(" [3] Delete passList")
                    print(" [0] Exit")

                print()
                menu()

                option = int(input("\n Choose option: "))

                if option == 1:
                
                    passName = input("\n Note for password: ")
                    password = ""

                    letterLarge = list(string.ascii_uppercase)
                    letterSmall = list(string.ascii_lowercase)
                    number = list(string.digits)

                    for i in range(3):
                            password += random.choice(letterLarge)

                    password += "_"

                    for i in range(4):
                            password += random.choice(letterSmall)

                    for i in range(4):
                            password += random.choice(number)

                    print("\n Password: " + passName + " - " + password)

                    f = open("pass.txt", "a")
                    f.write(passName + " - " + password + "\n")
                    f.close

                    input("\n Press any key to exit...")

                elif option == 2:
                    print("")
                    openPass = open("pass.txt", "r")
                    readPass = print(openPass.read())
                    print(str(readPass) + "\n")

                    input("\n Press any key to exit...")

                elif option == 3:
                
                    os.remove("pass.txt")

                else:
                    input("\n Press any key to exit...")

            ###########################################################
            #                       DECRYPTION                        #
            ###########################################################

            elif option == 2:
            
                def menu():
                
                        print(" [1] Encrypt")
                        print(" [2] Decrypt")
                        print(" [3] Generate key")
                        print(" [4] Delete key")

                print()
                menu()

                option = int(input("\n Choose option: "))

                if option == 1:
                
                    passList = "pass.txt"

                    if os.path.exists("key.key"):
                    
                            with open("key.key", "rb") as key:
                                    key = key.read()

                            with open(passList, "rb") as theFile:
                                    contents = theFile.read()

                            contents_encrypted = Fernet(key).encrypt(contents)

                            with open(passList, "wb") as theFile:
                                    theFile.write(contents_encrypted)

                            print("\n Encrypting...")
                    else:
                            print("\n Key is missing!")

                    input("\n Press any key to exit...")


                elif option == 2:
                
                    print("\n Decrypting...")

                    passList = "pass.txt"

                    if os.path.exists("key.key"):
                    
                            key = Fernet.generate_key()

                            with open("key.key", "rb") as key:
                                    decryptKey = key.read()

                            with open(passList, "rb") as theFile:
                                    contents = theFile.read()

                            contents_decrypted = Fernet(decryptKey).decrypt(contents)

                            with open(passList, "wb") as theFile:
                                    theFile.write(contents_decrypted)

                    else:
                            print("\n Key is missing!")

                    input("\n Press any key to exit...")

                elif option == 3:
                
                    key = Fernet.generate_key()

                    with open("key.key", "wb") as theKey:
                                    theKey.write(key)

                    print("\n Generating key... \n")

                elif option == 4:
                
                    os.remove("key.key")

                else:
                    input("\n Press any key to exit...")

            else:
                input("\n Press any key to exit...")

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
        nmapComm = os.system("nmap -sC -A -Pn "+ nmap)

    def sshFunc():

        logo = """

     ____                           ____  _          _ _ 
    / ___|  ___  ___ _   _ _ __ ___/ ___|| |__   ___| | |
    \___ \ / _ \/ __| | | | '__/ _ \___ \| '_ \ / _ \ | |
     ___) |  __/ (__| |_| | | |  __/___) | | | |  __/ | |
    |____/ \___|\___|\__,_|_|  \___|____/|_| |_|\___|_|_|

        """

        print(logo)

        sshUsr = input("User: ")
        sshIP = input("IP or hostname: ")
        os.system("ssh " + sshUsr + "@" + sshIP)

except KeyboardInterrupt:
     print("")
     input("\n Press any key to exit...")
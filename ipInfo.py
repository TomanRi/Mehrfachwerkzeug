import os

def ipInfoFunc():
    
    option = 1

    while option != 0:

        def menuIP():
            print(" [1] IPCONFIG")
            print(" [2] DHCP RENEW")
            print(" [0] Exit")

        print()
        menuIP()

        option = int(input("\n Choose option: "))

        if option == 1:
            ipInfo = os.system("ipconfig/all")

            input("\n Press any key to continue...")
        
        elif option == 2:
            dhcpRea = os.system("ipconfig/release")
            dhcpRen = os.system("ipconfig/renew")
            
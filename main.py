from tools import ipTrackerFunc
from tools import ipInfoFunc
from tools import passGenFunc
from tools import nmapFunc
from tools import sshFunc
import os

clear = lambda: os.system('cls')

clear()

try:

    logo = """

      __  __      _           __           _                      _                         
     |  \/  |    | |         / _|         | |                    | |                        
     | \  / | ___| |__  _ __| |_ __ _  ___| |____      _____ _ __| | __ _______ _   _  __ _ 
     | |\/| |/ _ \ '_ \| '__|  _/ _` |/ __| '_ \ \ /\ / / _ \ '__| |/ /|_  / _ \ | | |/ _` |
     | |  | |  __/ | | | |  | || (_| | (__| | | \ V  V /  __/ |  |   <  / /  __/ |_| | (_| |
     |_|  |_|\___|_| |_|_|  |_| \__,_|\___|_| |_|\_/\_/ \___|_|  |_|\_\/___\___|\__,_|\__, |
                                                                                       __/ |
                                                                                      |___/ 

    """


    option = 1

    while option != 0:

        def menuMain():
            print(logo + "\n")
            print(" [1] IP Tracker")
            print(" [2] IP Info")
            print(" [3] passGen")
            print(" [4] nmap")
            print(" [5] SSH")
            print(" [0] Exit")

        print()
        menuMain()

        option = int(input("\n Choose option: "))

        if option == 1:
            print("")
            ipTrackerFunc()

        elif option == 2:
            print("")
            ipInfoFunc()

        elif option == 3:
            print("")
            passGenFunc()

            clear()

        elif option == 4:
            print("")
            nmapFunc()

        elif option == 5:
            clear()
            print("")
            sshFunc()

except KeyboardInterrupt:

    print("")
    input("\n Press any key to exit...")
    
    clear()
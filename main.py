from ipTracker import getIP
from passGen import passGenFunc
import os

clear = lambda: os.system('cls')
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
        print(" [2] passGen")
        print(" [0] Exit")

    print()
    menuMain()

    option = int(input("\n Choose option: "))

    if option == 1:
        print("")
        getIP()

        input("\n Press any key to continue...")
        clear()


    elif option == 2:
        print("")
        passGenFunc()

        input("\n Press any key to continue...")
        clear()

    else:
        input("\n Press any key to exit...")
        clear()
        print(logo)
        clear()
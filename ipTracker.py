import ipinfo
import webbrowser
import os
from tkn import token

# Token can be found at https://ipinfo.io/ after signing in.

clear = lambda: os.system('cls')

def getIP():
    access_token = token
    handler = ipinfo.getHandler(access_token)
    
    ip_address = input(" Enter an IP address: ")

    if ip_address == "0":
        input("\n Press any key to exit...")
        clear()

    else:
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

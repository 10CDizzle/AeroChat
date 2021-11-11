#Main Program for accessing chat functions
import NetworkHandler
import ChatHelpers
import ConfigHelper

#Grab User Info and store globally.
UserInfo = ConfigHelper.LoadConfigs()

def main():
    print("***AeroChat ver. 0.1a***")
    print("Welcome {}.".format(UserInfo["Username"]))
    ChatHelpers.clearScr()
    print("***Setting Up BLE Comms***")
    OurDevice = NetworkHandler.BLEDevice(UserInfo)


if __name__ == '__main__':
    main()
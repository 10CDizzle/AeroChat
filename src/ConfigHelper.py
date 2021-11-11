# Container for Handling Configuration Files
import os

ConfigFolder = "{}/Configs/".format(os.getcwd())

#returns a dictionary with relevant configuration data
def LoadConfigs():
    ConfigDict = {}
    ConfigDict['Username'] = GetUsername()
    return ConfigDict

def GetUsername():
    return open("{}{}".format(ConfigFolder,"Username.txt"),'r').read()

def main():
    pass

if __name__ == '__main__':
    main()
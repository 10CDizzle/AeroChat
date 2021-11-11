#Simple container for setting up network settings/connections for each client
import bleak

#Class abstracting control of the bluetooth driver.

class BLEDevice:

    UserData = None

    def __init__(self, Userinfo):
        print("Beep boop, I'm an active BLEDevice Instance, aNd I know you are {}".format(Userinfo["Username"]))
        self.UserData = Userinfo




class ServerInstance:

    def __init__(self):
        print("Some Server... Somewhere.")

def main():
    pass

if __name__ == '__main__':
    main()
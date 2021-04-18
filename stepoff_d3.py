from time import sleep
# import RPi.GPIO as gpio
import sys
import ibmiotf.application # to install pip install ibmiotf
import ibmiotf.device


#Provide your IBM Watson Device Credentials
organization = "nwarur" #replace the ORG ID
deviceType = "device_third"#replace the Device type wi
deviceId = "device_third"#replace Device ID
authMethod = "token"
authToken = "shahrruck@student.tce.edu" #Replace the authtoken(device auth token)



# gpio.setmode(gpio.BOARD)
# gpio.setwarnings(False)

enable = 29 #stepper motor enable pin


# gpio.setup(29, gpio.OUT,initial = gpio.LOW)



def myCommandCallback(cmd): # function for Callback
        
        #print("Command received: %s" % cmd.data)

        status_of_data = (cmd.data['key3']).isalpha()

        if(status_of_data):
                if cmd.data['key3'] == 'stepperon':
                        print("stepper ON IS RECEIVED")
                        # gpio.output(29,gpio.LOW)
                elif cmd.data['key3'] =='stepperoff':
                        print("MOTOR OFF IS RECEIVED")
                        # gpio.output(29,gpio.HIGH)

                        
                #GPIO.cleanup()

        else:   


                print(int(cmd.data['key3']))                                     


         

        if cmd.command == "setInterval":

                if 'interval' not in cmd.data:
                        print("Error - command is missing required information: 'interval'")
                else:
                        interval = cmd.data['interval']
        elif cmd.command == "print":
                if 'message' not in cmd.data:
                        print("Error - command is missing required information: 'message'")
                #else:
                        #output=cmd.data['message']
                        #print(output)

try:
    deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
    deviceCli = ibmiotf.device.Client(deviceOptions)
    #..............................................

except Exception as e:
    print("Caught exception connecting device: %s" % str(e))
    sys.exit()

# Connect and send a datapoint "hello" with value "world" into the cloud as an event of type "greeting" 10 times
deviceCli.connect()

while True:

        deviceCli.commandCallback = myCommandCallback

# Disconnect the device and application from the cloud
deviceCli.disconnect()



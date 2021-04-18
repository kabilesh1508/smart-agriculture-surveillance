from time import sleep
# import RPi.GPIO as gpio
import sys
import ibmiotf.application # to install pip install ibmiotf
import ibmiotf.device


#Provide your IBM Watson Device Credentials
organization = "nwarur" #replace the ORG ID
deviceType = "device_first"#replace the Device type wi
deviceId = "device_first"#replace Device ID
authMethod = "token"
authToken = "shahrruck@student.tce.edu" #Replace the authtoken


#Motor gpio pins
# gpio.setmode(gpio.BOARD)
# gpio.setup(32,gpio.OUT,initial = gpio.HIGH) #motor pin : 32
# gpio.setwarnings(False)





def myCommandCallback(cmd): # function for Callback
        

        status_of_data = (cmd.data['key1']).isalpha()

        if(status_of_data):
                if cmd.data['key1'] == 'motoron':
                        print("MOTOR ON IS RECEIVED")
                        # gpio.output(32,gpio.LOW)
                elif cmd.data['key1'] =='motoroff':
                        print("MOTOR OFF IS RECEIVED")
                        # gpio.output(32,gpio.HIGH)

                        

                        

                        
                #GPIO.cleanup()

        else:   
                #if int(cmd.data['command']) > 100:
                  #      print("Turn Left")
                #elif int(cmd.data['command']) < 100:
                 #       print(" Turn right")

                print(int(cmd.data['key1']))


         

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



from time import sleep
# import RPi.GPIO as gpio
import sys
import ibmiotf.application # to install pip install ibmiotf
import ibmiotf.device


#Provide your IBM Watson Device Credentials
organization = "nwarur" #replace the ORG ID
deviceType = "device_second"#replace the Device type wi
deviceId = "device_second"#replace Device ID
authMethod = "token"
authToken = "shahrruck@student.tce.edu" #Replace the authtoken

#Stepper motor initialisation

DIR = 31
STEP = 33
CW =1
CCW =0

# gpio.setmode(gpio.BOARD)
# gpio.setwarnings(False)
#
# gpio.setup(DIR, gpio.OUT)
# gpio.setup(STEP, gpio.OUT)
# gpio.output(DIR,CW)



def myCommandCallback(cmd): # function for Callback
        

        status_of_data = (cmd.data['key2']).isalpha()

        if(status_of_data):

                while(cmd.data['key2'] =='stepperon'):
                    sleep(1)
                    # gpio.output(DIR, CW)
                    print("Forward Rotation starts")
                    for x in range(200):
                        # gpio.output(STEP, gpio.HIGH)
                        sleep(.0100)
                        # gpio.output(STEP, gpio.LOW)
                        sleep(.0100)

                    print("Backward Rotation starts")
                    sleep(0.5)
                    # gpio.output(DIR,CCW)
                    for x in range(200):
                        # gpio.output(STEP, gpio.HIGH)
                        sleep(.010)
                        # gpio.output(STEP, gpio.LOW)
                        sleep(.0110)


                        


        else:   

                print(int(cmd.data['key2']))


         

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



#Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import numpy as np
import cv2
import time
import imutils
# from imutils import FileVideoStream
from imutils.video import FileVideoStream, VideoStream
from imutils.video import FPS
import json
import boto3
import requests
from twilio.rest import Client as cl

import ibm_boto3
from ibm_botocore.client import Config
import socket
# import RPi.GPIO as gpio

account_sid = 'AC89fe45948b61d7f8b3cfa857b81cb43a'
auth_token = '1c41c1f944f32911854510e4d02aa671'

cos = ibm_boto3.client(service_name='s3',
                       ibm_api_key_id='buvY-YKO6fSBkVXDF_kPwNcmcrG9V7V4XtJzygAYeJL_',
                       ibm_service_instance_id='crn:v1:bluemix:public:cloud-object-storage:global:a/b899ba06add14a0dbd98042825b7d3e8:49b529d9-2f17-479a-b3f6-0a509bf25476::',
                       config=Config(signature_version='oauth'),
                       endpoint_url='https://s3.us-south.cloud-object-storage.appdomain.cloud')

#ibm cloud object storage




cl2 = cl(account_sid, auth_token)
i=0
j=0
count = 0


#Siren gpio pins
# gpio.setmode(gpio.BOARD)
# gpio.setup(35,gpio.OUT,initial = gpio.LOW) #motor pin : 32
# gpio.setwarnings(False)

#ibm cloud object storage credentials
cos = ibm_boto3.client(service_name='s3',
                       ibm_api_key_id='buvY-YKO6fSBkVXDF_kPwNcmcrG9V7V4XtJzygAYeJL_',
                       ibm_service_instance_id='crn:v1:bluemix:public:cloud-object-storage:global:a/b899ba06add14a0dbd98042825b7d3e8:49b529d9-2f17-479a-b3f6-0a509bf25476::',
                       config=Config(signature_version='oauth'),
                       endpoint_url='https://s3.us-south.cloud-object-storage.appdomain.cloud')


while True:

	client=boto3.client('rekognition',
	                    aws_access_key_id="ASIAUJOMIPXW53RL7BE4",
	                    aws_secret_access_key="RnvF66tSapr3hLnGMuU716SRDoGU7I4NRxEyIrXz",
	                    aws_session_token="FwoGZXIvYXdzEBAaDF5sW/nFSSLbAVUxCSLHAabJ+MGZg/draZfSYkbtqQEQ6W93d4vVGB0eqLsVjWBZLcIm7h8RZ5JChWkbFpaYn5MKLzIXTZD74wT7w2Klgd8f3Hi+OjzWjCHhvzQV6Fm8JD3g15lFTyqaOlHDG7rxya2HxqyeqgZ3ri4I//iPM2J+l80XzjLyV24fqmneXvsa35YAorfuS8J99MAjvA8YhzVJP10aHw+JR+ggH3+KASD4+lcnzsdxf8xdoojsJQWFR+qLDJVh+91hTea8/+LkiYQrw+MvpVAopc6X/gUyLcngax4jGPtooU4oTKWeHTt1DVahA1n+mN3aIPl0NVAamNjSmqGQYSYrcbv7TQ==",

	                    region_name='us-east-1')

	    #response = client.detect_labels(Image={'S3Object':{'Bucket':bucket,'Name':photo}},
	     #   MaxLabels=10)
	# path = "E:/cocurricular-1/trial/video.mp4"
	path = "rtsp://admin:UKQNXJ@25.34.134.216:554/h264_stream"
	# name = "boar.jpg"
	# name = r"test1.jpg"
	# img = cv2.imread(name)

	vs = VideoStream(path).start()
	#time.sleep(2.0)
	fps= FPS().start()

	while True:
		frame = vs.read()
		frame = imutils.resize(frame, width=600)
		name = "Test" + str(i) + ".jpg"
		cv2.imwrite(name,frame)
		i = i+1

		with open(name,'rb') as source_image:
		        
		    source_bytes=source_image.read()
		    print(type(source_bytes))
		    response = client.detect_custom_labels(
		        ProjectVersionArn='arn:aws:rekognition:us-east-1:295170506221:project/animal_detection/version/animal_detection.2020-11-27T22.32.31/1606496554158',
		       
		        Image={
		            'Bytes':source_bytes

		        },
		       
		        )


		

		if not len(response['CustomLabels']):
                        print('Animal not identified')
        		 # gpio.output(32,gpio.LOW)

		else:
			 # gpio.output(32,gpio.HIGH)
			for label in response['CustomLabels']:
				print ("Label: " + label['Name'])
				print ("Confidence: " + str(label['Confidence']))
				# print ("Instances:")
		        # for instance in label['Geometry']['BoundingBox']['Width']:
		        #     # print ("  Bounding box")
		        #     # print ("    Top: " + str(instance[0]))
		        #     # print ("    Left: " + str(instance['Left']))
		        #     # print ("    Width: " +  str(instance['BoundingBox']['Width']))
		        #     # print ("    Height: " +  str(instance['BoundingBox']['Height']))
		        #     # print ("  Confidence: " + str(instance['Confidence']))
		        #     print(int(instance))



				Width = label['Geometry']['BoundingBox']['Width']
				Height = label['Geometry']['BoundingBox']['Height']
				Top = label['Geometry']['BoundingBox']['Top']
				Left = label['Geometry']['BoundingBox']['Left']

				print("Width : " + str(Width))
				print("Height : "+ str(Height))
				print("Top : "+str(Top))
				print("Left : " +str(Left))


			height, width, channels = frame.shape

		# cv2.line(img,(0,0),(200,300),(255,255,255),50)
			leftbox = int(width * Left)
			topbox = int(height * Top)
			widthbox = int(width * Width)
			heightbox = int(height * Height)

			cv2.rectangle(frame, (leftbox, topbox), (leftbox+widthbox, topbox+heightbox) ,(0, 255, 0), 6)
			namedec = "detected"+ ".jpg"
			cv2.imwrite(namedec, frame)
		                 
		# cv2.imshow('image', img)

		# cv2.waitKey(0)
			print('Animal identified')



            # print('response['CustomLabels'].Name')
            # img=cv2.imread(person.jpg)
            # cv2.imshow("detected", frame)
			# cv2.imshow("detected", frame)
			# # cv2.waitKey()
			# time.sleep(5)
			# cv2.destroyAllWindows()
            # cv2.imshow("detected", img)

            

			message = cl2.messages.create(
                                  body='Animal has been detected',
                                  from_='+15172009420',
                                  to='+918248256456'
                              )



			try:

				res = cos.upload_file(namedec, 'animaldetection2', 'detected.jpg')
			except Exception as e:
				print(Exception, e)
			else:
				print('File Uploaded')





			cv2.destroyAllWindows()




        #print ("Parents:")
        #for parent in label['Parents']:
         #   print ("   " + parent['Name'])
        #print ("----------")
        #print ()
    #return len(response['Labels'])


#def main():
    #photo=''
    #bucket=''
    #label_count=detect_labels(photo, bucket)
    #print("Labels detected: " + str(label_count)


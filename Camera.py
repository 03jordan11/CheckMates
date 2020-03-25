#!/usr/bin/env python
# coding: utf-8


import imutils
import cv2

class Camera:

	def __init__(self,test_flag):
		#placeholder
		self.cam = True
		self.test_flag = test_flag

	def takePicture(self):
		'''grab an image from the camera'''
        
		if self.test_flag:
		# for testing purpose
			img_filename = "image1.jpg" # Read image of clear board
			image = cv2.imread(img_filename)
		else:
			pass
			# take a picture
			# **** Need to be edit ****
		resized_image = imutils.resize(image, height = 500, width = 500)
		return resized_image


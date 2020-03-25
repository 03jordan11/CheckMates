#!/usr/bin/env python
# coding: utf-8


import cv2
import numpy as np
import math

debug = False


class Board:
	"""
	Holds all the Square instances and updates changes to board after moves
	"""
	def __init__(self, squares,test_flag):

		self.squares = squares
		self.boardMatrix = []
		self.move = 'e2e4'
		self.test_flag = test_flag
		self.promotion = 'q'
		self.promo = False


	def draw(self,image):
		""" 
		For testing purposes, draws the board and classifies the squares (draws the square state on the image).
		"""
		for square in self.squares:
			square.draw(image, (0,0,255))
			square.classify(image)

	def assignState(self):
		"""
		Assigns initial setup states to squares and initializes the Board matrix.
		"""
		black = ['r', 'n', 'b','q','k','b','n','r']
		white = ['R','N','B','Q','K','B','N','R']

		for i in range(8):
			self.squares[8*i + 0].state = black[i]
			self.squares[8*i + 1].state = 'p'
			self.squares[8*i + 2].state = '.'
			self.squares[8*i + 3].state = '.'
			self.squares[8*i + 4].state = '.'
			self.squares[8*i + 5].state = '.'
			self.squares[8*i + 6].state = 'P'
			self.squares[8*i + 7].state = white[i]

		for square in self.squares:
			self.boardMatrix.append(square.state)

	def determineChanges(self,previous, current):
		'''
		Determines the change within squares from "previous" picture to "current" picture to infer piece movement (calls "computer vision" Layer)
        
		**** Need to be edit ****
        update the move and return the move
		'''


		return self.move


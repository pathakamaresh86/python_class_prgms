#!/usr/bin/python
import pickle
class Card:
	def __init__(self, cardNumber, cardPin, cardType):
		self.cardNumber = cardNumber
		self.__cardPin = cardPin
		self.cardType = cardType
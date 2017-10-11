#!/usr/bin/python3
# -*- coding: utf-8 -*-

from OpenGL.GL import *

_MAX_LIGHTS = 8

class Lamp(object):
	
	__FreeNumbers = [eval('GL_LIGHT{0}'.format(x)) 
					 for x in range(0, _MAX_LIGHTS)] # создание списка из последовательности
	
	def __init__(self, number = None):
		
		if number is not None:
			self.__Number = Lamp.__FreeNumbers[number]
			if self.__Number is None:
				raise ValueError('Number already taken')
			Lamp.__FreeNumbers[number] = None
		else:
			for k in range(0, _MAX_LIGHTS):
				if Lamp.__FreeNumbers[k] is None:
					continue
				self.__Number = Lamp.__FreeNumbers[k]
				Lamp.__FreeNumbers[k] = None
				break
			else:
				raise ValueError('No free numbers')
	
	@property
	def enable(self):
		return glIsEnable(self.__Number)
	
	@enable.setter
	def enable(self, value):
		if value:
			glEnable(self.__Number)
		else:
			glDisable(self.__Number)
	
	number = property (lambda self: self.__Number)
	ambient = property(lambda self: self.__Ambient)
	diffuse = property(lambda self: self.__Diffuse)
	specular = property(lambda self: self.__Specular)
	position = property(lambda self: self.__Position)
	
	@ambient.setter
	def ambient(self, value):
		glLightfv(self.__Number, GL_AMBIENT, value)
		self.__Ambient
		
	@diffuse.setter
	def diffuse(self, value):
		glLightfv(self.__Number, GL_DIFFUSE, value)
		self.__Diffuse = value
		
	@specular.setter
	def specular(self, value):
		glLightfv(self.Number, GL_SPECULAR, value)
		self.__Specular = value
		
	@position.setter
	def position(self, value):
		glLightfv(self.Number, GL_POSITION, value)
		self.__Position = value
		
	def __del__(self):
		#self.enable = False
		for k in range(0, _MAX_LIGHTS):
			if Lamp.__FreeNumbers[k] is None:
				Lamp.__FreeNumbers[k] = self.__Number
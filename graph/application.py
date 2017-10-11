#!/usr/bin/python3
# -*- coding: utf-8 -*-

# добавить в класс свойство которое включает/выключает GL_COLOR_MATERIAL на основе GL_LIGHTING

import sys
from contextlib import suppress
from abc import ABCMeta, abstractmethod
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class Application(object, metaclass = ABCMeta):

	def __init__(self):
		self.__DisplayMode = set([
			GLUT_RGBA,
			GLUT_DOUBLE,
			GLUT_DEPTH,
			GLUT_MULTISAMPLE
		])
		self.__WindowSize = (800, 600)
		self.__Title = 'Experimental'
		glutInit(sys.argv)
		
	@property	
	def lighting(self):
		return glIsEnable(GL_LIGHTING)
		
	@lighting.setter
	def lighting(self, value):
		if value:
			glEnable(GL_LIGHTING)
		else:
			glDisable(GL_LIGHTING)
	# (glEnable if value else glDisable)(GL_LIGHTING)
	
	'''
	lighting = property(
		lambda self: glIsEnabled(GL_LIGHTING),
		lambda self, value:
		(glEnable if value else glDisable)(GL_LIGHTING)	
	)
	'''
	
	
	rgba = property(lambda self: GLUT_RGBA in self.__DisplayMode)
	double_buffer = property(lambda self: GLUT_DOUBLE in self.__DisplayMode)
	depth_buffer = property(lambda self: GLUT_DEPTH in self.__DisplayMode)
	multisample = property(lambda self: GLUT_MULTISAMPLE in self.__DisplayMode)
	
	@rgba.setter
	def rgba(self, value):
		if value:
			self.__DisplayMode.add(GLUT_RGBA)
		else:
			self.__DisplayMode.remove(GLUT_RGBA)
			
	win_size = property(lambda self: self.__WindowSize)
	
	win_pos = property(lambda self: self.__WindowPos)
	
	@win_pos.setter
	def win_pos(self, value):
		self.__WindowPos = value
		
	title = property(lambda self: self.__Title)	
	
	@property
	def display_mode(self):
		result = 0
		for flag in self.__DisplayMode:
			result |= flag
		return result
	
	def init_window(self):
		glutInitDisplayMode(self.display_mode)
		glutInitWindowSize(*self.win_size)
		with suppress(AttributeError):
			glutInitWindowPosition(*self.win_pos)
		glutCreateWindow(self.title.encode('windows-1251'))
	
	def draw(self):
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		glLoadIdentity()
		glScalef(0.1,  0.1, 0.1)
		self.draw_stage()
		glutSwapBuffers()
	
	@abstractmethod
	def draw_stage(self):
		pass
	
	def timer(self, number):
		pass
	
	def resize(self, width, height):
		glViewport(0, 0, width, height)
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		a = width / height
		glOrtho(-a, a, -1.0, 1.0, -1.0, 1.0)
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()
	
	def init_context(self):
		glClearColor(0.0, 0.0, 0.0, 0.0)
		if self.depth_buffer:
			glEnable(GL_DEPTH_TEST)
		#if self.multisample:
		#	glEnable(GL_MULTISAMPLE)
		glEnable(GL_COLOR_MATERIAL)
		self.lifgting = True
		
		glutTimerFunc( 1000//30, self.timer, 1 )
		glutReshapeFunc(self.resize) # функция которую использует главный цикл, для отслеживания изменения размера окна
		glutDisplayFunc(self.draw) # функция которую использует главный цикл, для отрисовки сцены
	
	def run(self):
		self.init_window()
		self.init_context()
		glutMainLoop()
		
	
		
		
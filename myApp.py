#!/usr/bin/python3
# -*- coding: utf-8 -*-
import time
import graph
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class MyApp(graph.Application):
	
	def __init__(self):
		super().__init__()
		self.__Lamp = graph.Lamp()
		self.__CubeA = graph.Cube(4.0, 30.0)
	
	def init_context(self):
		super().init_context()
		self.__Lamp.ambient = (1.0, 2.0, 3.0, 1.0)
		self.__Lamp.diffuse = (1.0, 1.0, 1.0, 1.0)
		self.__Lamp.enable = False
		
	def timer(self, number):
		self.__CubeA.angle += 0.5
		glutTimerFunc( 1000//30, self.timer, 1 )
		glutPostRedisplay()
		
	def draw_stage(self):
		self.__CubeA.draw()
		#with graph.figure(GL_TRIANGLES):
			#glVertex3f(0.0, 0.0, 0.0)
			#glVertex3f(1.0, 1.0, 0.0)
			#glVertex3f(0.0, 1.0, 0.5)
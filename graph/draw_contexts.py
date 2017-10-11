#!/usr/bin/python3
# -*- coding: utf-8 -*-

from contextlib import contextmanager
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# создание менеджера контекста с помощью декоратора
@contextmanager
def figure(mode):
	glBegin(mode)
	try:
		yield
	finally:
		glEnd()

# создание объекта менеджера контекста		
class DrawContext(object):
	
	def __init__(self):
		pass
		
	def __enter__(self):
		glPushMatrix() # для работы с библиотекой openGL
		return self
		
	def __exit__(self, exc_type, exc_value, traceback):
		glPopMatrix() # для работы с библиотекой openGL
		return False
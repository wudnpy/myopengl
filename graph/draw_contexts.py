#!/usr/bin/python3
# -*- coding: utf-8 -*-

from contextlib import contextmanager
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

@contextmanager
def figure(mode):
	glBegin(mode)
	try:
		yield
	finally:
		glEnd()
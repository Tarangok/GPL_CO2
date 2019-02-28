import matplotlib.pyplot as plt
import numpy as np
from math import *
from tkinter import *
import pickle
from colour import Color 
import datetime
#from tkinter import Tk, BOTH, IntVar, LEFT
from tkinter.ttk import Frame, Label, Scale, Style
from threading import Thread


class Point:
	def __init__( self, x, y, time, value):
		self.x = x
		self.y = y
		self.time = datetime.datetime.strptime(time, '%Y-%m-%d %H:%M:%S.%f').date()
		self.value = value

	def Print( self ):
		print("lat =% 4.8f;\t long =% 4.8f;\t val = % 4.8f;\t time = %s " % ( self.x, self.y, self.value, self.time ))

	def GetX( self ):
		return self.x

	def GetY( self ):
		return self.y

	def GetV( self ):
		return self.value

def byValue(point):
	return point.GetV()

def onScale(val):
	canv.delete("all")
	time = keys[int(float(val))]
	for p in points[time]:
		clr = colors[int(p.GetV() - 370)].get_hex()
		x1, y1 = 540 + p.GetX()*3-2, 270 + p.GetY()*-3+2  
		x2, y2 = 540 + p.GetX()*3+2, 270 + p.GetY()*-3-2
		canv.create_oval(x1, y1, x2, y2, outline=clr, fill=clr)
		#iterator_1 += 1
	
	var.set(time)

if __name__ == "__main__":    
	with open( "points.g2s", "rb" ) as file:
		points = pickle.load( file )
	
	##points.sort(key=byValue)

	root = Tk()

	colors = list(Color("blue").range_to(Color("red"), 150))
	canv = Canvas(root, width = 1080, height = 540, bg = "white")
	global keys
	keys = list(points.keys())
	iterator_1 = 1
	#keysList = list()
	#for key in points:
	#	print(iterator_1, " ", key)
	#	iterator_1 += 1
	global time
	time = "2009-05"
	
	
		#time = input("Enter date: ")
		#canv.delete("all")
		#if time == "exit":
		#	canv.destroy()
		#	break
	#for p in points[time]:
	#	clr = colors[int(p.GetV() - 370)].get_hex()
	#	x1, y1 = 540 + p.GetX()*3-2, 270 + p.GetY()*-3+2  
	#	x2, y2 = 540 + p.GetX()*3+2, 270 + p.GetY()*-3-2
	#	canv.create_oval(x1, y1, x2, y2, outline=clr, fill=clr)
	#	iterator_1 += 1

	canv.pack()	

	global var 
	var = IntVar()
	label = Label(root, text=0, textvariable=var)        
	label.pack(side=LEFT)
	scale = Scale(root, from_=1, to=114, command=onScale)
	scale.pack(side=BOTTOM, padx=15)
	#canv.bind( "<B1-Motion>", paint )
	
	canv.mainloop()

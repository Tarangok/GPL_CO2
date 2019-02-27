import matplotlib.pyplot as plt
import numpy as np
from math import *
from tkinter import *
import pickle
from colour import Color 
import datetime


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

if __name__ == "__main__":    
	with open( "points.g2s", "rb" ) as file:
		points = pickle.load( file )
	
	##points.sort(key=byValue)

	root = Tk()

	colors = list(Color("blue").range_to(Color("red"), 150))
	canv = Canvas(root, width = 1300, height = 700, bg = "white")
	keys = list(points.keys())
	iterator_1 = 1
	for key in keys:
		if key == "None":
			continue
		for p in points[key]:
			clr = colors[int(p.GetV() - 370)].get_hex()
			x1, y1 = p.GetX()*4-2, p.GetY()*4-2  
			x2, y2 = p.GetX()*4+2, p.GetY()*4+2
			#canv.create_oval(570 + p.GetY()*4, 350 + p.GetX()*-5, 570 + p.GetY()*4 + 4, 350 + p.GetX()*-5 + 4, outline=clr, fill=clr)
			canv.create_oval(x1, y1, x2, y2, outline=clr, fill=clr)
			iterator_1 += 1

			canv.pack()
	canv.pack()	
	
	root.mainloop()

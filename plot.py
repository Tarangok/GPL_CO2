import matplotlib.pyplot as plt
import numpy as np
from math import *
from tkinter import *
import pickle
from colour import Color 
import datetime


class Point:
	def __init__( self, x, y, time, value ):
		self.x = x
		self.y = y
		self.time = time
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
	
	points.sort(key=byValue)

	root = Tk()

	colors = list(Color("blue").range_to(Color("red"), 40))
	canv = Canvas(root, width = 1300, height = 700, bg = "white")
	#pilImage = Image.open("world_map.jpg")
	#image = ImageTk.PhotoImage(pilImage)
	#imagesprite = canv.create_image(600,400,image=image)
	iterator_1 = 1
	for p in points:
		clr = colors[int(p.GetV() - 364)].get_hex()
		canv.create_oval(570 + p.GetY()*4, 350 + p.GetX()*-5, 570 + p.GetY()*4 + 4, 350 + p.GetX()*-5 + 4, outline=clr, fill=clr)
		iterator_1 += 1

		canv.pack()
	canv.pack()	
	
	root.mainloop()

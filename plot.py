import matplotlib.pyplot as plt
import numpy as np
from math import *
#from tkinter import *
import pickle
#import 
#from PIL import Image, ImageTk

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


if __name__ == "__main__":    
	
	with open( "points.g2s", "rb" ) as file:
		points = pickle.load( file )

	root = Tk()
	RED = "#f00"
	GREEN = "#0f0"
	BLUE = "#00f"
	canv = Canvas(root, width = 1300, height = 700, bg = "white")
	#pilImage = Image.open("world_map.jpg")
	#image = ImageTk.PhotoImage(pilImage)
	#imagesprite = canv.create_image(600,400,image=image)
	iterator_1 = 1
	for p in points:
		#print( iterator_1, " ", p.GetX(), " ", p.GetY())
		if p.GetV() < 400: 
			color = BLUE
		if (p.GetV() >= 400) & (p.GetV() < 410):
			color = GREEN
		if p.GetV() >= 410:
			color = RED
		canv.create_oval(570 + p.GetY()*4, 350 + p.GetX()*-5, 570 + p.GetY()*4 + 1, 350 + p.GetX()*-5 + 1, outline=color)
		iterator_1 += 1
		canv.pack()
	canv.pack()	
	
	root.mainloop()

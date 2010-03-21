""" 
    Copyright 2008 Marcel Pinheiro Caraciolo <caraciol@gmail.com>
    Modified on 21st March, 2010 by Matovu Richard, Email: rkmatrich@gmail.com, Website: http://www.matrich.net/ 
 
    This file is part of PySChart.

    PySChart is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Lesser Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    PySChart is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Lesser Public License for more details.

    You should have received a copy of the GNU General Lesser Public License
    along with PySChart; if not, write to the Free Software
    Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""
from __future__ import generators
import graphics, appuifw, key_codes


# linechart.py - Line Chart Plotter for PyS60
# @version 0.7
# @date:  21/03/2010

class LineChart:


    ##Creates a new instance of LineChart.
    # @param size  		Chart's size (width,height)
    # @param xyrange 	The list with x and y range [min_x,max_x,step_x,min_y,max_y,step_y]
    # @param xyvalues 	The list with values of (x,y) data
    # @param colors 	The list of colors for the lines of the data     
    # @param legend 	The list of labels of data
    # @param color 		The color of the line
    # @param colorBack 	The background color
    # @param xaxislabels 	The list of x-axis labels
    # @param formatter 	The format of the series composed in the chart
    def __init__(self,size,xyrange,xyvalues,colors,legend=[], color = (255,0,0),
                  colorBack=(255,255,255), xaxislabels = [], formatter=lambda x:x):

        self._img = graphics.Image.new(size)
        self._view = appuifw.Canvas(redraw_callback= self._OnUpdate)
        appuifw.app.body = self._view
        
        self._view.bind(key_codes.EKeyLeftArrow,lambda: self._traverse(1))
        self._view.bind(key_codes.EKeyRightArrow,lambda: self._traverse(0))

        self._width,self._height = self._img.size        
        self._position = None
        self._min_x = None
        self._min_y = None
        self._scale_x = None
        self._legend = legend
        self._scale_y = None
        self._axe_x = 0
        self._actual_pos = 0
        self._xyrange = xyrange
        self._colorBack = colorBack
        self._color = color
        self._formatter = formatter
        self._xyvalues = xyvalues
	self._colors = colors
	self._xaxislabels = xaxislabels
        
        self._setPosition()
        self._set_axes()
        self._plot()

    ##Callback method for key events (navigates into the chart)
    def _traverse(self,code):
        #left
        if code: 
            if self._actual_pos > 0: 
                self._actual_pos -= 1
                self._set_axes()
                self._plot()
        #right
        else:
            if self._actual_pos < len(self._xs)-1:
                self._actual_pos += 1
                self._set_axes()
                self._plot()

    ##Handler for the paint the scren
     # @param self The object pointer.           
     # @param rect The screen itself.
    def _OnUpdate(self,rect):
        self._view.blit(self._img)
        

    ##Defines the ranges of the graph in the screen.
    def _setPosition(self):
        left = self._view.measure_text(unicode(float(self._xyrange[4])), font=('normal',10,graphics.FONT_BOLD))[1]
        self._position = [left+2,self._height-40,self._width-10,10]
        
     
     
    ## Iterator for generate random numbers
    #  @param self The object pointer.  
    #  @param start The first number of the series
    #  @param stop The last number of the series
    #  @param step  The incrementator given
    def _arange(self,start, stop=None, step=None):
        if stop is None:
            stop = float(start)
            start = 0.0
        if step is None:
            step = 1.0
        cur = float(start)
        while cur < stop:
            yield cur
            cur+= step
     
     
     ## Plot chart axes.
      # @param self The object pointer.
    def _set_axes(self):
        #position: The position where the chart will be painted [left,bottom,right,top]
        left,bottom,right,top = self._position
        self._min_x,max_x,step_x,self._min_y,max_y,step_y = self._xyrange
        self._scale_x = float(right - left)/(max_x-self._min_x)
        self._scale_y = float(bottom - top)/(max_y-self._min_y)
        
        self._img.clear()
        self._img.rectangle([(left,top),(right+1,bottom+1)],0,fill = self._colorBack)

        self._axe_x = 0
        
	xaxislabelcount = 0
        #~ #Plot the data legends.
        for x in self._arange(self._min_x,max_x,step_x):
	    if not self._xaxislabels:
		self._img.text((15+self._scale_x*(x-self._min_x), self._height-24), unicode(self._formatter(x)), font= ('normal',10,graphics.FONT_BOLD))
	    else:
		self._img.text((15+self._scale_x*(x-self._min_x), self._height-24), unicode(self._xaxislabels[xaxislabelcount]), font= ('normal',10,graphics.FONT_BOLD))
		xaxislabelcount = xaxislabelcount + 1
            for z in range(top,bottom,3):
                self._img.point((left+self._scale_x*(x-self._min_x),z),0)
                self._img.point((left+self._scale_x*(x-self._min_x),z+1),0)            
            self._img.point((left+self._scale_x*(x-self._min_x), bottom-1), 0)
            self._img.point((left+self._scale_x*(x-self._min_x), top+1), 0)

        #Plot y data set.    
        for y in self._arange(self._min_y,max_y,step_y):
            self._img.text((2,bottom+2-self._scale_y*(y-self._min_y)), unicode(self._formatter(y)), font= ('normal',10,graphics.FONT_BOLD))
            for i in range(left,right,3):            
                self._img.point((i,bottom-self._scale_y*(y-self._min_y)), 0)
                self._img.point((i+1,bottom-self._scale_y*(y-self._min_y)), 0)   
            self._img.point((left+1, bottom-self._scale_y*(y-self._min_y)), 0)
            self._img.point((right-1,bottom-self._scale_y*(y-self._min_y)), 0)
            
       #Plot x data set. 
        self._xs = []
	self._ys = []
        for xyvalue in self._xyvalues:
	    for (x,y) in xyvalue:
		self._xs.append(x)
		self._ys.append(y)
			
        for x in self._xs:
            if self._axe_x == self._actual_pos:
                for z in range(top,bottom,3):
                    self._img.point((left+self._scale_x*(x-self._min_x),z), outline = self._color)
                    self._img.point((left+self._scale_x*(x-self._min_x),z+1), outline = self._color)            
                self._img.point((left+self._scale_x*(x-self._min_x), bottom-1), 0)
                self._img.point((left+self._scale_x*(x-self._min_x), top+1), 0)

                tl = (left+self._scale_x*(x-self._min_x)-5, top+7)
            self._axe_x +=1
            
    ## Plot the real graph
     #  @param self The object pointer.  
    def _plot(self):
            
        left,bottom,right,top = self._position
	
	color_index = 0
	lx,ly = 2,15
	for xyvalue in self._xyvalues:
		last = left + (xyvalue[0][0] - self._min_x) * self._scale_x, bottom - (xyvalue[0][1]-self._min_y) * self._scale_y
		for (x,y) in xyvalue:
			for i in range(1, len(xyvalue)):
			    p = left + (x - self._min_x) * self._scale_x, bottom - (y-self._min_y) * self._scale_y 
			    self._img.line([last, p], self._colors[color_index])
			    last = p
			self._img.point(last, self._colors[color_index])
		# Draw the legends		
		endlx = lx + 15
		self._img.rectangle([(lx,bottom+17),(ly,self._height-4)],0,fill = self._colors[color_index] )
		self._img.text((endlx,self._height-5), unicode(self._legend[color_index]), font= ('normal',12))
		
		color_index = color_index + 1
		lx,ly = lx + 80, ly + 80
       
        self._OnUpdate(None)      

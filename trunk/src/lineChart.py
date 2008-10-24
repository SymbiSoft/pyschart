""" 
    Copyright 2008 Marcel Pinheiro Caraciolo <caraciol@gmail.com>
 
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

from appuifw import *

# linechart.py - Line Chart Plotter for PyS60
# @version 0.1
# @date:  24/10/2008


class LineChart:
    
    ##The constructor.
    # @param canvas: The graphics component
    # @param xyrange: The list with x and y range [min_x,max_x,step_x,min_y,max_y,step_y]
    # @param subtitle: the subtitle for x axe
    # @param colorLine: The color of the line
    # @param colorBack: The background color
    # @param formatter: The format of the series composed in the chart
    def __init__(self,canvas,xyrange,subtitle="",colorLine=(255,0,0),
                  colorBack=(255,255,255),formatter=lambda x:x):
        self._view = canvas
        self._width,self._height = self._view.size
        self._position = None
        self._min_x = None
        self._min_y = None
        self._scale_x = None
        self._scale_y = None        
        self._setPosition()
        self._set_axes(xyrange,color_rect,formatter)
    
    ##Defines the ranges of the graph in the screen.
    def setPosition(self):
        self._position = [26,self._height-19,self._width-10,10]
           
     
     ## Plotthe chart axes.
      # @param self The object pointer.
      # @param xyrange: The list with x and y range [min_x,max_x,step_x,min_y,max_y,step_y]
      # @param color_rect: The color used to fill the chart
      # @param formatter: The format of the numbers in the chart
    def set_axes(self,xyrange,color_rect,formatter):
        #position: The position where the chart will be painted [left,bottom,right,top]
        left,bottom,right,top = position
        self._min_x,max_x,step_x,self._min_y,max_y,step_y = xyrange
        self._scale_x = float(right - left)/(max_x-self.min_x)
        self._scale_y = float(bottom - top)/(max_y-self.min_y)
        self._view.clear()
        
          
     
     ## Plot the graph axes
        #  @param self The object pointer.  
        #  @param xyrange: The list with x and y range [min_x,max_x,step_x,min_y,max_y,step_y]

        #  @param color: The color used to fill the graph
        #  @param formater:  The format of the numbers composed in the graph
    def set_axes(self,xyrange,position,color=(255,255,255),formatter=lambda x:x):        
        self.left,self.bottom,self.right,self.top = position
        self.min_x,max_x,step_x,self.min_y,max_y,step_y = xyrange
        self.scale_x = float(self.right-self.left)/(max_x-self.min_x)
        self.scale_y = float(self.bottom-self.top)/(max_y-self.min_y)
        self._view.clear()
        self._view.rectangle([(self.left,self.top), (self.right+1, self.bottom+1)],0, fill = color)
        for x in self.arange(self.min_x,max_x,step_x):
            self._view.text((14+self.scale_x*(x-self.min_x), self.height-1), unicode(formatter(x)))
            self._view.point((self.left+self.scale_x*(x-self.min_x), self.bottom-1), 0)
            self._view.point((self.left+self.scale_x*(x-self.min_x), self.bottom-1), 0)
            self._view.point((self.left+self.scale_x*(x-self.min_x), self.top+1), 0)
        for y in self.arange(self.min_y, max_y, step_y):
            for i in range(self.left,self.right):
                if(i%2 ==0):
                    self._view.point((i,self.bottom-self.scale_y*(y-self.min_y)), 0)
            if y!= 0:
                self._view.text((2, self.bottom+2-self.scale_y*(y-self.min_y)), unicode(formatter(y)))
            self._view.point((self.left+1, self.bottom-self.scale_y*(y-self.min_y)), 0)
            self._view.point((self.right-1, self.bottom-self.scale_y*(y-self.min_y)), 0)


      
x=        
//.idjsdksjdkjdksd

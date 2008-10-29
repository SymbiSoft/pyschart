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
from __future__ import generators
from graphics import *
from appuifw import *

# linechart.py - Line Chart Plotter for PyS60
# @version 0.4
# @date:  26/10/2008

class LineChart:
    
    ##The constructor.
    # @param canvas: The graphics component
    # @param xyrange: The list with x and y range [min_x,max_x,step_x,min_y,max_y,step_y]
    # @param subtitle: the subtitle for x axe
    # @param colorBack: The background color
    # @param formatter: The format of the series composed in the chart
    def __init__(self,canvas,xyrange,subtitle="",
                  colorBack=(255,255,255),formatter=lambda x:x):
        self._view = canvas
        self._width,self._height = self._view.size
        self._position = None
        self._min_x = None
        self._min_y = None
        self._scale_x = None
        self._subtitle = unicode(subtitle)
        self._scale_y = None        
        self._setPosition(xyrange)
        self._set_axes(xyrange,colorBack,formatter)
    
    ##Defines the ranges of the graph in the screen.
    def _setPosition(self,xyrange):
        left = self._view.measure_text(unicode(float(xyrange[4])), font=('normal',10,FONT_BOLD))[1]
        self._position = [left+2,self._height-40,self._width-10,10]
        
     
     
    ## Iterator for generate random numbers
    #  @param self The object pointer.  
    #  @param start: The first number of the series
    #  @param stop: The last number of the series
    #  @param step:  The incrementator given
    def __arange(self,start, stop=None, step=None):
        if stop is None:
            stop = float(start)
            start = 0.0
        if step is None:
            step = 1.0
        cur = float(start)
        while cur < stop:
            yield cur
            cur+= step
     
     
     ## Plotthe chart axes.
      # @param self The object pointer.
      # @param xyrange: The list with x and y range [min_x,max_x,step_x,min_y,max_y,step_y]
      # @param colorBack: The color used to fill the chart
      # @param formatter: The format of the numbers in the chart
    def _set_axes(self,xyrange,colorBack,formatter):
        #position: The position where the chart will be painted [left,bottom,right,top]
        left,bottom,right,top = self._position
        self._min_x,max_x,step_x,self._min_y,max_y,step_y = xyrange
        self._scale_x = float(right - left)/(max_x-self._min_x)
        self._scale_y = float(bottom - top)/(max_y-self._min_y)
        self._view.clear()
        self._view.rectangle([(left,top),(right+1,bottom+1)],0,fill = colorBack)

        for x in self.__arange(self._min_x,max_x,step_x):
            #self._view.text((14+self._scale_x*(x-self._min_x), self._height-1), unicode(formatter(x)))         
            for z in range(top,bottom,3):
                self._view.point((left+self._scale_x*(x-self._min_x),z),0)
                self._view.point((left+self._scale_x*(x-self._min_x),z+1), 0)                 
            self._view.point((left+self._scale_x*(x-self._min_x), bottom-1), 0)
            self._view.point((left+self._scale_x*(x-self._min_x), top+1), 0)
        
        for y in self.__arange(self._min_y,max_y,step_y):
            self._view.text((2,bottom+2-self._scale_y*(y-self._min_y)), unicode(formatter(y)), font= ('normal',10,FONT_BOLD))
            for i in range(left,right,3):            
                self._view.point((i,bottom-self._scale_y*(y-self._min_y)), 0)
                self._view.point((i+1,bottom-self._scale_y*(y-self._min_y)), 0)   
            self._view.point((left+1, bottom-self._scale_y*(y-self._min_y)), 0)
            self._view.point((right-1,bottom-self._scale_y*(y-self._min_y)), 0)
            
       
            
            
    ## Plot the real graph
        #  @param self The object pointer.  
        #  @param xs: The list with x series 
        #  @param ys: The list with the y series
        #  @param color: The color used to fill the line     
    def plot(self,xs,ys=None,color = (255,0,0)):
        if ys == None:
            ys = xs
            xs = range(len(ys))
        left,bottom,right,top = self._position
        last = left + (xs[0] - self._min_x) * self._scale_x, bottom - (ys[0]-self._min_y) * self._scale_y    
        for i in range(1, len(ys)):
            p = left + (xs[i] - self._min_x) * self._scale_x, bottom - (ys[i]-self._min_y) * self._scale_y 
            self._view.line([last, p], color)
            last = p
        self._view.point(last,color)

        #The subtitle
        self._view.rectangle([(2,bottom+17),(15,self._height-4)],0,fill = color )
        self._view.text((17,self._height-5), self._subtitle, font= ('normal',13))
       
            

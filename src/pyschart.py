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
# @version 0.2
# @date:  26/10/2008

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
        self._set_axes(xyrange,colorBack,formatter)
    
    ##Defines the ranges of the graph in the screen.
    def _setPosition(self):
        self._position = [26,self._height-19,self._width-10,10]
           
     
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
          
   

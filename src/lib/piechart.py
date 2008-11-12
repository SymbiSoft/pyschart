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
import graphics, appuifw, key_codes


# piechart.py - Pie Chart Plotter for PyS60
# @version 0.2
# @date:  11/11/2008


class PieChart:

    #The default font for the texts
    FONT = font=('normal',10,graphics.FONT_BOLD)



    ##Creates a new instance of PieChart.
    # @param size  Chart's size (width,height)
    # @param data   Values of the data  [(subtitle,value)]
    # @param colors Color of the bars of the graph [color]
    # @param colorBack The background color
    # @param formatter The format of the series composed in the chart
    def __init__(self,size,data,colors,colorBack=(255,255,255),formatter=lambda x:x):
        self._img = graphics.Image.new(size)
        self._view = appuifw.Canvas(redraw_callback = self._OnUpdate)
        appuifw.app.body = self._view
        
        self._view.bind(key_codes.EKeyLeftArrow,lambda: self._traverse(1))
        self._view.bind(key_codes.EKeyRightArrow,lambda: self._traverse(0))
        
        self._width,self._height = self._img.size
        self._position = None

        self._axe_x = 0
        self._actual_pos = 0

        self._colorBack = colorBack
        self._colors = colors
        self._formatter = formatter
        self._data = data
        self._total = reduce(lambda x,y: x+y, data)
        
        self._setPosition()
        self._plot()
        



   ##Callback method for key events (navigates into the chart)
    def _traverse(self,code):
        #left
        if code:
            if self._actual_pos > 0:
                self._actual_pos -= 1
                self._plot()

        #right
        elif self._actual_pos < len(self._data)-1:
            self._actual_pos +=1
            self._plot()


    ##Handler for the painting the screen
     #@param self The object pointer.
     #@param rect the screen itself.
    def _OnUpdate(self,rect):
        self._view.blit(self._img)


   ##Defines the ranges of the graph in the screen
    def _setPosition(self):
        self._position = [10, self._height-30,self._width-10,10]



  #Plot the real graph.
    # @param self The object pointer.
    def _plot(self):
        pass

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


# barchart.py - Bars Chart Plotter for PyS60
# @version 0.1
# @date:  07/11/2008


class BarChart:

    #The default font for the texts
    FONT = font=('normal',10,graphics.FONT_BOLD)

   ##Creates a new instance of BarChart.
    # @param size  Chart's size (width,height)
    # @param yrange The list with y range [min_y,max_y,step_y]
    # @param data   Values of the data  [(subtitle,value)]
    # @param colors Color of the bars of the graph [color]
    # @param colorBack The background color
    # @param formatter The format of the series composed in the chart
    def __init__(self,size,yrange,data,colors,colorBack=(255,255,255),formatter=lambda x:x):
        
        self._img = graphics.Image.new(size)
        self._view = appuifw.Canvas(redraw_callback = self._OnUpdate)
        appuifw.app.body = self._view

        self._view.bind(key_codes.EKeyLeftArrow,lambda: self._traverse(1))
        self._view.bind(key_codes.EKeyRightArrow,lambda: self._traverse(0))
        
        self._width,self._height = self._img.size
        self._position = None
        self._min_y = None
        self._scale_y = None

        self._axe_x = 0
        self._actual_pos = 0

        self._yrange = yrange
        self._colorBack = colorBack
        self._colors = colors
        self._formatter = formatter
        self._data = data
        
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
        elif self._actual_pos < len(self._data)-1:
            self._actual_pos +=1
            self._set_axes()
            self._plot()

    ##Handler for the painting the screen
     #@param self The object pointer.
     #@param rect the screen itself.
    def _OnUpdate(self,rect):
        self._view.blit(self._img)


    ##Defines the ranges of the graph in the screen
    def _setPosition(self):
        left = self._view.measure_text(unicode(float(self._yrange[1])), font = self.__class__.FONT)[1]
        self._position = [left+2, self._height-30,self._width-10,10]

            
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

    #Plot chart axes.
    def _set_axes(self):
        #position: The position where the chart will be painted [left,bottom,right,top]
        left,bottom,right,top = self._position
        self._min_y,max_y,step_y = self._yrange
        self._scale_y = float(bottom - top)/(max_y-self._min_y)

        self._img.clear()
        self._img.rectangle([(left,top),(right+1,bottom+1)],0,fill = self._colorBack)

        #Plot y data set.    
        for y in self._arange(self._min_y,max_y,step_y):
            self._img.text((2,bottom+2-self._scale_y*(y-self._min_y)), unicode(self._formatter(y)), font= self.__class__.FONT)
            for i in range(left,right,3):            
                self._img.point((i,bottom-self._scale_y*(y-self._min_y)), 0)
                self._img.point((i+1,bottom-self._scale_y*(y-self._min_y)), 0)   
            self._img.point((left+1, bottom-self._scale_y*(y-self._min_y)), 0)
            self._img.point((right-1,bottom-self._scale_y*(y-self._min_y)), 0)



    #Plot the real graph.
    # @param self The object pointer.
    def _plot(self):
        left,bottom,right,top = self._position
        max_x = (len(self._data)) * 20
        scale_x = float(right - left)/ max_x
        index = 1
        data_index = 0
        self._axe_x = 0
        for x in self._arange(0,max_x,10):
            if index % 2 == 0:
                    if self._axe_x == self._actual_pos:
                        outline = (158,158,158)
                        tl = (left+ scale_x*(x)-30, top+7)
                        legend = unicode(self._data[self._actual_pos][0] + ": ") + unicode(self._formatter(self._data[self._actual_pos][1]))
                        bbox = self._view.measure_text(legend,font= self.__class__.FONT)[0]
                        t = (tl[0]-bbox[0],tl[1]-bbox[1])
                    else:
                        outline = self._colors[data_index]
                    x1 = left + scale_x * (x) - 17
                    x2 = left + scale_x * (x) + 17
                    y = bottom - self._scale_y * float(self._data[data_index][1]) 
                    self._img.rectangle([(x1,y),(x2,bottom+1)],outline, fill = self._colors[data_index])

                    if self._axe_x == self._actual_pos:
                        self._img.rectangle((t[0]+bbox[0]-4,t[1]+bbox[1]-4,t[0]+bbox[2]+4,t[1]+bbox[3]+4),outline=(0,0,0), fill = (255,255,255))
                        self._img.text((left+scale_x*(x)-30, top+15), legend, font= self.__class__.FONT)

                    data_index +=1
                    self._axe_x +=1        
            index += 1

        self._OnUpdate(None)     


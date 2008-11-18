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
import graphics, appuifw, key_codes, math


# piechart.py - Pie Chart Plotter for PyS60
# @version 0.2
# @date:  17/11/2008


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
        self._index = None

        self._axe_x = 0
        self._actual_pos = 0

        self._colorBack = colorBack
        self._colors = colors
        self._formatter = formatter
        self._data = data
        self._total = reduce(lambda x,y: x+y, map(lambda x: x[1], data))        
        self._setPosition()
        self._plot()
        

   ##Callback method for key events (navigates into the chart)
    def _traverse(self,code):
        #left
        if code:
            if self._actual_pos > 0:
                self._actual_pos -= 1
            else:
                self._actual_pos = len(self._data)-1
            self._plot()
             
        #right
        else:
            if self._actual_pos < len(self._data)-1:
                self._actual_pos +=1
            else:
                self._actual_pos = 0
            self._plot()


    ##Handler for the painting the screen
     #@param self The object pointer.
     #@param rect the screen itself.
    def _OnUpdate(self,rect):
        self._view.blit(self._img)


   ##Defines the ranges of the graph in the screen
    def _setPosition(self):
        l = map(lambda x: len(x[0]), self._data)
        self._index = l.index(max(l))
        box = self._view.measure_text(unicode(self._data[0][0]), font=('normal',15))[0]
        diff = box[1] - 25 
        self._position = [10, self._height+diff,self._width-10,10]
        


  #Plot the real graph. 
    # @param self The object  pointer.
    def _plot(self):
        left,bottom,right,top = self._position
        rate_conversion =  math.pi / 180.0
        self._axe_x = 0
        aux = 0.0
        color_index = 0

        self._img.clear()
        
        for (label,value) in self._data:

            if self._axe_x == self._actual_pos:
                outline = (158,158,158)
                _width = 4
                text = unicode(label + ": " + str(float(value)))
                tl = (right/3, bottom+10)
                bbox = self._view.measure_text(unicode(self._data[self._index][0] + ": " + str(float(self._data[self._index][1]))), font=('normal',15))[0]
                t = (tl[0]-bbox[0],tl[1]-bbox[1])
                #self._img.rectangle((t[0]+bbox[0]-4,t[1]+bbox[1]-4,t[0]+bbox[2]+4,t[1]+bbox[3]+4),outline=(0,0,0), fill = self._colors[color_index])
                self._img.text((t[0] + bbox[0], t[1]+bbox[1]+ 15), text, fill = self._colors[color_index], font= ('normal',15))
                #self._img.polygon(((50,25),(100,50),(100,0)),outline = 0xFFFF00)

            else:
                outline = self._colors[color_index]
                _width = 1
                
            calculo =  (float(value) / self._total) * 360
            calculo = math.ceil(calculo)
            if aux + calculo > 360:
                aux_end = 360
            else:
                aux_end =  aux + calculo
            self._img.pieslice([(left,top),(right,bottom)], aux*rate_conversion, aux_end * rate_conversion , outline, width = _width,  fill=self._colors[color_index])
            aux += calculo
            color_index +=1
            self._axe_x +=1
            self._OnUpdate(None)
            



        

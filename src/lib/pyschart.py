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


# linechart.py - Line Chart Plotter for PyS60
# @version 0.6
# @date:  06/11/2008

class LineChart:


    ##Creates a new instance of LineChart.
    # @param size  Chart's size (width,height)
    # @param xyrange The list with x and y range [min_x,max_x,step_x,min_y,max_y,step_y]
    # @param xs The list with values of data  x series
    # @param ys The list with the y series     
    # @param subtitle identification of the data set
    # @param legend labels of data
    # @param color The color of the line
    # @param colorBack The background color
    # @param formatter The format of the series composed in the chart
    def __init__(self,size,xyrange,xs,ys=None,subtitle="", legend = [], color = (255,0,0),
                  colorBack=(255,255,255),formatter=lambda x:x):

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
        self._subtitle = unicode(subtitle)
        self._legend = legend
        self._scale_y = None
        self._axe_x = 0
        self._actual_pos = 0
        self._xyrange = xyrange
        self._colorBack = colorBack
        self._color = color
        self._formatter = formatter
        self._xs = xs
        self._ys = ys
        
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
        
        
        for x in self._arange(self._min_x,max_x,step_x):         
            self._img.text((15+self._scale_x*(x-self._min_x), self._height-24), unicode(self._formatter(x)), font= ('normal',10,graphics.FONT_BOLD))
            for z in range(top,bottom,3):
                self._img.point((left+self._scale_x*(x-self._min_x),z),0)
                self._img.point((left+self._scale_x*(x-self._min_x),z+1),0)            
            self._img.point((left+self._scale_x*(x-self._min_x), bottom-1), 0)
            self._img.point((left+self._scale_x*(x-self._min_x), top+1), 0)

            
        for y in self._arange(self._min_y,max_y,step_y):
            self._img.text((2,bottom+2-self._scale_y*(y-self._min_y)), unicode(self._formatter(y)), font= ('normal',10,graphics.FONT_BOLD))
            for i in range(left,right,3):            
                self._img.point((i,bottom-self._scale_y*(y-self._min_y)), 0)
                self._img.point((i+1,bottom-self._scale_y*(y-self._min_y)), 0)   
            self._img.point((left+1, bottom-self._scale_y*(y-self._min_y)), 0)
            self._img.point((right-1,bottom-self._scale_y*(y-self._min_y)), 0)

        for x in self._xs:
            if self._axe_x == self._actual_pos:
                for z in range(top,bottom,3):
                    self._img.point((left+self._scale_x*(x-self._min_x),z), outline = self._color)
                    self._img.point((left+self._scale_x*(x-self._min_x),z+1), outline = self._color)            
                self._img.point((left+self._scale_x*(x-self._min_x), bottom-1), 0)
                self._img.point((left+self._scale_x*(x-self._min_x), top+1), 0)

                tl = (left+self._scale_x*(x-self._min_x)-5, top+7)
                if self._legend:
                    legend = unicode(self._legend[self._axe_x] + ": ") + unicode(self._formatter(x)) + "," + unicode(self._formatter(self._ys[self._actual_pos]))
                else:
                    legend = unicode(self._formatter(x)) + "," + unicode(self._formatter(self._ys[self._actual_pos]))
                bbox = self._view.measure_text(legend, font=('normal',10,graphics.FONT_BOLD))[0]
                t = (tl[0]-bbox[0],tl[1]-bbox[1])
                self._img.rectangle((t[0]+bbox[0]-4,t[1]+bbox[1]-4,t[0]+bbox[2]+4,t[1]+bbox[3]+4),outline=(0,0,0), fill = (255,255,255))
                self._img.text((left+self._scale_x*(x-self._min_x)-5, top+15), legend, font= ('normal',10,graphics.FONT_BOLD))
            self._axe_x +=1
        
       
            
            
    ## Plot the real graph
     #  @param self The object pointer.  
    def _plot(self):
        if self._ys == None:
            self._ys = self._xs
            self._xs = range(len(self._ys))
            
        left,bottom,right,top = self._position
        last = left + (self._xs[0] - self._min_x) * self._scale_x, bottom - (self._ys[0]-self._min_y) * self._scale_y    

        for i in range(1, len(self._ys)):
            p = left + (self._xs[i] - self._min_x) * self._scale_x, bottom - (self._ys[i]-self._min_y) * self._scale_y 
            self._img.line([last, p], self._color)
            last = p
        self._img.point(last,self._color)

        #The subtitle
        self._img.rectangle([(2,bottom+17),(15,self._height-4)],0,fill = self._color )
        self._img.text((17,self._height-5), self._subtitle, font= ('normal',13))
       
        self._OnUpdate(None)      

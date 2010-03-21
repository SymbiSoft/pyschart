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

"""  Mini application to test the charts.
     Author: Marcel P. Caraciolo    """
     
"""  Modified by Matovu Richard 	"""

from appuifw import *
import e32
from linechart import LineChart
from barchart import BarChart
from piechart import PieChart

def quit():
    print "Exit key pressed"
    app_lock.signal()
    
# @param size  		Chart's size (width,height)
# @param xyrange 		The list with x and y range [min_x,max_x,step_x,min_y,max_y,step_y]
# @param xyvalues 		The list with values of (x,y) data
# @param colors 		The list of colors for the lines of the data     
# @param legend 		The list of labels of data
# @param color 		The color of the line
# @param colorBack 	The background color
# @param xaxislabels 	The list of x-axis labels
# @param formatter 	The format of the series composed in the chart

def line_example01():
    dataset = [[(0, 32.5),(1, 45.0), (2, 90.0)],[(0,32.7),(1,67.5),(2.0,67.3),(3,100),(4,65)]]
    chart = LineChart(app.body.size,[0,5,1,0,125,25], dataset, [(255,140,0),(51,96,161),(114,171,242),(16,77,140),(250,210,125),(206,125,49)], legend=["Revenues", "Profits"], colorBack = (237,246,253), xaxislabels=["Jan","Feb","Mar","Apr","May","June"]) 

def line_example02():
    dataset = [[(0, 32.5),(1, 40.0), (2, 75.0),(3,60),(4,120)]]
    chart = LineChart(app.body.size,[0,5,1,0,125,25], dataset, [(114,171,242),(16,77,140),(250,210,125),(206,125,49)], legend=["Profits"], colorBack = (237,246,253), xaxislabels=["Jan","Feb","Mar","Apr","May","June"]) 

def pie_chart():
    chart = PieChart(app.body.size ,[("Brazil",50),("Germany",88), ("Italy",71), ("Argentina",45), ("Uruguay",22)], colors = [(0,255,0),(16,78,139),(205,127,50),(255,140,0), (255,0,0)], colorBack = (128,128,128))

def bars_chart():
    chart = BarChart(app.body.size,[0,90,22.5],[("Paraguay",30),("Brazil",60), ("Peru",20), ("Argentina",40), ("Venezuela", 70)], colors = [(255,0,0),(16,78,139),(205,127,50),(255,140,0), (0,0,0)], colorBack = (128,128,128))

canvas = Canvas()
app.body = canvas

app.menu=[ (u"Line Chart", line_example01),
		  (u"Pie Chart", pie_chart),
                  (u"Bar Chart", bars_chart),
                  (u"Line Chart", ((u"Example 01", line_example01),
                               (u"Example 02", line_example02)))]

app.exit_key_handler = quit
app_lock = e32.Ao_lock()
app_lock.wait()
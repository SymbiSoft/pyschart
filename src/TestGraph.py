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

"""  Mini application to test the charts.
     Author: Marcel P. Caraciolo    """




from appuifw import *
import e32
from pyschart import LineChart


def quit():
    print "Exit key pressed"
    app_lock.signal()

def line_example01():
    
    chart = LineChart(app.body.size,[0,125,25,0,90,22.5], [0.0,22.0,50.0,62.0,70.0,85.0],[0.0,25.0,50.0,30.0,20.0,80.0], subtitle="Producao", colorBack = (128,128,128))   
  

def line_example02():
    chart = LineChart(app.body.size,[0,125,25,0,125,25], [0.0,22.0,50.0,62.0,70.0,85.0],[0.0,25.0,50.0,30.0,20.0,80.0] , subtitle="Producao", legend = ["Jan","Feb","Mar","Apr","May","Jun"], colorBack = (128,128,128))  

def pizza_chart():
    pass


def columns_chart():
    pass


canvas = Canvas()
#app.screen = "full"
app.body = canvas

app.menu=[(u"Pizza Chart", pizza_chart),
                  (u"Columns Chart", columns_chart),
                  (u"Line Chart", ((u"Example 01", line_example01),
                               (u"Example 02", line_example02)))]

app.exit_key_handler = quit
app_lock = e32.Ao_lock()
app_lock.wait()





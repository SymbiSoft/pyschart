from appuifw import *
import e32
from pyschart import LineChart


def quit():
    print "Exit key pressed"
    app_lock.signal()


canvas = Canvas()
#app.screen = "full"
app.body = canvas
chart = LineChart(canvas,[0,50,10,0,125,25])   

    
app.exit_key_handler = quit
app_lock = e32.Ao_lock()
app_lock.wait()





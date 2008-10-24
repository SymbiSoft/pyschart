
class LineChart:   
    
    
    ## The constructor.
    #  @param xyrange: The list with x and y range [min_x,max_x,step_x,min_y,max_y,step_y]
    #  @param position: The position where the graph will be painted [left,bottom,right,top]
    #  @param color: The color used to fill the graph
    #  @param formater:  The format of the numbers composed in the graph
    
    def __init__(self,canvas,xyrange,color_rect,formatter):
        self._view = canvas
        self.width,self.height = self._view.size
        self.left = None
        self.right = None
        self.bottom = None
        self.top = None
        self.min_x = None
        self.min_y = None
        self.scale_x = None
        self.scale_y = None
        self.set_axes(xyrange,[26,self.height-19,self.width-10,10],color_rect,formatter)
    
    
     ## Iterator for generate random numbers
        #  @param self The object pointer.  
        #  @param start: The first number of the series
        #  @param stop: The last number of the series
        #  @param step:  The incrementator given
    def arange(self,start, stop=None, step=None):
        if stop is None:
            stop = float(start)
            start = 0.0
        if step is None:
            step = 1.0
        cur = float(start)
        while cur < stop:
            yield cur
            cur+= step
    
    
   
    
     ## Plot the real graph
        #  @param self The object pointer.  
        #  @param xs: The list with x series 
        #  @param ys: The list with the y series
        #  @param color: The color used to fill the line     
    def plot(self,xs,ys=None,color = 0x00000ff):
        if ys == None:
            ys = xs
            xs = range(len(ys))
        last = self.left+(xs[0]-self.min_x)*self.scale_x, self.bottom-(ys[0]-self.min_y)*self.scale_y
        for i in range(1, len(ys)):
            p = self.left + (xs[i]-self.min_x)*self.scale_x, self.bottom-(ys[i]-self.min_y)*self.scale_y
            self._view.line([last, p], color)
            last = p
        self._view.point(last,color)

      
x=        
//.idjsdksjdkjdksd




    private int width;
    private int heightTotal;
    private int heightGraph;
    private int total;
    
    private short[] data;
    private String idData;
    private int sizeFont;
    
    private Font font;
    
    public final static byte RED = 0;
    public final static byte LIME = 1;
    public final static byte BLUE = 2;
    public final static byte YELLOW = 3;
    public final static byte AQUA = 4;
    public final static byte FUCHSIA = 5;
    public final static byte WHITE = 6;
    public final static byte BLACK = 7;
    public final static byte MAROON = 8;
    public final static byte GREEN = 9;
    public final static byte NAVY = 10;
    public final static byte OLIVE = 11;
    public final static byte TEAL = 12;
    public final static byte PURPLE = 13;
    public final static byte SILVER = 14;
    public final static byte GRAY = 15;
    
    private int colorHexaBack;
    private int colorHexaLine;
    
    //representa o valor máximo, de posso deste valor, podemos fazer uma escala vertical do gráfico
    private short maxValue;
    
    //número de linhas horizontais
    private short nHorLines;
    private boolean horLines;
    
    private Font minorFont;
    
    private String[] legend;
    
    private short indVerticalBar;
    
    /**
     * Creates a new instance of PieChart.
     * @param width - width of chart
     * @param height - height of chart
     * @param data - values of data
     * @param legend - labels of data
     * @param idData - identification of the data set
     * @param sizeFont - size of fonte of text
     * @param colorLine - color of line
     * @param colorBack - color of background
     * @param maxValue - bigger value of the data set
     */
    public LineChart(int width, int height, short[] data, String[] legend, String idData, int sizeFont, byte colorLine, 
            byte colorBack, short maxValue) {
        super("");
        
        this.width = width;  
        this.data = data;  
        this.idData = idData;
        this.sizeFont = sizeFont; 
        this.total = total;
        
        switch (colorLine)
        {
            case RED:
                colorHexaLine = 0xff0000;
                break;
            case LIME:
                colorHexaLine = 0x00ff00;
                break;
            case BLUE:
                colorHexaLine = 0x0000ff;
                break;
            case YELLOW:
                colorHexaLine = 0xffff00;
                break;
            case AQUA:
                colorHexaLine = 0x00ffff;
                break;
            case FUCHSIA:
                colorHexaLine = 0xff00ff;
                break;
            case WHITE:
                colorHexaLine = 0xffffff;
                break;
            case BLACK:
                colorHexaLine = 0x000000;
                break;
            case MAROON:
                colorHexaLine = 0x800000;
                break;
            case GREEN:
                colorHexaLine = 0x008000;
                break;
            case NAVY:
                colorHexaLine = 0x000080;
                break;
            case OLIVE:
                colorHexaLine = 0x808000;
                break;
            case TEAL:
                colorHexaLine = 0x008080;
                break;
            case PURPLE:
                colorHexaLine = 0x800080;
                break;
            case SILVER:
                colorHexaLine = 0xc0c0c0;
                break;
            case GRAY:
                colorHexaLine = 0x808080;
        }
        
        switch (colorBack)
        {
            case RED:
                colorHexaBack = 0xff0000;
                break;
            case LIME:
                colorHexaBack = 0x00ff00;
                break;
            case BLUE:
                colorHexaBack = 0x0000ff;
                break;
            case YELLOW:
                colorHexaBack = 0xffff00;
                break;
            case AQUA:
                colorHexaBack = 0x00ffff;
                break;
            case FUCHSIA:
                colorHexaBack = 0xff00ff;
                break;
            case WHITE:
                colorHexaBack = 0xffffff;
                break;
            case BLACK:
                colorHexaBack = 0x000000;
                break;
            case MAROON:
                colorHexaBack = 0x800000;
                break;
            case GREEN:
                colorHexaBack = 0x008000;
                break;
            case NAVY:
                colorHexaBack = 0x000080;
                break;
            case OLIVE:
                colorHexaBack = 0x808000;
                break;
            case TEAL:
                colorHexaBack = 0x008080;
                break;
            case PURPLE:
                colorHexaBack = 0x800080;
                break;
            case SILVER:
                colorHexaBack = 0xc0c0c0;
                break;
            case GRAY:
                colorHexaBack = 0x808080;
        }
        
        this.maxValue = maxValue;
        this.legend = legend;
        
        nHorLines = 4;
        horLines = true;
        
        indVerticalBar = 0;
        
        font = Font.getFont(Font.FACE_MONOSPACE, Font.STYLE_PLAIN, Font.SIZE_SMALL);  
        this.heightGraph = height;
        
        minorFont = Font.getFont(Font.FACE_MONOSPACE, Font.STYLE_PLAIN, Font.SIZE_SMALL);  
        this.heightTotal = height+(font.getHeight())+3+minorFont.getHeight();
    }

    /**
     * Implemented by the subclass of CustomItem to return the minimum width of the content area, in pixels. This method is called by the implementation as part of its layout algorithm. The actual width granted is reported in the sizeChanged and paint methods.
     * @return the minimum content width in pixels
     */
    protected int getMinContentWidth() {
        return width;
    }

    /**
     * Implemented by the subclass of CustomItem to return the minimum height of the content area, in pixels. This method is called by the implementation as part of its layout algorithm. The actual height granted is reported in the sizeChanged and paint methods.
     * @return the minimum content height in pixels
     */
    protected int getMinContentHeight() {
        return heightTotal;
    }

    /**
     * Implemented by the subclass of CustomItem to return the preferred width of the content area, in pixels. This method is called by the implementation as part of its layout algorithm.
     * The height parameter is the tentative height assigned to the content area. The subclass code may use this value in its computation of the preferred width. The height parameter will be -1 if the implementation has not assigned a tentative value for the height. Otherwise, height will have a specific value if the application has locked the height of the CustomItem or if the container's layout algorithm has already computed a tentative height at the time of this call. The subclass must not assume that the tentative height passed or the preferred width returned will be granted. The actual size granted is reported in the sizeChanged and paint methods. <p>
     * @param height - the tentative content height in pixels, or -1 if a tentative height has not been computed
     * @return the preferred content width in pixels
     */
    protected int getPrefContentWidth(int i) {
        return width;
    }

    /**
     * Implemented by the subclass of CustomItem to return the preferred height of the content area, in pixels. This method is called by the implementation as part of its layout algorithm.
     * The width parameter is the tentative width assigned to the content area. The subclass code may use this value in its computation of the preferred height. The width parameter will be -1 if the implementation has not assigned a tentative value for the width. Otherwise, width will have a specific value if the application has locked the width of the CustomItem or if the container's layout algorithm has already computed a tentative width at the time of this call. The subclass must not assume that the tentative width passed or the preferred height returned will be granted. The actual size granted is reported in the sizeChanged and paint methods.<p>
     * @param width - the tentative content width in pixels, or -1 if a tentative width has not been computed
     * @return the preferred content height in pixels
     */
    protected int getPrefContentHeight(int i) {
        return heightTotal;
    }

    /**
     * Implemented by the subclass of CustomItem to render the item within its container. At the time of the call, the Graphics context's destination is the content area of this CustomItem  (or back buffer for it). The Translation is set so that the upper left corner of the content area is at (0,0), and the clip is set to the area to be painted. The application must paint every pixel within the given clip area. The item is allowed to modify the clip area, but the system must not allow any modification to result in drawing outside the bounds of the item's content area. The w and h passed in are the width and height of the content area of the item. These values will always be equal to the values passed with the most recent call to sizeChanged(); they are passed here as well for convenience.
     * @param g - the Graphics object to be used for rendering the item
     * @param w - current width of the item in pixels
     * @param h - current height of the item in pixels
     */
    protected void paint(Graphics g, int w, int h) {
        float aux = minorFont.stringWidth("99,9");
        float aux2 = aux;
        float aux3;
        float calculo = 0;
        
        int comGra = minorFont.getHeight()/2;
      
        g.setColor(colorHexaBack);
        g.fillRect(minorFont.stringWidth("99,9"), comGra, (int)(width-(9+aux)), heightGraph);
        
        g.setColor(0, 0, 0);
        g.drawRect(minorFont.stringWidth("99,9"), comGra, width-(9+minorFont.stringWidth("99,9")), heightGraph);
        
        float pontos = ((float)(width-(9+aux))/(data.length-1));
        
        pontos = (float)Math.ceil(pontos);
        
        g.setFont(font);
        
        g.setColor(0, 0 ,0);
        aux2 = (float)((float)maxValue/(float)nHorLines);
        aux3 = (float)((float)heightGraph/(float)nHorLines);
        
        g.drawString(""+maxValue, 0, 0, Graphics.LEFT|Graphics.TOP);
        for (int l = nHorLines-1, m = 1; l != 0; l--, m++)
        {
            g.drawString(new String(""+(float)(aux2*l)).substring(0, 4), 0, (int)(aux3*m)-minorFont.getHeight()/2+comGra, Graphics.LEFT|Graphics.TOP);
        }
        g.drawString("0", 0, heightGraph, Graphics.LEFT|Graphics.TOP);
        
        g.setColor(0, 0, 0);
        g.drawRect(0, heightTotal-font.getHeight()+1, 10, font.getHeight()-2);
        g.drawString(idData, 14, heightTotal-font.getHeight(), Graphics.LEFT|Graphics.TOP);
        g.setColor(colorHexaLine);
        g.fillRect(0, heightTotal-font.getHeight()+1, 10, font.getHeight()-2);
        g.setColor(0, 0, 0);
        
        if (horLines)
        {
            aux2 = heightGraph/nHorLines;
            
            g.setStrokeStyle(Graphics.DOTTED);
            for (int l = nHorLines-1; l != 0; l--)
            {
                g.drawLine(minorFont.stringWidth("99,9"), (int)(aux2*l)+comGra, width-9, (int)(aux2*l)+comGra);
            }
        }
        
        for (int j = 1; j < data.length; j++)
        {    
            if (indVerticalBar == j)
                g.setColor(colorHexaLine);
            else
                g.setColor(0, 0, 0);
            
            g.setStrokeStyle(Graphics.DOTTED);
            g.drawLine(((int)(j*pontos))+minorFont.stringWidth("99,9"), heightGraph+comGra, ((int)(j*pontos))+minorFont.stringWidth("99,9"), comGra);
            g.setStrokeStyle(Graphics.SOLID);
            
            if (indVerticalBar == j)
            {
                g.setColor(255, 255, 255);
                g.fillRect((((int)(j*pontos))+minorFont.stringWidth("99,9"))-2-((minorFont.stringWidth(legend[0]+": "+data[0]))/2), comGra+2, minorFont.stringWidth(legend[0]+": "+data[0])+4, minorFont.getHeight());
                g.setColor(0, 0, 0);
                g.drawRect((((int)(j*pontos))+minorFont.stringWidth("99,9"))-2-((minorFont.stringWidth(legend[0]+": "+data[0]))/2), comGra+2, minorFont.stringWidth(legend[0]+": "+data[0])+4, minorFont.getHeight());
                g.drawString(legend[j]+": "+data[j], ((int)(j*pontos))+minorFont.stringWidth("99,9"), comGra+2, Graphics.HCENTER|Graphics.TOP);
            }
        }
        
        if (indVerticalBar == 0)
        {
            g.setColor(colorHexaLine);
            g.drawLine(minorFont.stringWidth("99,9"), heightGraph+comGra, minorFont.stringWidth("99,9"), comGra);
            
            g.setColor(255, 255, 255);
            g.fillRect(minorFont.stringWidth("99,9")+2, comGra+2, minorFont.stringWidth(legend[0]+": "+data[0])+4, minorFont.getHeight());
            g.setColor(0, 0, 0);
            g.drawRect(minorFont.stringWidth("99,9")+2, comGra+2, minorFont.stringWidth(legend[0]+": "+data[0])+4, minorFont.getHeight());
            g.drawString(legend[0]+": "+data[0], minorFont.stringWidth("99,9")+4, comGra+2, Graphics.LEFT|Graphics.TOP);
        }
        else if (indVerticalBar == data.length-1)
        {
            g.setColor(colorHexaLine);
            g.drawLine(width-9, heightGraph+comGra, width-9, comGra);
            
            g.setColor(255, 255, 255);
            g.fillRect(width-15-(minorFont.stringWidth(legend[0]+": "+data[0])), comGra+2, minorFont.stringWidth(legend[0]+": "+data[0])+4, minorFont.getHeight());
            g.setColor(0, 0, 0);
            g.drawRect(width-15-(minorFont.stringWidth(legend[0]+": "+data[0])), comGra+2, minorFont.stringWidth(legend[0]+": "+data[0])+4, minorFont.getHeight());
            g.drawString(legend[data.length-1]+": "+data[data.length-1], width-13, comGra+2, Graphics.RIGHT|Graphics.TOP);
        }
        
        g.setColor(colorHexaLine);
        
        float backup = heightGraph;
        
        calculo = (Float.parseFloat(""+data[0]))*((float)((float)heightGraph/(float)maxValue));
        calculo = (float)Math.ceil(calculo);
        calculo = heightGraph-(int)calculo;
        backup = calculo+comGra;
        
        for (int j = 1; j < data.length; j++)
        {
            calculo = (Float.parseFloat(""+data[j]))*((float)((float)heightGraph/(float)maxValue));
            calculo = (float)Math.ceil(calculo);
            calculo = heightGraph-(int)calculo+comGra;
            g.drawLine((int)aux, (int)backup, (int)(aux+pontos), (int)calculo);
            
            backup = calculo;
            aux += pontos;
        }
    }
    
    /**
     * Called by the system when traversal has entered the item or has occurred within the item. The direction of traversal and the item's visible rectangle are passed into the method. The method must do one of the following: it must either update its state information pertaining to its internal traversal location, set the return rectangle to indicate a region associated with this location, and return true; or, it must return false to indicate that this item does not support internal traversal, or that that internal traversal has reached the edge of the item and that traversal should proceed to the next item if possible.<p>
     * The implementation indicates support for internal traversal within a CustomItem by setting one or both of the TRAVERSE_HORIZONTAL or TRAVERSE_VERTICAL bits in the value returned by the getInteractionModes method. The dir parameter indicates the direction of traversal by using Canvas game actions Canvas.UP, Canvas.DOWN, Canvas.LEFT, and Canvas.RIGHT, or the value NONE, which indicates that there is no specific direction associated with this traversal event. If the TRAVERSE_HORIZONTAL bit is set, this indicates that the Canvas.LEFT and Canvas.RIGHT values will be used to indicate the traversal direction. If the TRAVERSE_VERTICAL bit is set, this indicates that the Canvas.UP and Canvas.DOWN values will be used to indicate the traversal direction. If both bits are set, all four direction values may be used for the traversal direction, indicating that the item should perform two-dimensional traversal. The dir parameter may have the value NONE under any combination of the TRAVERSE_VERTICAL and TRAVERSE_HORIZONTAL bits.<p>
     * Although Canvas game actions are used to indicate the traversal direction, this does not imply that the keys mapped to these game actions are being used for traversal, nor that that keys are being used for traversal at all.<p>
     * The viewportWidth and viewportHeight parameters indicate the size of the viewable area the item's container has granted to its items. This represents the largest area of the item that is likely to be visible at any given time.<p>
     * The visRect_inout parameter is used both for passing information into this method and for returning information from this method. It must be an int[4] array. The information in this array is a rectangle of the form [x,y,w,h] where (x,y) is the location of the upper-left corner of the rectangle relative to the item's origin, and (w,h) are the width and height of the rectangle. The return values placed into this array are significant only when the traverse() method returns true. The values are ignored if the traverse() method returns false.<p>
     * When this method is called, the visRect_inout array contains a rectangle representing the region of the item that is currently visible. This region might have zero area if no part of the item is visible, for example, if it is scrolled offscreen. The semantics of the rectangle returned are discussed below.<p>
     * The CustomItem must maintain state that tracks whether traversal is within this item, and if it is, it must also record the current internal location. Initially, traversal is outside the item. The first call to the traverse() method indicates that traversal has entered the item. Subsequent calls to this method indicate that traversal is occurring within this item. Traversal remains within the item until the traverseOut method is called. The CustomItem must keep track of its traversal state so that it can distinguish traversal entering the item from traversal within the item.<p>
     * When traversal enters the item, the traversal code should initialize its internal traversal location to the "first" location appropriate for the item's structure and the traversal direction. As an example of the latter policy, if the traversal direction is DOWN, the initial location should be the topmost internal element of the item. Similarly, if the traversal direction is UP, the initial location should be the bottommost element of the item. The CustomItem should still choose the "first" location appropriately even if its primary axis is orthogonal to the axis of traversal. For example, suppose the traversal mode supported is TRAVERSE_VERTICAL but the CustomItem is structured as a horizontal row of elements. If the initial traversal direction is DOWN, the initial location might be the leftmost element, and if the initial traversal direction is UP, the initial location might be the rightmost element.<p>
     * Traversal may enter the item without any specific direction, in which case the traversal direction will be NONE. This may occur if the user selects the item directly (e.g., with a pointing device), or if the item gains the focus because its containing Form has become current. The CustomItem should choose a default traversal location. If the CustomItem had been traversed to previously, and if it is appropriate for the user interface of the CustomItem, the previous traversal location should be restored.<p>
     * When traversal occurs within the item, the internal traversal location must be moved to the next appropriate region in the direction of traversal. The item must report its updated internal traversal location in the visRect_inout return parameter as described below and return true. The item will typically provide a highlight to display the internal traversal location to the user. Thus, the item will typically also request repaints of the old and new traversal locations after each traversal event. There is no requirement that the area the item requests to be repainted is the same as the area returned in the visRect_inout rectangle. The system will combine any repaint requests with any additional repainting that may occur as a result of scrolling.<p>
     * The traverse() method may be called with a direction of NONE when the traversal is already within the CustomItem. This will occur in response to the CustomItem subclass code having called the invalidate() method. In this case, the CustomItem should simply return its current notion of the traversal location. This mechanism is useful if the CustomItem needs to update the traversal location spontaneously (that is, not in response to a traversal event), for example, because of a change in its contents.<p>
     * If the internal traversal location is such that the traversal event would logically cause traversal to proceed out of the item, the item should return false from the traverse() method. For example, if the current traversal location is the bottommost internal element of the item, and the traversal direction is DOWN, the traverse() method should simply return false. In this case the method need not update the values in the visRect_inout array. The item must leave its internal traversal location unchanged, and it should not request a repaint to update its highlighting. It should defer these actions until the traverseOut() method is called. The system will call the traverseOut() method when traversal actually leaves the item. The system might not call the traverseOut() method, even if traverse() has returned false, if this item is at the edge of the Form or there is no other item beyond to accept the traversal. Even if the traverse() method returns false, the traversal location is still within this item. It remains within this item until traverseOut() is called.<p>
     * Note the subtle distinction here between the initial traverse() call signifying entry into the item and subsequent calls signifying traversal within the item. A return value of false to the initial call indicates that this item performs no internal traversal at all, whereas a return of false to subsequent calls indicates that traversal is within this item and may now exit.<p>
     * The width and height of the rectangle returned in the visRect_inout array are used by the Form for scrolling and painting purposes. The Form must always position the item so that the upper left corner of this rectangle, as specified by the (x,y) position, is visible. In addition, the item may also specify a width and height, in which case the Form will attempt to position the item so that as much of this rectangle as possible is visible. If the width and height are larger than the size of the viewport, the bottom and right portions of this rectangle will most likely not be visible to the user. The rectangle thus returned will typically denote the size and location of one of the item's internal elements, and it will also typically (though not necessarily) correspond to where the element's highlight will be painted. Width and height values of zero are legal and are not treated specially. Negative values of width and height are treated as if they were zero.<p>
     * There is no requirement on the location of the rectangle returned in the visRect_inout array with respect to the traversal direction. For example, if the CustomItem implements internal scrolling, a traversal direction of DOWN may cause the item's contents to scroll upwards far enough so that the rectangle returned may be above its old location. CustomItem subclasses must ensure that continued traversal in one direction will eventually reach the edge of the item and then traverse out by returning false from this method. CustomItems must not implement "wraparound" behavior (for example, traversing downwards from the bottommost element moves the traversal location to the topmost element) because this will trap the traversal within the item.<p>
     * If the CustomItem consists of internal elements that are smaller than the container's viewport, the rectangle returned should be the same size as one of these elements. However, the CustomItem might have contents whose elements are larger than the viewport, or it might have contents having no internal structure. In either of these cases, the item should return a rectangle that best represents its idea of the content area that is important for the user to see. When traversal occurs, the item should move its traversal location by an amount based on the viewport size. For example, if the viewport is 80 pixels high, and traversal occurs downwards, the item might move its traversal location down by 70 pixels in order to display the next screenful of content, with 10 pixels overlap for context.<p>
     * All internal traversal locations must be reachable regardless of which traversal modes are provided by the implementation. This implies that, if the implementation provides one-dimensional traversal, the CustomItem must linearize its internal locations. For example, suppose the traversal mode is TRAVERSE_VERTICAL and the CustomItem consists of a horizontal row of elements. If the traversal direction is DOWN the internal traversal location should move to the right, and if the traversal direction is UP the internal traversal location should move to the left. (The foregoing convention is appropriate for languages that use left-to-right text. The opposite convention should be used for languages that use right-to-left text.) Consider a similar example where the traversal mode is TRAVERSE_VERTICAL and the CustomItem consists of a grid of elements. A traversal direction of DOWN might proceed leftwards across each row, moving to the next row downwards when the location reaches the rightmost element in a row.<p>
     * If the implementation provides two-dimensional traversal but the CustomItem is one-dimensional, a traversal direction along the item's axis should traverse within the item, and a traversal direction orthogonal to the item's axis should cause immediate traversal out of the item by returning false from this method. For example, suppose a CustomItem is implementing a vertical stack of elements and traversal is already inside the item. If a traverse event is received with direction UP or DOWN, the traverse() method should move to the next element and return true. On the other hand, if a traverse event is received with direction RIGHT or LEFT, the traverse() method should always return false so that traversal exits the item immediately. An item that implements internal traversal should always accept entry - that is, the initial call to traverse() should return true - regardless of the axis of the traversal direction.<p>
     * If the traverse() method returns false when traversal is entering the item, this indicates to the system that the item does not support internal traversal. In this case, the item should not perform any of its own highlighting, and the system will perform highlighting appropriate for the platform, external to the item.<p>
     * The default implementation of the traverse() method always returns false.
     * @param dir - the direction of traversal, one of Canvas.UP, Canvas.DOWN, Canvas.LEFT, Canvas.RIGHT, or NONE.
     * @param viewportWidth - the width of the container's viewport
     * @param viewportHeight - the height of the container's viewport
     * @param visRect_inout - passes the visible rectangle into the method, and returns the updated traversal rectangle from the method
     */
    protected boolean traverse(int dir, int viewportWidth, int viewportHeight, int[] visRect_inout) {
        switch (dir)
        {
            case Canvas.LEFT:
                if (indVerticalBar > 0)
                {
                    indVerticalBar--;
                    repaint();

                    return true;
                }
                else
                {
                    return false;
                }
            case Canvas.RIGHT:
                if (indVerticalBar < data.length-1)
                {
                    indVerticalBar++;
                    repaint();

                    return true;
                }
                else
                {
                    return false;
                }
            case NONE:
                return true;
        }
        
        return false;
    }
    
}

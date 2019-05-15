import wx
import matplotlib
#from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import csvdata

class TopPanel(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self, parent=parent)
        wx.Button(self, -1, "Billy", size=(50,-1))
        self.SetBackgroundColour("pink")


class BottomPanel(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self, parent=parent)
        self.togglebuttomStart=wx.ToggleButton(self,id=-1, label="Show the chart", pos=(10,90))
        self.togglebuttomStart.Bind(wx.EVT_TOGGLEBUTTON,self.OnStartClick)
        self.togglebuttomStart.SetBackgroundColour("red")

        labelwriteurl= wx.StaticText(self,-1,"Write URL", pos=(10,10))
        self.textboxTheurl=wx.TextCtrl(self,-1,"https://www.ssb.no/eksport/tabell.csv?key=372475", size=(380,-1), pos=(10,30))

    def OnStartClick(self,event):
        val=self.togglebuttomStart.GetValue()
        if val==True:
            self.togglebuttomStart.SetLabel("Done")
            csvdata.plotmaking(self.textboxTheurl.GetValue())
        else:
            self.togglebuttomStart.SetLabel("Show the chart")

class Main(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,parent=None, title="Income Comparation",size=(450,400))
        splitter=wx.SplitterWindow(self)
        top=TopPanel(splitter)
        bottom=BottomPanel(splitter)
        splitter.SplitHorizontally(top,bottom)
        splitter.SetMinimumPaneSize(100)



if __name__=="__main__":
    app=wx.App()
    frame= Main()
    frame.Show()
    app.MainLoop()
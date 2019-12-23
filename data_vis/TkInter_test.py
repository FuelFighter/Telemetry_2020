import os
import wx
import webbrowser

class MyApp(wx.App):
    def __init__(self):
        super().__init__(clearSigInt=True)

        self.InitFrame()

    def InitFrame(self):
        frame = MyFrame(parent=None, title="Telemetry Data Vis", pos=(50,50), size=(720,480))
        frame.Show()


class MyFrame(wx.Frame):
    def __init__(self, parent, title, pos, size):
        super().__init__(parent=parent, title=title, pos=pos, size=size)
        self.OnInit()

    def OnInit(self):
        panel = MyPanel(parent=self)

class MyPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent=parent)

        welcomeText = wx.StaticText(self, id=wx.ID_ANY, label="Blæ", pos=(20,20))
        
        button = wx.Button(parent=self, label="Click here", pos=(20, 80))
        button.Bind(event=wx.EVT_BUTTON, handler=self.OnSubmit)

    def OnSubmit(self, event):
        webbrowser.open('https://www.google.com')

if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()



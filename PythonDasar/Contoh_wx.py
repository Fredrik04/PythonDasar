import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(300, 200))
        
        panel = wx.Panel(self)
        button = wx.Button(panel, label="Klik Saya", pos=(100, 50))
        button.Bind(wx.EVT_BUTTON, self.on_button_click)
        
    def on_button_click(self, event):
        print("Tombol diklik")

app = wx.App()
frame = MyFrame(None, "Contoh Program wxPython")
frame.Show()
app.MainLoop()

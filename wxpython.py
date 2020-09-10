"""
import tkinter
import turtle
root = tkinter.Tk()
label = tkinter.Label(root, text = 'ind9X')
label.pack()
button1 = tkinter.Button(root, text = '五角星')
button1.pack()
def wjx(event):
    for i in range(5):
        turtle.forward(200)
        turtle.right(144)

button1.bind('<Button-1>', wjx)
root.mainloop()
"""
"""
import wx
app = wx.App()
frame = wx.Frame(parent = None)
frame.Show()
app.MainLoop()
"""
"""
import wx
class MyApp(wx.App):
    def OnInit(self):
        Frame = wx.Frame(parent = None)
        Frame.Show()
        return True
app = MyApp()
app.MainLoop()
"""
import wx
import time

class LanChat(wx.App):
    def OnInit(self):
        ChatFrame = wx.Frame(parent = None, title = 'LanChat', size = (500,600), pos = (300,100))
        panel = wx.Panel(ChatFrame, -1)
        Label_Msg = wx.StaticText(panel, -1, "聊天信息", (0,0), (485,20), wx.ALIGN_CENTER)
        Label_Msg.SetForegroundColour('red')
        self.Msg = wx.TextCtrl(panel, -1, size = (446,300), pos = (19,20), style = wx.TE_READONLY|wx.TE_MULTILINE)
        Label_Input = wx.StaticText(panel, -1, "输入框", (0,320), (485,20), wx.ALIGN_CENTER)
        Label_Input.SetForegroundColour('red')
        self.Input = wx.TextCtrl(panel, -1, size = (446,170), pos = (19,340), style = wx.TE_MULTILINE)
        self.ButtonSet = wx.Button(panel, -1, "发送", size=(75,25), pos=(112,520))
        self.Bind(wx.EVT_BUTTON, self.OnButtonSent, self.ButtonSet)
        self.ButtonClear = wx.Button(panel, -1, "清空", size=(75,25), pos=(299,520))
        self.Bind(wx.EVT_BUTTON, self.OnButtonClear, self.ButtonClear)
        ChatFrame.Show()
        return True
    
    def OnButtonSent(self, event):
        UserInput = self.Input.GetValue()
        self.Input.Clear()
        NowTime = time.ctime()
        InMsg = "You said (%s) :\n%s \n" % (NowTime,UserInput)
        self.Msg.AppendText(InMsg)
        
    def OnButtonClear(self, event):
        self.Msg.Clear()

if __name__ == '__main__':
    app = LanChat()
    app.MainLoop()
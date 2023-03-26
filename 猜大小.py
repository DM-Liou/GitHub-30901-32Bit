# -*- coding:utf-8 -*-
import random, wx

class Game(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="猜數字", size=(270,200))
        panel = wx.Panel(self)

        # 配置視窗元件
        wx.StaticText(parent=panel, label="請猜1-100的數字", pos=(10,10))
        self.answer = wx.TextCtrl(parent=panel, pos=(120,10))
        self.btn = wx.Button(parent=panel, label="大或小", pos=(120,50))
        self.message = wx.StaticText(parent=panel,pos=(10,100))

        # 新增 BtnCheck 事件
        self.Bind(wx.EVT_BUTTON, self.BtnCheck, self.btn)


        # 配置選單元件
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        fitem = fileMenu.Append(wx.ID_EXIT, '結束', '結束軟體')
        menubar.Append(fileMenu, '&檔案')
        self.SetMenuBar(menubar)
        
        # 新增 MenuQuit 事件
        self.Bind(wx.EVT_MENU, self.MenuQuit, fitem)


    # 撰寫 BtnCheck 事件函式
    def BtnCheck(self, event):
        answer = eval(self.answer.GetValue())

        if answer > num:
            messageStr ="太大了"
        elif answer < num:
            messageStr = "太小了"
        else:
            messageStr = "猜中了"

        self.message.SetLabel(messageStr)

    # 撰寫 MenuQuit 事件函式
    def MenuQuit(self, e):
        self.Close()


if __name__ == '__main__':
    num = random.randint(1, 100)
    answer = -1

    app = wx.App()
    frame = Game()
    frame.Show()
    
    app.MainLoop()
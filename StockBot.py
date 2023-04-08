
# -*- coding: utf-8 -*-
import wx
import time
#  import wx, time
import wx.grid
import wx.lib.anchors as anchors
from ctypes import byref, POINTER, windll
from comtypes import IUnknown, GUID
from comtypes.client import GetModule,  GetBestInterface, GetEvents
import queue as queue
# ---------------------------------------------------
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


cls()
# ----------------------------------------------------

user32 = windll.user32
atl = windll.atl
q = queue.Queue()


#class StockBot:

    #def __init__(self, botuid):
        #self.Yuanta = YuantaQuoteWapper(botuid, self)

    #def login(self, account, password):
    

        # -----------------------------------------------------------------------------------------------------------
print('6-1.START Login   class StockBot: /def login(self,account,password) ')
        # T port 80/443 , T+1 port 82/442 ,  reqType=1 T盤 , reqType=2  T+1盤
Yuanta.YuantaQuote.SetMktLogon(
    'E123632952', '3359ldmYY', 'apiquote.yuantafutures.com.tw', '80', 1, 0)  # 正式環境
        #self.Yuanta.YuantaQuote.SetMktLogon(account, password, 'apiquote.yuantafutures.com.tw', '82', 2, 0)
print('6-1.END.  Login   class StockBot: /def login(self,account,password)')
print('login')
        # -----------------------------------------------------------------------------------------------------------


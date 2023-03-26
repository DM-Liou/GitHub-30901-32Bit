# -*- coding: utf-8 -*-
# https://gist.github.com/kwedr/134e27c61405acdb5bed4b3a2dfed2c1

# 一開始使用 comtypes, pythonnet, win32com 都無法使用後來看到
# http://kwedr.blogspot.com/2018/11/api-with-python.html

# [一]Python通過ActiveX容器嵌入flash
# https://www.twblogs.net/a/5e51c222bd9eee21168043d1




#import queue as queue
import queue
import wx
import time
import wx.lib.anchors as anchors
from ctypes import byref, POINTER, windll
from comtypes import IUnknown, GUID
from comtypes.client import GetModule,  GetBestInterface, GetEvents

user32 = windll.user32
atl = windll.atl

q = queue.Queue()


class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration

    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args:  # changed for v1.5, see below
            self.fall = True
            return True
        else:
            return False


class Job:
    STOCK_LOGIN = 1
    STOCK_WATCH = 2

    def __init__(self, do_type, do_value=0):
        self.do_type = do_type
        self.do_value = do_value
        q.put(self)


def DoJob(Bot, x):
    print('def DoJob(Bot, x): test OK1')
    for case in switch(x.do_type):
        print('def DoJob(Bot, x): test OK2')
        if case(Job.STOCK_LOGIN):
            print('def DoJob(Bot, x): test OK3-1')
            Bot.login()    ################################### error
            print('def DoJob(Bot, x): test OK3-2')
            break
        if case(Job.STOCK_WATCH):
            print('def DoJob(Bot, x): test OK4-1')
            Bot.watch(x.do_value)
            print('def DoJob(Bot, x): test OK4-2')
            break

    print('def DoJob(Bot, x): test END OK')

class YuantaQuoteEvents(object):
    def __init__(self, parent):
        self.parent = parent

    def OnMktStatusChange(self, this, Status, Msg, ReqType):
        print('OnMktStatusChange {},{},{}'.format(ReqType, Msg, Status))
        if Status == 2:
            Job(Job.STOCK_WATCH, ReqType)

    def OnRegError(self, this, symbol, updmode, ErrCode, ReqType):
        print('OnRegError {},{},{},{}'.format(
            ReqType, ErrCode, symbol, updmode))

    def OnGetMktData(self, this, PriType, symbol, Qty, Pri, ReqType):
        print('OnGetMktData')

    def OnGetMktQuote(self, this, symbol, DisClosure, Duration, ReqType):
        print('OnGetMktQuote')

    def OnGetMktAll(self, this, symbol, RefPri, OpenPri, HighPri, LowPri, UpPri, DnPri, MatchTime, MatchPri, MatchQty, TolMatchQty,
                    BestBuyQty, BestBuyPri, BestSellQty, BestSellPri, FDBPri, FDBQty, FDSPri, FDSQty, ReqType):
        # print ('OnGetMktAll\n')
        print('{} {} c:{} o:{} h:{} l:{} v:{}'.format(
            ReqType, MatchTime,  MatchPri, OpenPri, HighPri, LowPri, TolMatchQty))

    def OnGetDelayClose(self, this, symbol, DelayClose, ReqType):
        print('OnGetDelayClose')

    def OnGetBreakResume(self, this, symbol, BreakTime, ResumeTime, ReqType):
        print('OnGetBreakResume')

    def OnGetTradeStatus(self, this, symbol, TradeStatus, ReqType):
        print('OnGetTradeStatus')

    def OnTickRegError(self, this, strSymbol, lMode, lErrCode, ReqType):
        print('OnTickRegError')

    def OnGetTickData(self, this, strSymbol, strTickSn, strMatchTime, strBuyPri, strSellPri, strMatchPri, strMatchQty, strTolMatQty,
                      strMatchAmt, strTolMatAmt, ReqType):
        print('OnGetTickData')

    def OnTickRangeDataError(self, this, strSymbol, lErrCode, ReqType):
        print('OnTickRangeDataError')

    def OnGetTickRangeData(self, this, strSymbol, strStartTime, strEndTime, strTolMatQty, strTolMatAmt, ReqType):
        print('OnGetTickRangeData')

    def OnGetTimePack(self, this, strTradeType, strTime, ReqType):
        print('OnGetTimePack {},{}'.format(strTradeType, strTime))

    def OnGetDelayOpen(self, this, symbol, DelayOpen, ReqType):
        print('OnGetDelayOpen')

    def OnGetFutStatus(self, this, symbol, FunctionCode, BreakTime, StartTime, ReopenTime, ReqType):
        print('OnGetFutStatus')

    def OnGetLimitChange(self, this, symbol, FunctionCode, StatusTime, Level, ExpandType, ReqType):
        print('OnGetLimitChange')


class YuantaQuoteWapper:
    def __init__(self, handle, bot):
        self.bot = bot

        Iwindow = POINTER(IUnknown)()
        Icontrol = POINTER(IUnknown)()
        Ievent = POINTER(IUnknown)()

        res = atl.AtlAxCreateControlEx("YUANTAQUOTE.YuantaQuoteCtrl.1", handle, None,
                                       byref(Iwindow),
                                       byref(Icontrol),
                                       byref(GUID()),
                                       Ievent)

        self.YuantaQuote = GetBestInterface(Icontrol)
        self.YuantaQuoteEvents = YuantaQuoteEvents(self)
        self.YuantaQuoteEventsConnect = GetEvents(
            self.YuantaQuote, self.YuantaQuoteEvents)


class StockBot:

    def __init__(self, botuid, account, pwd):
        #----------------------------------------
        print('class StockBot: TO GOGOGO')
        print('self.Yuanta = YuantaQuoteWapper(botuid, self) TO GOGOGOGOGOGO')
        #---------------------------------------
        self.Yuanta = YuantaQuoteWapper(botuid, self)
        self.Account = account
        self.Pwd = pwd

    def login(self):
        # T port 80/443 , T+1 port 82/442 ,  reqType=1 T盤 , reqType=2  T+1盤
        #self.Yuanta.YuantaQuote.SetMktLogon(
        #    self.Account, self.Pwd, '203.66.93.84', '80', 1, 0)
        
        print('login-1')
        self.Yuanta.YuantaQuote.SetMktLogon(self.Account, self.Pwd, '203.66.93.84', '82', 2, 1)
        print('login-2')

    def watch(self, ret_type):
        ret = self.Yuanta.YuantaQuote.AddMktReg('1101', "4", ret_type, 0)
        print("AddMktReg {}".format(ret))


class MyApp(wx.App):
    def MainLoop(self, run_func):

        # Create an event loop and make it active.  If you are
        # only going to temporarily have a nested event loop then
        # you should get a reference to the old one and set it as
        # the active event loop when you are done with this one...
        evtloop = wx.GUIEventLoop()
        old = wx.EventLoop.GetActive()
        wx.EventLoop.SetActive(evtloop)

        # This outer loop determines when to exit the application,
        # for this example we let the main frame reset this flag
        # when it closes.
        while self.keepGoing:
            # At this point in the outer loop you could do
            # whatever you implemented your own MainLoop for.  It
            # should be quick and non-blocking, otherwise your GUI
            # will freeze.

            # call_your_code_here()
            run_func()
            while not q.empty():
                next_job = q.get()
                DoJob(Bot, next_job)

            # This inner loop will process any GUI events
            # until there are no more waiting.
            while evtloop.Pending():
                evtloop.Dispatch()

            # Send idle events to idle handlers.  You may want to
            # throttle this back a bit somehow so there is not too
            # much CPU time spent in the idle handlers.  For this
            # example, I'll just snooze a little...
            time.sleep(0.10)
            evtloop.ProcessIdle()

        wx.EventLoop.SetActive(old)

    def OnInit(self):
        self.keepGoing = True
        return True


def run_job():
    while not q.empty():   #error
        next_job = q.get()

        print('def run_job() test OK1')
        DoJob(Bot, next_job)  #error
        print('def run_job() test OK-end')

#===================================================================
if __name__ == "__main__":
    print()
    print('This name = main then GO')
    print('1. wx.App START')
    #------------------------------
    app = MyApp()
    #app=wx.App()
    #-------------------------------
    frame = wx.Frame(None, wx.ID_ANY, "YA-G Hello")
    frame.Show(True)       #frame.Show(False)
    print('1. wx.App END')
    print()
      
    ACCOUNT = 'E123632952'
    PWD = '3359ldmYY'
    #----------------------------------------------------------
    print('2. Bot = StockBot START')
    #Bot = StockBot(frame.Handle, 'E123632952','3359ldmYY')
    Bot = StockBot(frame.Handle, ACCOUNT, PWD)
    print('2. Bot = StockBot END')
    print()
    #----------------------------------------------------------
    print('3. Job(Job.STOCK_LOGIN) TO GO')
    Job(Job.STOCK_LOGIN)  # class job   def __init__(self, do_type, do_value=0):
    print('3. Job(Job.STOCK_LOGIN) END')
    print()

    #------------------------------------
    print('4. app.MainLoop() TO GO')
    app.MainLoop(run_job) #error
    #app.MainLoop()
    print('4. app.MainLoop() END')
    print()
    #-------------------------------------

    print('main-000-END')
    #==========================================================================


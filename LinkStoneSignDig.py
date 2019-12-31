#coding=utf-8

import wx
import LinkStoneSignDigGUI
import win32api, win32gui


class DIGSFrame(LinkStoneSignDigGUI.MyDialog1):
    def __init__(self,parent):
        LinkStoneSignDigGUI.MyDialog1.__init__(self,parent)

def main():     
    ct = win32api.GetConsoleTitle()
    hd = win32gui.FindWindow(0,ct)
    win32gui.ShowWindow(hd,0)   
    app = wx.App(False) 
    frame = DIGSFrame(None) 
    frame.Show(True) 
    app.MainLoop() 
 
if __name__ == '__main__':
    main()

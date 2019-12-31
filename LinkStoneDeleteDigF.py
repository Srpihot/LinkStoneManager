#coding=utf-8

import wx
import LinkStoneDeleteDigFGUI
import win32api, win32gui


class DIGFrame(LinkStoneDeleteDigFGUI.MyDialog1):
    def __init__(self,parent):
        LinkStoneDeleteDigFGUI.MyDialog1.__init__(self,parent)

def main():     
    ct = win32api.GetConsoleTitle()
    hd = win32gui.FindWindow(0,ct)
    win32gui.ShowWindow(hd,0)   
    app = wx.App(False) 
    frame = DIGFrame(None) 
    frame.Show(True) 
    app.MainLoop() 
 
if __name__ == '__main__':
    main()

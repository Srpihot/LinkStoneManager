#coding=utf-8

import wx
import LinkStoneInsertDigFGUI
import win32api, win32gui


class DIGFrame(LinkStoneInsertDigFGUI.MyDialog1):
    def __init__(self,parent):
        LinkStoneInsertDigFGUI.MyDialog1.__init__(self,parent)

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

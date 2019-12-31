#coding=utf-8

#coding=utf-8
import LinkStoneGSPanalGui
import wx
import win32api
import win32gui
import os


class LinkStoneGSP(LinkStoneGSPanalGui.MyFrame1):
    def __init__(self, parent):
       LinkStoneGSPanalGui.MyFrame1.__init__(self, parent)

    def nav_person_info(self,event):
        os.system('start python LinkStoneGanShi.py')
    
    def nav_StrGra(self,event):
        os.system('start python LinkStoneSelectStuGrade.py')
    
    def Nav_Course(self,event):
        os.system('start python LinkStoneSelectCourse.py')

    def LinkStone_info(self,event):
        os.system('start python LinkStoneStu.py')


def main():
    ct = win32api.GetConsoleTitle()
    hd = win32gui.FindWindow(0, ct)
    win32gui.ShowWindow(hd, 0)
    app = wx.App(False)
    frame = LinkStoneGSP(None)
    frame.Show(True)
    app.MainLoop()


if __name__ == '__main__':
    main()

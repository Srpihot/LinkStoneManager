#coding=utf-8

#coding=utf-8
import LinkStonePermissonPanalGui
import wx
import win32api
import win32gui
import os


class LinkStonePSP(LinkStonePermissonPanalGui.MyFrame11):
    def __init__(self, parent):
       LinkStonePermissonPanalGui.MyFrame11.__init__(self, parent)

    def nav_person_info(self,event):
        os.system('start python LinkStonePermisson.py')
    
    def nav_StrGra(self,event):
        os.system('start python LinkStoneSelectStuGradePermisson.py')
    
    def Nav_Course(self,event):
        os.system('start python LinkStoneSelectCourse.py')

    def LinkStone_info(self,event):
        os.system('start python LinkStoneStu.py')
    
    def money_manage(self,event):
        os.system('start python LinkStoneFinInsert.py')

    def select_money(self,event):
        os.system('start python LinkStoneSelectFin.py')

    def select_activity(self,event):
        os.system('start python Activity_1.py')
    
    def manage_activity(self,event):
        os.system('start python Activity_2.py')

def main():
    ct = win32api.GetConsoleTitle()
    hd = win32gui.FindWindow(0, ct)
    win32gui.ShowWindow(hd, 0)
    app = wx.App(False)
    frame = LinkStonePSP(None)
    frame.Show(True)
    app.MainLoop()


if __name__ == '__main__':
    main()

# -*- coding: utf-8 -*-


import ActivityGUI_2
import wx
import win32api
import win32gui
import pymssql
import os


connect = pymssql.connect("127.0.0.1","sa","123456","LinkStone")
cursor = connect.cursor()


class Activity_manage(ActivityGUI_2.MyFrame2):

    def __init__(self,Parent):
        ActivityGUI_2.MyFrame2.__init__(self,Parent)

    def Del_Activity(self,event):

        Id = self.m_textCtrl1.GetValue()
        try:
            cursor.execute(
                "delete from Activitylist where id = '%s'" % (Id)
            )
            connect.commit()
            os.system('start python LinkStoneDeleteDig.py')
        except:
            os.system('start python LinkStoneDeleteDigF.py')

        cursor.close()
        connect.close()

    def Add_Activity( self, event ):

        id = self.m_textCtrl1.GetValue()
        name = self.m_textCtrl2.GetValue()
        master = self.m_textCtrl3.GetValue()
        start = self.m_textCtrl4.GetValue()
        end = self.m_textCtrl5.GetValue()
        plan = self.m_textCtrl6.GetValue()
        coast = self.m_textCtrl7.GetValue()
        summarized = self.m_textCtrl8.GetValue()
        try:
            cursor.execute(
                "insert into Activitylist values( %s, '%s', '%s', '%s', '%s','%s','%s','%s')"  % (id,name,master,start,end,plan,coast,summarized)
            )
            connect.commit()
            os.system('start python LinkStoneInsertDig.py')
        except:
            os.system('start python LinkStoneInsertDigF.py')

        cursor.close()
        connect.close()

    def Cancel( self, event ):

        cursor.close()
        connect.close()
        exit()
    


def main():
    ct = win32api.GetConsoleTitle()
    hd = win32gui.FindWindow(0, ct)
    win32gui.ShowWindow(hd, 0)
    app = wx.App()
    frame = Activity_manage(None)
    frame.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
# -*- coding: utf-8 -*-


import ActivityGUI_1
import wx
import win32api
import win32gui
import pymssql


class Activity_select(ActivityGUI_1.MyFrame1):
    def __init__(self,parent):
        ActivityGUI_1.MyFrame1.__init__(self,parent)
    def se_Activity( self, event ):
        ID = self.m_textCtrl1.GetValue()
        connect = pymssql.connect("127.0.0.1","sa","123456","LinkStone")
        cursor = connect.cursor()
        cursor.execute(
            "select * from Activitylist where id = '%s'" % (ID)
        )
        row = cursor.fetchone()

        self.m_textCtrl2.SetValue(str(row[1]))
        self.m_textCtrl4.SetValue(str(row[2]))
        self.m_textCtrl3.SetValue(str(row[3]))
        self.m_textCtrl7.SetValue(str(row[4]))
        self.m_textCtrl6.SetValue(str(row[5]))
        self.m_textCtrl5.SetValue(str(row[6]))
        self.m_textCtrl8.SetValue(str(row[7]))

        cursor.close()
        connect.close()

def main():
    ct = win32api.GetConsoleTitle()
    hd = win32gui.FindWindow(0, ct)
    win32gui.ShowWindow(hd, 0)
    app = wx.App()
    frame = Activity_select(None)
    frame.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
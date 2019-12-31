#coding=utf-8
import LinkStoneSelectStuGradeGUI
import wx
import win32api
import win32gui
import pymssql


class SelStuGrade(LinkStoneSelectStuGradeGUI.MyFrame1):
    def __init__(self, parent):
        LinkStoneSelectStuGradeGUI.MyFrame1.__init__(self, parent)
        with open('Config.Painter','r') as f:
            readlines=f.readlines()
            readline=readlines[0].split('#')
            Sno=readline[0]
        self.StudentNo_text.SetValue(Sno)

    def SelectCoursef(self,event):
        Sno=self.StudentNo_text.GetValue()
        CourseName = self.CourseName_text.GetValue()
        connect = pymssql.connect('(local)', 'sa', '123456', 'LinkStone')
        cursor = connect.cursor()
        cursor.execute(
            "EXEC StuGrade_List @Sno='%s',@CourseName='%s'"%(Sno,CourseName))
        row = cursor.fetchone()

        self.CourseNo_text.SetValue(row[0])
        self.CourseGrade_text.SetValue(str(row[1]))
        cursor.close()
        connect.close()

    #确定按钮
    def SelCouDetf(self, event):
        exit()

	#取消按钮
    def SelCouCanf(self, event):
        exit()


def main():
    ct = win32api.GetConsoleTitle()
    hd = win32gui.FindWindow(0, ct)
    win32gui.ShowWindow(hd, 0)
    app = wx.App(False)
    frame = SelStuGrade(None)
    frame.Show(True)
    app.MainLoop()


if __name__ == '__main__':
    main()


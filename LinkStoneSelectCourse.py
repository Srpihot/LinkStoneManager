#coding=utf-8
import LinkStoneSelectCourseGUI
import wx
import win32api
import win32gui
import pymssql


class SelectCou(LinkStoneSelectCourseGUI.MyFrame1):
    def __init__(self, parent):
       LinkStoneSelectCourseGUI.MyFrame1.__init__(self, parent)

    def SelectCourse(self, event):
        courseName = self.CouseName_text.GetValue()
        connect = pymssql.connect('(local)', 'sa', '123456', 'LinkStone')
        cursor = connect.cursor()
        cursor.execute("select CourseNo,CourseGrade,CourseAbout from Course where CourseName ='%s'" % (courseName))
        row = cursor.fetchone()

        self.CouserNo_text.SetValue(str(row[0]))
        self.CouseGrade_text.SetValue(str(row[1]))
        self.CourseAbout_text.SetValue(str(row[2]))
        cursor.close()
        connect.close()

    #确定按钮
    def SelCouDet(self, event):
        exit()

	#取消按钮
    def SelCouCan(self, event):
        exit()


def main():
    ct = win32api.GetConsoleTitle()
    hd = win32gui.FindWindow(0, ct)
    win32gui.ShowWindow(hd, 0)
    app = wx.App(False)
    frame = SelectCou(None)
    frame.Show(True)
    app.MainLoop()


if __name__ == '__main__':
    main()

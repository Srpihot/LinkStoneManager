#coding=utf-8
import LinkStoneStuGUI
import wx
import win32api
import win32gui
import pymssql


class LinkStoneStu(LinkStoneStuGUI.MyFrame1):
    def __init__(self, parent):
       LinkStoneStuGUI.MyFrame1.__init__(self, parent)
       with open('Config.Painter','r') as f:
            readlines=f.readlines()
            readline=readlines[0].split('#')
            Sno=readline[0]
       self.StudentNo_text.SetValue(Sno)

    def SelectCourse(self, event):
        Sno=''
        with open('Config.Painter','r') as f:
            readlines=f.readlines()
            readline=readlines[0].split('#')
            Sno=readline[0]
        self.StudentNo_text.SetValue(Sno)
        connect = pymssql.connect('(local)', 'sa', '123456', 'LinkStone')
        cursor = connect.cursor()
        cursor.execute(
            "select * from LinkStoneStu where StudentNo ='%s'" % (Sno))
        row = cursor.fetchone()

        self.NickName_text.SetValue(str(row[1]))
        self.SelfAbout_text.SetValue(str(row[2]))
        self.WriteupNumber_text.SetValue(str(row[3]))
        self.SolveProblem_text.SetValue(str(row[4]))
        self.WrongProblem_text.SetValue(str(row[5]))
        self.Working_text.SetValue(str(row[6]))
        self.Integral_text.SetValue(str(row[7]))
        self.Money_text.SetValue(str(row[8]))
        self.Toplist_text.SetValue(str(row[9]))
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
    frame = LinkStoneStu(None)
    frame.Show(True)
    app.MainLoop()


if __name__ == '__main__':
    main()

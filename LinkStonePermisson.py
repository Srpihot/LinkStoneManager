#coding=utf-8
import wx
import LinkStonePermissonGui
import win32api, win32gui
import pymssql
import os

class LinkStonep1(LinkStonePermissonGui.MyFrame2):
    def __init__(self,parent):
        LinkStonePermissonGui.MyFrame2.__init__(self,parent)
    
    def save_info(self,event):
        connect = pymssql.connect('(local)','sa','123456','LinkStone')
        cursor=connect.cursor()
        Sname=self.searchName.GetValue()
    
        cursor.execute("exec StudentinfoName_List @Sname='"+Sname+"'")
        row=cursor.fetchone()
        #print(row) 
        self.gNo.SetValue(row[0])
        self.gName.SetValue(row[1])
        self.gSex.SetValue(row[2])
        self.gAge.SetValue(str(row[3]))
        self.gMarkName.SetValue(row[4])
        self.aGrade.SetValue(row[5])
        self.gCollege.SetValue(row[6])
        self.gMojar.SetValue(row[7])
        self.gNativePlace.SetValue(row[8])
        self.gTelnumber.SetValue(row[9])
        self.gQQnumber.SetValue(row[10])
        self.gEmail.SetValue(row[11])
        cursor.close()
        connect.close()
    
    def change_ture(self,event):
        connect = pymssql.connect('(local)','sa','123456','LinkStone')
        cursor=connect.cursor()
        Sname=self.searchName.GetValue()
    
        try:
            cursor.execute("update Student set MarkName='%s' where StudentName='%s'"%(self.gMarkName.GetValue(),Sname))
            cursor.execute("update Student set Age='%s' where StudentName='%s'"%(self.gAge.GetValue(),Sname))
            cursor.execute("update ConnectStu set Telnumber='%s' where StudentNo=(select StudentNo from Student where StudentName='%s')"%(self.gTelnumber.GetValue(),Sname))
            cursor.execute("update ConnectStu set QQnumber='%s' where StudentNo=(select StudentNo from Student where StudentName='%s')"%(self.gQQnumber.GetValue(),Sname))
            cursor.execute("update ConnectStu set Email='%s' where StudentNo=(select StudentNo from Student where StudentName='%s')"%(self.gEmail.GetValue(),Sname))
        
            connect.commit()
            cursor.execute("exec StudentinfoName_List @Sname='"+Sname+"'")
            row=cursor.fetchone()
            print(row)
            os.system('start python LinkStoneChangeDig.py')
        except:
            os.system('start python LinkStoneChangeDigF.py')
        
        cursor.close()
        connect.close()
    
    def  cancel_info(self,event):
        exit()


def main():  
    
    ct = win32api.GetConsoleTitle()
    hd = win32gui.FindWindow(0,ct)
    win32gui.ShowWindow(hd,0)   
    app = wx.App(False) 
    frame = LinkStonep1(None) 
    frame.Show(True) 
    app.MainLoop() 
 
if __name__ == '__main__':
    main()

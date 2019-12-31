#coding=utf-8
import wx
import LinkStoneSignGui
import win32api, win32gui
import pymssql
import os

class LinkStoneSign1(LinkStoneSignGui.MyFrame2):
    def __init__(self,parent):
        LinkStoneSignGui.MyFrame2.__init__(self,parent)
    
    def save_info(self,event):
        connect = pymssql.connect('(local)','sa','123456','LinkStone')
        cursor=connect.cursor()
        Sno=self.searchName.GetValue()
        #print(row) 
        StudentNo=self.gNo.GetValue()
        StudentName=self.gName.GetValue()
        Sex=self.gSex.GetValue()
        Age=self.gAge.GetValue()
        MarkName=self.gMarkName.GetValue()
        Place=self.gNativePlace.GetValue()
        tel=self.gTelnumber.GetValue()
        qq=self.gQQnumber.GetValue()
        email=self.gEmail.GetValue()
        try:
            cursor.execute("INSERT INTO student(StudentNo,StudentName,MarkName,Birthday,Sex,NativePlace) VALUES('%s','%s','%s','%s','%s','%s')"%(StudentNo,StudentName,MarkName,Age,Sex,Place))
            cursor.execute("INSERT INTO ConnectStu VALUES('%s','%s','%s','%s')"%(StudentNo,tel,qq,email))
            connect.commit()
            os.system('start python LinkStoneSignDig.py')
        except:
            os.system('start python LinkStoneSigFnDig.py')
        cursor.close()
        connect.close()
    

    
    def  cancel_info(self,event):
        exit()


def main():  
    
    ct = win32api.GetConsoleTitle()
    hd = win32gui.FindWindow(0,ct)
    win32gui.ShowWindow(hd,0)   
    app = wx.App(False) 
    frame = LinkStoneSign1(None) 
    frame.Show(True) 
    app.MainLoop() 
 
if __name__ == '__main__':
    main()

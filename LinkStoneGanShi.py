#coding=utf-8
import wx
import LinkStoneGanshiGui
import win32api, win32gui
import pymssql
import os

class LinkStonegs(LinkStoneGanshiGui.MyFame2):
    def __init__(self,parent):
        LinkStoneGanshiGui.MyFame2.__init__(self,parent)
    
    def save_info(self,event):
        connect = pymssql.connect('(local)','sa','123456','LinkStone')
        cursor=connect.cursor()
        Sno=''
        with open('Config.Painter','r') as f:
            readlines=f.readlines()
            readline=readlines[0].split('#')
            Sno=readline[0]
    
        cursor.execute("exec Studentinfo_List @Sno='"+Sno+"'")
        row=cursor.fetchone()
        #print(row) 
        self.gNo.SetValue(row[0])
        self.gName.SetValue(row[1])
        self.gSex.SetValue(row[2])
        self.gAge.SetValue(str(row[3]))
        self.gMarkName.SetValue(row[4])
        self.gGarde.SetValue(row[5])
        self.gCollege.SetValue(row[6])
        self.gMojar.SetValue(row[7])
        self.gNativePlace.SetValue(row[8])
        self.gTelnumber.SetValue(row[9])
        self.gQQ.SetValue(row[10])
        self.gEmail.SetValue(row[11])
        cursor.close()
        connect.close()
    
    def true_info(self,event):
        connect = pymssql.connect('(local)','sa','123456','LinkStone')
        cursor=connect.cursor()
        Sno=''
        with open('Config.Painter','r') as f:
            readlines=f.readlines()
            readline=readlines[0].split('#')
            Sno=readline[0]
        try:
            cursor.execute("update Student set MarkName='%s' where StudentNo='%s'"%(self.gMarkName.GetValue(),Sno))
            cursor.execute("update Student set Age='%s' where StudentNo='%s'"%(self.gAge.GetValue(),Sno))
            cursor.execute("update ConnectStu set Telnumber='%s' where StudentNo='%s'"%(self.gTelnumber.GetValue(),Sno))
            cursor.execute("update ConnectStu set QQnumber='%s' where StudentNo='%s'"%(self.gQQ.GetValue(),Sno))
            cursor.execute("update ConnectStu set Email='%s' where StudentNo='%s'"%(self.gEmail.GetValue(),Sno))
            connect.commit()
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
    frame = LinkStonegs(None) 
    frame.Show(True) 
    app.MainLoop() 
 
if __name__ == '__main__':
    main()

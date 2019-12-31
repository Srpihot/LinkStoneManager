#coding=utf-8 
import LinkStoneLogin
import wx
import os
import pymssql
import win32api, win32gui

class LoginFrame(LinkStoneLogin.MyFrame1):
    def __init__(self,parent):
        LinkStoneLogin.MyFrame1.__init__(self,parent)

    def check_login(self,event):
        Login_user=self.User_text.GetValue()
        Login_password=self.Password_text.GetValue()
        with open('Config.Painter','w') as f:
            f.write(Login_user)
            f.write('#')
            f.write(Login_password)
            f.close()            
        #print(Login_user,Login_password)
        user=[]
        pawd=[]
        connect = pymssql.connect('(local)','sa','123456','LinkStone')
        cursor=connect.cursor()
        cursor.execute("select * from PermissionBy")
        row=cursor.fetchone()
        while row:
            #print('%s\t%s'%(row[0],row[1]))
            user.append(row[0].strip())
            pawd.append(row[1].strip())
            row=cursor.fetchone()
       
        if Login_user in user and Login_password in pawd:
                cursor.execute("select Permission from Permissionlist where StudentNo='%s'"%(Login_user))
                row=cursor.fetchone()
                if '3' in str(row[0]).strip():
                    os.system('start python LinkStoneGSPanal.py')
                if '1' in str(row[0]).strip():
                    os.system('start python LinkStonePermissonPanal.py')
                if '2' in str(row[0]).strip():
                    os.system('start python LinkStonePermissonPanal.py')
                if '4' in str(row[0]).strip():
                    os.system('start python LinkStoneSign.py')
                #os.system('start calc')
                #print(str(row[0]).strip())
                cursor.close()
                connect.close()
                exit()
        else:
                os.system('start python LinkStoneDig.py')
                cursor.close()
                connect.close()

    def Check_Password(self,event):
        with open('Config.Painter','r') as f:
            readlines=f.readlines()
            #for readline in readlines:
            readline=readlines[0].split('#')
            self.User_text.SetValue(readline[0])
            self.Password_text.SetValue(readline[1])

def main():    
    ct = win32api.GetConsoleTitle()
    hd = win32gui.FindWindow(0,ct)
    win32gui.ShowWindow(hd,0)       
    app = wx.App(False) 
    frame = LoginFrame(None) 
    frame.Show(True) 
    app.MainLoop() 
 
if __name__ == '__main__':
    main()

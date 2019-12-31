#coding=utf-8

#coding=utf-8
import LinkStoneSelectFinGui
import wx
import win32api
import win32gui
import os
import pymssql

with open('ConfigN.Painter','w') as f:
    f.write('1')
    f.close()


class LinkStoneSFG(LinkStoneSelectFinGui.MyFrame1):

    def __init__(self, parent):
        n=1
        LinkStoneSelectFinGui.MyFrame1.__init__(self, parent)
        connect = pymssql.connect('(local)','sa','123456','LinkStone')
        cursor=connect.cursor()
        try:
            cursor.execute("select * from Financial where id=%s"%(int(n)))
            row=cursor.fetchone()
            self.id_text_1.SetValue(str(row[0]))
            self.dong_text_1.SetValue(row[1])
            self.coast_text_1.SetValue(str(row[2]))
            self.note_text_1.SetValue(row[3])
        except:
            pass
        try:
            cursor.execute("select * from Financial where id=%s"%(int(n)+1))
            row=cursor.fetchone()
            self.id_text_2.SetValue(str(row[0]))
            self.dong_text_2.SetValue(row[1])
            self.coast_text_2.SetValue(str(row[2]))
            self.note_text_2.SetValue(row[3])
        except:
            pass

        try:
            cursor.execute("select * from Financial where id=%s"%(int(n+2)))
            row=cursor.fetchone()
            self.id_text_3.SetValue(str(row[0]))
            self.dong_text_3.SetValue(row[1])
            self.coast_text_3.SetValue(str(row[2]))
            self.note_text_3.SetValue(row[3])
        except:
            pass

        try:
            cursor.execute("select * from Financial where id=%s"%(int(n+3)))
            row=cursor.fetchone()
            self.id_text_4.SetValue(str(row[0]))
            self.dong_text_4.SetValue(row[1])
            self.coast_text_4.SetValue(str(row[2]))
            self.note_text_4.SetValue(row[3])
        except:
            pass

        try:
            cursor.execute("select * from Financial where id=%s"%(int(n+4)))
            row=cursor.fetchone()
            self.id_text_5.SetValue(str(row[0]))
            self.dong_text_5.SetValue(row[1])
            self.coast_text_5.SetValue(str(row[2]))
            self.note_text_5.SetValue(row[3])
        except:
            pass
        cursor.close()
        connect.close()

    def next_page(self,event):
        with open('ConfigN.Painter','r') as f:
            n=f.read()
            f.close()
        n=int(n)+5
        connect = pymssql.connect('(local)','sa','123456','LinkStone')
        cursor=connect.cursor()
        try:
            cursor.execute("select * from Financial where id=%s"%(int(n)))
            row=cursor.fetchone()
            self.id_text_1.SetValue(str(row[0]))
            self.dong_text_1.SetValue(row[1])
            self.coast_text_1.SetValue(str(row[2]))
            self.note_text_1.SetValue(row[3])
        except:
            pass
        try:
            cursor.execute("select * from Financial where id=%s"%(int(n)+1))
            row=cursor.fetchone()
            self.id_text_2.SetValue(str(row[0]))
            self.dong_text_2.SetValue(row[1])
            self.coast_text_2.SetValue(str(row[2]))
            self.note_text_2.SetValue(row[3])
        except:
            pass

        try:
            cursor.execute("select * from Financial where id=%s"%(int(n+2)))
            row=cursor.fetchone()
            self.id_text_3.SetValue(str(row[0]))
            self.dong_text_3.SetValue(row[1])
            self.coast_text_3.SetValue(str(row[2]))
            self.note_text_3.SetValue(row[3])
        except:
            pass

        try:
            cursor.execute("select * from Financial where id=%s"%(int(n+3)))
            row=cursor.fetchone()
            self.id_text_4.SetValue(str(row[0]))
            self.dong_text_4.SetValue(row[1])
            self.coast_text_4.SetValue(str(row[2]))
            self.note_text_4.SetValue(row[3])
        except:
            pass

        try:
            cursor.execute("select * from Financial where id=%s"%(int(n+4)))
            row=cursor.fetchone()
            self.id_text_5.SetValue(str(row[0]))
            self.dong_text_5.SetValue(row[1])
            self.coast_text_5.SetValue(str(row[2]))
            self.note_text_5.SetValue(row[3])
        except:
            pass
        cursor.close()
        connect.close()
        with open('ConfigN.Painter','w') as f:
            f.write(str(n))
            f.close()

    def before_page(self,event):
       with open('ConfigN.Painter','r') as f:
            n=f.read()
            f.close()
       n=int(n)-5
       if n>=0:
            connect = pymssql.connect('(local)','sa','123456','LinkStone')
            cursor=connect.cursor()
            try:
                cursor.execute("select * from Financial where id=%s"%(int(n)))
                row=cursor.fetchone()
                self.id_text_1.SetValue(str(row[0]))
                self.dong_text_1.SetValue(row[1])
                self.coast_text_1.SetValue(str(row[2]))
                self.note_text_1.SetValue(row[3])
            except:
                pass
            try:
                cursor.execute("select * from Financial where id=%s"%(int(n)+1))
                row=cursor.fetchone()
                self.id_text_2.SetValue(str(row[0]))
                self.dong_text_2.SetValue(row[1])
                self.coast_text_2.SetValue(str(row[2]))
                self.note_text_2.SetValue(row[3])
            except:
                pass

            try:
                cursor.execute("select * from Financial where id=%s"%(int(n+2)))
                row=cursor.fetchone()
                self.id_text_3.SetValue(str(row[0]))
                self.dong_text_3.SetValue(row[1])
                self.coast_text_3.SetValue(str(row[2]))
                self.note_text_3.SetValue(row[3])
            except:
                pass

            try:
                cursor.execute("select * from Financial where id=%s"%(int(n+3)))
                row=cursor.fetchone()
                self.id_text_4.SetValue(str(row[0]))
                self.dong_text_4.SetValue(row[1])
                self.coast_text_4.SetValue(str(row[2]))
                self.note_text_4.SetValue(row[3])
            except:
                pass

            try:
                cursor.execute("select * from Financial where id=%s"%(int(n+4)))
                row=cursor.fetchone()
                self.id_text_5.SetValue(str(row[0]))
                self.dong_text_5.SetValue(row[1])
                self.coast_text_5.SetValue(str(row[2]))
                self.note_text_5.SetValue(row[3])
            except:
                pass
            cursor.close()
            connect.close()

       else:
            connect = pymssql.connect('(local)','sa','123456','LinkStone')
            cursor=connect.cursor()
            try:
                cursor.execute("select * from Financial where id=%s"%(int(1)))
                row=cursor.fetchone()
                self.id_text_1.SetValue(str(row[0]))
                self.dong_text_1.SetValue(row[1])
                self.coast_text_1.SetValue(str(row[2]))
                self.note_text_1.SetValue(row[3])
            except:
                pass
            try:
                cursor.execute("select * from Financial where id=%s"%(int(2)))
                row=cursor.fetchone()
                self.id_text_2.SetValue(str(row[0]))
                self.dong_text_2.SetValue(row[1])
                self.coast_text_2.SetValue(str(row[2]))
                self.note_text_2.SetValue(row[3])
            except:
                pass

            try:
                cursor.execute("select * from Financial where id=%s"%(int(3)))
                row=cursor.fetchone()
                self.id_text_3.SetValue(str(row[0]))
                self.dong_text_3.SetValue(row[1])
                self.coast_text_3.SetValue(str(row[2]))
                self.note_text_3.SetValue(row[3])
            except:
                pass

            try:
                cursor.execute("select * from Financial where id=%s"%(int(4)))
                row=cursor.fetchone()
                self.id_text_4.SetValue(str(row[0]))
                self.dong_text_4.SetValue(row[1])
                self.coast_text_4.SetValue(str(row[2]))
                self.note_text_4.SetValue(row[3])
            except:
                pass

            try:
                cursor.execute("select * from Financial where id=%s"%(int(5)))
                row=cursor.fetchone()
                self.id_text_5.SetValue(str(row[0]))
                self.dong_text_5.SetValue(row[1])
                self.coast_text_5.SetValue(str(row[2]))
                self.note_text_5.SetValue(row[3])
            except:
                pass

            cursor.close()
            connect.close()
       with open('ConfigN.Painter','w') as f:
            f.write(str(n))
            f.close()

    def cando(self,event):
        exit()

def main():
    
    ct = win32api.GetConsoleTitle()
    hd = win32gui.FindWindow(0, ct)
    win32gui.ShowWindow(hd, 0)
    app = wx.App(False)
    frame = LinkStoneSFG(None)
    frame.Show(True)
    app.MainLoop()


if __name__ == '__main__':
    main()

#coding=utf-8
import LinkStoneFinInsertGUI
import wx
import win32api
import win32gui
import pymssql
import os


class LinkStoneFinInsert(LinkStoneFinInsertGUI.MyFrame1):
    def __init__(self, parent):
       LinkStoneFinInsertGUI.MyFrame1.__init__(self, parent)

    def insertInfo(self, event):
        

        connect = pymssql.connect('(local)', 'sa', '123456', 'LinkStone')
        cursor = connect.cursor()

        finId = self.mId_text.GetValue()
        finDoing = self.mDoing_text.GetValue()
        finHowMuch = self.mHowMuch_text.GetValue()
        finNote = self.mNote_text.GetValue()
        try:
            cursor.execute("INSERT INTO Financial(id,Doing,HowMuch,Note) VALUES(%s,'%s',%s,'%s')" % (finId,finDoing,finHowMuch,finNote))
            connect.commit()
            os.system('start python LinkStoneInsertDig.py')
        except:
            os.system('start python LinkStoneInsertDigF.py')

        cursor.close()
        connect.close()
        # try:
        #     conn = pymssql.connect(host='127.0.0.1',user='sa',password='123456',database='MOSHI_lqx',charset='utf8')
        #     cursor.execute("INSERT INTO Financial VALUES('%s','%s','%s','%s')" % (finId, finDoing, finHowMuch, finNote))
        #     conn.commit()

        # except Exception as ex:
        #     conn.rollback()
        #     raise ex
        # finally:
        #     conn.close()

    def cancel(self,event):
        exit()

    def deleteInfo(self,event):
        deleteID = self.DelectNote_text.GetValue()
        print(deleteID)

        connect = pymssql.connect('(local)', 'sa', '123456', 'LinkStone')
        cursor = connect.cursor()
        try:
            cursor.execute(
                "delete from Financial where id =  %s" % deleteID)

            connect.commit()
            os.system('start python LinkStoneDeleteDig.py')
        except:
            os.system('start python LinkStoneDeleteDigF.py')

        cursor.close()
        connect.close()

        # try:
        #     conn = pymssql.connect(host='127.0.0.1',user='sa',password='123456',database='MOSHI_lqx',charset='utf8')
        #     cur = conn.cursor("delete from Financial where id = '%s'" % deleteID)
        #     conn.commit()

        # except Exception as ex:
        #     conn.rollback()
        # finally:
        #     conn.close()



def main():
    ct = win32api.GetConsoleTitle()
    hd = win32gui.FindWindow(0, ct)
    win32gui.ShowWindow(hd, 0)
    app = wx.App(False)
    frame = LinkStoneFinInsert(None)
    frame.Show(True)
    app.MainLoop()


if __name__ == '__main__':
    main()


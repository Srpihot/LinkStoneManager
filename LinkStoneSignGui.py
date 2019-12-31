# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):

	def __init__( self, parent ):

		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"正在注册", pos = wx.DefaultPosition, size = wx.Size( 583,373 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		icon = wx.EmptyIcon()
		icon.CopyFromBitmap(wx.BitmapFromImage(wx.Image(("LOGO1.png"), wx.BITMAP_TYPE_PNG)))
		self.SetIcon(icon)
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"学号：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		bSizer9.Add( self.m_staticText6, 0, wx.ALL, 5 )

		self.gNo = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.gNo, 0, wx.ALL, 5 )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"姓名：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		bSizer9.Add( self.m_staticText7, 0, wx.ALL, 5 )

		self.gName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.gName, 0, wx.ALL, 5 )

		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"性别：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		bSizer9.Add( self.m_staticText8, 0, wx.ALL, 5 )

		self.gSex = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.gSex, 0, wx.ALL, 5 )


		bSizer8.Add( bSizer9, 1, wx.EXPAND, 5 )

		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"出生日期：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		bSizer10.Add( self.m_staticText9, 0, wx.ALL, 5 )

		self.gAge = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.gAge, 0, wx.ALL, 5 )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"代号：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		bSizer10.Add( self.m_staticText10, 0, wx.ALL, 5 )

		self.gMarkName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.gMarkName, 0, wx.ALL, 5 )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"年级：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		bSizer10.Add( self.m_staticText11, 0, wx.ALL, 5 )

		self.aGrade = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.aGrade, 0, wx.ALL, 5 )


		bSizer8.Add( bSizer10, 1, wx.EXPAND, 5 )

		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"院系：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		bSizer11.Add( self.m_staticText12, 0, wx.ALL, 5 )

		self.gCollege = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.gCollege, 0, wx.ALL, 5 )

		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"专业：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		bSizer11.Add( self.m_staticText13, 0, wx.ALL, 5 )

		self.gMojar = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.gMojar, 0, wx.ALL, 5 )

		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"籍贯：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		bSizer11.Add( self.m_staticText14, 0, wx.ALL, 5 )

		self.gNativePlace = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.gNativePlace, 0, wx.ALL, 5 )


		bSizer8.Add( bSizer11, 1, wx.EXPAND, 5 )

		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"电话：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		bSizer12.Add( self.m_staticText15, 0, wx.ALL, 5 )

		self.gTelnumber = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.gTelnumber, 0, wx.ALL, 5 )

		self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"QQ：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )

		bSizer12.Add( self.m_staticText16, 0, wx.ALL, 5 )

		self.gQQnumber = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.gQQnumber, 0, wx.ALL, 5 )

		self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"邮箱：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )

		bSizer12.Add( self.m_staticText17, 0, wx.ALL, 5 )

		self.gEmail = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.gEmail, 0, wx.ALL, 5 )


		bSizer8.Add( bSizer12, 1, wx.EXPAND, 5 )

		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, u"个人介绍：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )

		bSizer13.Add( self.m_staticText18, 1, wx.ALL, 5 )

		self.searchName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.searchName, 3, wx.ALL, 5 )


		bSizer8.Add( bSizer13, 0, wx.EXPAND, 5 )

		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )

		self.save_button = wx.Button( self, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.save_button, 1, wx.ALL|wx.EXPAND, 5 )

		self.cancel_button = wx.Button( self, wx.ID_ANY, u"取消", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.cancel_button, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer8.Add( bSizer14, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer8 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.save_button.Bind( wx.EVT_BUTTON, self.save_info )
		self.cancel_button.Bind( wx.EVT_BUTTON, self.cancel_info )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def save_info( self, event ):
		event.Skip()

	def cancel_info( self, event ):
		event.Skip()



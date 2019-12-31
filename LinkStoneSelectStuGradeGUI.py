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
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):

		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,274 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		icon = wx.EmptyIcon()
		icon.CopyFromBitmap(wx.BitmapFromImage(wx.Image(("LOGO1.png"), wx.BITMAP_TYPE_PNG)))
		self.SetIcon(icon)
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"墨石协会测试成绩查询", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "字魂87号-乾坤手书" ) )

		bSizer1.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText41 = wx.StaticText( self, wx.ID_ANY, u"学号：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )

		bSizer4.Add( self.m_staticText41, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.StudentNo_text = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.StudentNo_text, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText51 = wx.StaticText( self, wx.ID_ANY, u"科目名：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )

		bSizer4.Add( self.m_staticText51, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.CourseName_text = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.CourseName_text, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.SelectCourse = wx.Button( self, wx.ID_ANY, u"查询", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.SelectCourse, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer2.Add( bSizer4, 0, 0, 5 )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText61 = wx.StaticText( self, wx.ID_ANY, u"编号：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText61.Wrap( -1 )

		bSizer5.Add( self.m_staticText61, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.CourseNo_text = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.CourseNo_text, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer2.Add( bSizer5, 0, wx.EXPAND, 5 )

		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"成绩：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		bSizer6.Add( self.m_staticText8, 0, wx.ALL, 5 )

		self.CourseGrade_text = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.CourseGrade_text, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer2.Add( bSizer6, 0, wx.EXPAND, 5 )

		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )

		self.SelCouDet = wx.Button( self, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.SelCouDet, 0, wx.ALL, 5 )

		self.SelCouCan = wx.Button( self, wx.ID_ANY, u"取消", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.SelCouCan, 0, wx.ALL, 5 )


		bSizer2.Add( bSizer13, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.SelectCourse.Bind( wx.EVT_BUTTON, self.SelectCoursef )
		self.SelCouDet.Bind( wx.EVT_BUTTON, self.SelCouDetf )
		self.SelCouCan.Bind( wx.EVT_BUTTON, self.SelCouCanf )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def SelectCoursef( self, event ):
		event.Skip()

	def SelCouDetf( self, event ):
		event.Skip()

	def SelCouCanf( self, event ):
		event.Skip()



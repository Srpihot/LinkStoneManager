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

		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,322 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL, name = u"墨石协会管理系统" )
		icon = wx.EmptyIcon()
		icon.CopyFromBitmap(wx.BitmapFromImage(wx.Image(("LOGO1.png"), wx.BITMAP_TYPE_PNG)))
		self.SetIcon(icon)
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"墨石协会测试科目查询", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "字魂87号-乾坤手书" ) )

		bSizer2.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer23 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer26 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"科目名称：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		bSizer26.Add( self.m_staticText14, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.CouseName_text = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer26.Add( self.CouseName_text, 0, wx.ALL, 5 )


		bSizer23.Add( bSizer26, 0, wx.ALL, 5 )

		self.SelCourBtn = wx.Button( self, wx.ID_ANY, u"查询", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer23.Add( self.SelCourBtn, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		bSizer2.Add( bSizer23, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer24 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"科目编号 ：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		bSizer24.Add( self.m_staticText15, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.CouserNo_text = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer24.Add( self.CouserNo_text, 1, wx.ALL, 5 )


		bSizer2.Add( bSizer24, 0, wx.EXPAND, 5 )

		bSizer25 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"科目最高分:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )

		bSizer25.Add( self.m_staticText16, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.CouseGrade_text = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer25.Add( self.CouseGrade_text, 1, wx.ALL, 5 )


		bSizer2.Add( bSizer25, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer27 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"科目描述 ：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )

		bSizer27.Add( self.m_staticText17, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.CourseAbout_text = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer27.Add( self.CourseAbout_text, 1, wx.ALL, 5 )


		bSizer2.Add( bSizer27, 0, wx.EXPAND, 5 )

		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		self.DetBtn = wx.Button( self, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.DetBtn, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

		self.CanBtn = wx.Button( self, wx.ID_ANY, u"取消", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.CanBtn, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer2.Add( bSizer7, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.SelCourBtn.Bind( wx.EVT_BUTTON, self.SelectCourse )
		self.DetBtn.Bind( wx.EVT_BUTTON, self.SelCouDet )
		self.CanBtn.Bind( wx.EVT_BUTTON, self.SelCouCan )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def SelectCourse( self, event ):
		event.Skip()

	def SelCouDet( self, event ):
		event.Skip()

	def SelCouCan( self, event ):
		event.Skip()



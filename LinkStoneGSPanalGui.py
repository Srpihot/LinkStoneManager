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

		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,200 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		icon = wx.EmptyIcon()
		icon.CopyFromBitmap(wx.BitmapFromImage(wx.Image(("LOGO1.png"), wx.BITMAP_TYPE_PNG)))
		self.SetIcon(icon)
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"干事用户界面", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetFont( wx.Font( 25, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "字魂87号-乾坤手书" ) )
		self.m_staticText1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.m_staticText1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer2.Add( self.m_staticText1, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_bpButton1 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton1.SetBitmap( wx.Bitmap( u"LOGO1.png", wx.BITMAP_TYPE_ANY ) )
		bSizer2.Add( self.m_bpButton1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"个人信息查询", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_button1, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"成绩查询", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_button2, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_button4 = wx.Button( self, wx.ID_ANY, u"科目查询", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_button4, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_button5 = wx.Button( self, wx.ID_ANY, u"平台信息查询", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_button5, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer1.Add( bSizer3, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.nav_person_info )
		self.m_button2.Bind( wx.EVT_BUTTON, self.nav_StrGra )
		self.m_button4.Bind( wx.EVT_BUTTON, self.Nav_Course )
		self.m_button5.Bind( wx.EVT_BUTTON, self.LinkStone_info )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def nav_person_info( self, event ):
		event.Skip()

	def nav_StrGra( self, event ):
		event.Skip()

	def Nav_Course( self, event ):
		event.Skip()

	def LinkStone_info( self, event ):
		event.Skip()



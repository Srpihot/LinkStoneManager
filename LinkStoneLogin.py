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

		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"墨石协会管理系统", pos = wx.DefaultPosition, size = wx.Size( 500,435 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		icon = wx.EmptyIcon()
		icon.CopyFromBitmap(wx.BitmapFromImage(wx.Image(("LOGO1.png"), wx.BITMAP_TYPE_PNG)))
		self.SetIcon(icon)
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_bitmap3 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"LOGO1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_bitmap3, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"墨石协会管理系统登陆", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText9.Wrap( -1 )

		self.m_staticText9.SetFont( wx.Font( 25, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "字魂87号-乾坤手书" ) )
		self.m_staticText9.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.m_staticText9.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )

		bSizer2.Add( self.m_staticText9, 1, wx.ALL, 20 )


		bSizer1.Add( bSizer2, 0, wx.EXPAND, 2 )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"学号：", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText2.Wrap( 1 )

		self.m_staticText2.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "字魂87号-乾坤手书" ) )
		self.m_staticText2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

		bSizer3.Add( self.m_staticText2, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.User_text = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.User_text.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "字魂87号-乾坤手书" ) )
		self.User_text.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer3.Add( self.User_text, 3, wx.ALIGN_CENTER_VERTICAL|wx.FIXED_MINSIZE|wx.RIGHT, 50 )


		bSizer1.Add( bSizer3, 0, wx.ALL|wx.EXPAND, 20 )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"密码：", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText3.Wrap( -1 )

		self.m_staticText3.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "字魂87号-乾坤手书" ) )
		self.m_staticText3.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

		bSizer4.Add( self.m_staticText3, 1, wx.ALL, 20 )

		self.Password_text = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Password_text.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, "Small Fonts" ) )

		bSizer4.Add( self.Password_text, 3, wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 50 )


		bSizer1.Add( bSizer4, 0, wx.ALL|wx.EXPAND, 20 )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_checkBox1 = wx.CheckBox( self, wx.ID_ANY, u"记住密码", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		bSizer5.Add( self.m_checkBox1, 1, wx.ALL, 20 )

		self.LoginButton = wx.Button( self, wx.ID_ANY, u"登陆", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.LoginButton, 1, wx.ALL, 20 )


		bSizer1.Add( bSizer5, 1, wx.EXPAND, 5 )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"墨石安全技术部", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		self.m_staticText10.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "字魂87号-乾坤手书" ) )
		self.m_staticText10.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

		bSizer6.Add( self.m_staticText10, 0, wx.ALL|wx.ALIGN_RIGHT, 20 )


		bSizer1.Add( bSizer6, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_checkBox1.Bind( wx.EVT_CHECKBOX, self.Check_Password )
		self.LoginButton.Bind( wx.EVT_BUTTON, self.check_login )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def Check_Password( self, event ):
		event.Skip()

	def check_login( self, event ):
		event.Skip()



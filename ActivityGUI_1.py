# -*- coding: utf-8 -*-


import wx
import wx.xrc


class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):

		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"墨石活动管理", pos = wx.DefaultPosition, size = wx.Size( 500,403 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		icon = wx.EmptyIcon()
		icon.CopyFromBitmap(wx.BitmapFromImage(wx.Image(("LOGO1.png"), wx.BITMAP_TYPE_PNG)))
		self.SetIcon(icon)
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"墨石信安活动查询系统", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText6.Wrap( -1 )

		self.m_staticText6.SetFont( wx.Font( 22, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "华文行楷" ) )
		self.m_staticText6.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.m_staticText6.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer8.Add( self.m_staticText6, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer1.Add( bSizer8, 1, wx.EXPAND, 5 )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"活 动 名 称", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetFont( wx.Font( 12, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "楷体" ) )
		self.m_staticText1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.m_staticText1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer3.Add( self.m_staticText1, 0, wx.ALL, 5 )

		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_textCtrl2, 1, wx.ALL, 5 )


		bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )

		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"活动负责人 ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		self.m_staticText2.SetFont( wx.Font( 12, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "楷体" ) )
		self.m_staticText2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.m_staticText2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer6.Add( self.m_staticText2, 0, wx.ALL, 5 )

		self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_textCtrl4, 1, wx.ALL, 5 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"开始时间", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		self.m_staticText3.SetFont( wx.Font( 12, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "楷体" ) )
		self.m_staticText3.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.m_staticText3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer6.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_textCtrl3, 1, wx.ALL, 5 )


		bSizer1.Add( bSizer6, 1, wx.EXPAND, 5 )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"活动总花费 ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		self.m_staticText8.SetFont( wx.Font( 12, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "楷体" ) )
		self.m_staticText8.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.m_staticText8.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer4.Add( self.m_staticText8, 0, wx.ALL, 5 )

		self.m_textCtrl5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_textCtrl5, 1, wx.ALL, 5 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"结束时间", wx.DefaultPosition, wx.DefaultSize, wx.ST_NO_AUTORESIZE )
		self.m_staticText4.Wrap( -1 )

		self.m_staticText4.SetFont( wx.Font( 12, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "楷体" ) )
		self.m_staticText4.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.m_staticText4.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer4.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.m_textCtrl7 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_textCtrl7, 1, wx.ALL, 5 )


		bSizer1.Add( bSizer4, 1, wx.EXPAND, 5 )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"计划书 url ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		self.m_staticText5.SetFont( wx.Font( 12, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "楷体" ) )
		self.m_staticText5.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.m_staticText5.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer5.Add( self.m_staticText5, 0, wx.ALL, 5 )

		self.m_textCtrl6 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_textCtrl6, 1, wx.ALL, 5 )


		bSizer1.Add( bSizer5, 1, wx.EXPAND, 5 )

		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"活动总结url", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		self.m_staticText9.SetFont( wx.Font( 12, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "楷体" ) )
		self.m_staticText9.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.m_staticText9.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer7.Add( self.m_staticText9, 0, wx.ALL, 5 )

		self.m_textCtrl8 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_textCtrl8, 1, wx.ALL, 5 )


		bSizer1.Add( bSizer7, 1, wx.EXPAND, 5 )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"输入活动ID查询：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		self.m_staticText10.SetFont( wx.Font( 14, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "楷体" ) )
		self.m_staticText10.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTIONTEXT ) )
		self.m_staticText10.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer2.Add( self.m_staticText10, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		bSizer2.Add( self.m_textCtrl1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"查询", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button1.SetFont( wx.Font( 12, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "楷体" ) )
		self.m_button1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_button1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		bSizer2.Add( self.m_button1, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.se_Activity )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def se_Activity( self, event ):
		event.Skip()



# -*- coding: utf-8 -*-


import wx
import wx.xrc

class MyFrame2 ( wx.Frame ):

	def __init__( self, parent ):

		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,360 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		icon = wx.EmptyIcon()
		icon.CopyFromBitmap(wx.BitmapFromImage(wx.Image(("LOGO1.png"), wx.BITMAP_TYPE_PNG)))
		self.SetIcon(icon)
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"墨石信安活动管理系统", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		self.m_staticText12.SetFont( wx.Font( 22, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "华文行楷" ) )
		self.m_staticText12.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

		bSizer9.Add( self.m_staticText12, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer23 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText27 = wx.StaticText( self, wx.ID_ANY, u"活动ID(如要删除活动数据则输入ID点击删除)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )

		self.m_staticText27.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

		bSizer23.Add( self.m_staticText27, 0, wx.ALL, 5 )

		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		bSizer23.Add( self.m_textCtrl1, 1, wx.ALL, 5 )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"删除", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.m_button2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

		bSizer23.Add( self.m_button2, 0, wx.ALL, 5 )


		bSizer9.Add( bSizer23, 1, wx.EXPAND, 5 )

		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"活 动 名 称", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		self.m_staticText11.SetFont( wx.Font( 12, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "楷体" ) )
		self.m_staticText11.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

		bSizer11.Add( self.m_staticText11, 0, wx.ALL, 5 )

		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_textCtrl2, 1, wx.ALL, 5 )


		bSizer9.Add( bSizer11, 1, wx.EXPAND, 5 )

		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText111 = wx.StaticText( self, wx.ID_ANY, u"活动负责人 ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText111.Wrap( -1 )

		self.m_staticText111.SetFont( wx.Font( 12, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "楷体" ) )
		self.m_staticText111.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

		bSizer12.Add( self.m_staticText111, 0, wx.ALL, 5 )

		self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.m_textCtrl3, 1, wx.ALL, 5 )

		self.m_staticText1114 = wx.StaticText( self, wx.ID_ANY, u"开始时间", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1114.Wrap( -1 )

		self.m_staticText1114.SetFont( wx.Font( 12, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "楷体" ) )
		self.m_staticText1114.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

		bSizer12.Add( self.m_staticText1114, 0, wx.ALL, 5 )

		self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.m_textCtrl4, 1, wx.ALL, 5 )


		bSizer9.Add( bSizer12, 1, wx.EXPAND, 5 )

		bSizer121 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText1111 = wx.StaticText( self, wx.ID_ANY, u"活动总花费 ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1111.Wrap( -1 )

		self.m_staticText1111.SetFont( wx.Font( 12, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "楷体" ) )
		self.m_staticText1111.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

		bSizer121.Add( self.m_staticText1111, 0, wx.ALL, 5 )

		self.m_textCtrl7 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer121.Add( self.m_textCtrl7, 1, wx.ALL, 5 )

		self.m_staticText11111 = wx.StaticText( self, wx.ID_ANY, u"结束时间", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11111.Wrap( -1 )

		self.m_staticText11111.SetFont( wx.Font( 12, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "楷体" ) )
		self.m_staticText11111.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

		bSizer121.Add( self.m_staticText11111, 0, wx.ALL, 5 )

		self.m_textCtrl5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer121.Add( self.m_textCtrl5, 1, wx.ALL, 5 )


		bSizer9.Add( bSizer121, 1, wx.EXPAND, 5 )

		bSizer122 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText1112 = wx.StaticText( self, wx.ID_ANY, u"计划书 url ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1112.Wrap( -1 )

		self.m_staticText1112.SetFont( wx.Font( 12, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "楷体" ) )
		self.m_staticText1112.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

		bSizer122.Add( self.m_staticText1112, 0, wx.ALL, 5 )

		self.m_textCtrl6 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer122.Add( self.m_textCtrl6, 1, wx.ALL, 5 )


		bSizer9.Add( bSizer122, 1, wx.EXPAND, 5 )

		bSizer123 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText1113 = wx.StaticText( self, wx.ID_ANY, u"活动总结url", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1113.Wrap( -1 )

		self.m_staticText1113.SetFont( wx.Font( 12, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "楷体" ) )
		self.m_staticText1113.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

		bSizer123.Add( self.m_staticText1113, 0, wx.ALL, 5 )

		self.m_textCtrl8 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer123.Add( self.m_textCtrl8, 1, wx.ALL, 5 )


		bSizer9.Add( bSizer123, 1, wx.EXPAND, 5 )

		bSizer24 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button3 = wx.Button( self, wx.ID_ANY, u"添加", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button3.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

		bSizer24.Add( self.m_button3, 1, wx.ALL, 5 )

		self.m_button4 = wx.Button( self, wx.ID_ANY, u"取消", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button4.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

		bSizer24.Add( self.m_button4, 1, wx.ALL, 5 )


		bSizer9.Add( bSizer24, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer9 )
		self.Layout()

		self.Centre( wx.BOTH )

		self.m_button2.Bind( wx.EVT_BUTTON, self.Del_Activity )
		self.m_button3.Bind( wx.EVT_BUTTON, self.Add_Activity )
		self.m_button4.Bind( wx.EVT_BUTTON, self.Cancel )

	def __del__( self ):
		pass


	def Del_Activity( self, event ):
		event.Skip()

	def Add_Activity( self, event ):
		event.Skip()

	def Cancel( self, event ):
		event.Skip()



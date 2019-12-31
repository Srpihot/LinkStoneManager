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

		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,420 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		icon = wx.EmptyIcon()
		icon.CopyFromBitmap(wx.BitmapFromImage(wx.Image(("LOGO1.png"), wx.BITMAP_TYPE_PNG)))
		self.SetIcon(icon)
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"墨石协会财务管理系统", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "字魂87号-乾坤手书" ) )

		bSizer1.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"流水号 ", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText2.Wrap( -1 )

		bSizer2.Add( self.m_staticText2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"状态", wx.DefaultPosition, wx.Size( 50,-1 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText3.Wrap( -1 )

		bSizer2.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"金额", wx.DefaultPosition, wx.Size( 100,-1 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText4.Wrap( -1 )

		bSizer2.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"备注", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText5.Wrap( -1 )

		bSizer2.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer1.Add( bSizer2, 0, wx.EXPAND|wx.ALL, 5 )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		self.id_text_1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		bSizer3.Add( self.id_text_1, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.dong_text_1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		bSizer3.Add( self.dong_text_1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.coast_text_1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		bSizer3.Add( self.coast_text_1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.note_text_1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.note_text_1, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer1.Add( bSizer3, 0, wx.EXPAND|wx.ALL, 5 )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		self.id_text_2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		bSizer4.Add( self.id_text_2, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.dong_text_2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		bSizer4.Add( self.dong_text_2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.coast_text_2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		bSizer4.Add( self.coast_text_2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.note_text_2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.note_text_2, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer1.Add( bSizer4, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer41 = wx.BoxSizer( wx.HORIZONTAL )

		self.id_text_3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		bSizer41.Add( self.id_text_3, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.dong_text_3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		bSizer41.Add( self.dong_text_3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.note_text_3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		bSizer41.Add( self.note_text_3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl81 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer41.Add( self.m_textCtrl81, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )


		bSizer1.Add( bSizer41, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND|wx.ALL, 5 )

		bSizer42 = wx.BoxSizer( wx.HORIZONTAL )

		self.id_text_4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		bSizer42.Add( self.id_text_4, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )

		self.dong_text_4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		bSizer42.Add( self.dong_text_4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.coast_text_4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		bSizer42.Add( self.coast_text_4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.note_text_4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer42.Add( self.note_text_4, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )


		bSizer1.Add( bSizer42, 0, wx.EXPAND|wx.ALL, 5 )

		bSizer43 = wx.BoxSizer( wx.HORIZONTAL )

		self.id_text_5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		bSizer43.Add( self.id_text_5, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.dong_text_5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		bSizer43.Add( self.dong_text_5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.coast_text_5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		bSizer43.Add( self.coast_text_5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.note_text_5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer43.Add( self.note_text_5, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )


		bSizer1.Add( bSizer43, 0, wx.EXPAND|wx.ALL, 5 )

		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )

		self.before_page_button = wx.Button( self, wx.ID_ANY, u"上一页", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.before_page_button, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.next_page_button = wx.Button( self, wx.ID_ANY, u"下一页", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.next_page_button, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.can = wx.Button( self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.can, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer8, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.before_page_button.Bind( wx.EVT_BUTTON, self.before_page )
		self.next_page_button.Bind( wx.EVT_BUTTON, self.next_page )
		self.can.Bind( wx.EVT_BUTTON, self.cando )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def before_page( self, event ):
		event.Skip()

	def next_page( self, event ):
		event.Skip()

	def cando( self, event ):
		event.Skip()



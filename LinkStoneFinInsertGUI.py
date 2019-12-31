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

		
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,328 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		icon = wx.EmptyIcon()
		icon.CopyFromBitmap(wx.BitmapFromImage(wx.Image(("LOGO1.png"), wx.BITMAP_TYPE_PNG)))
		self.SetIcon(icon)
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"墨石协会财务信息管理", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		self.m_staticText2.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "字魂87号-乾坤手书" ) )

		bSizer1.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"流水号:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer2.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.mId_text = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.mId_text, 1, wx.ALL, 5 )


		bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"状态 ：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		bSizer5.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.mDoing_text = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.mDoing_text, 1, wx.ALL, 5 )


		bSizer1.Add( bSizer5, 0, wx.EXPAND, 5 )

		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"金额 ：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		bSizer6.Add( self.m_staticText5, 0, wx.ALL, 5 )

		self.mHowMuch_text = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.mHowMuch_text, 1, wx.ALL, 5 )


		bSizer1.Add( bSizer6, 0, wx.EXPAND, 5 )

		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"备注 ：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		bSizer7.Add( self.m_staticText6, 0, wx.ALL, 5 )

		self.mNote_text = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.mNote_text, 1, wx.ALL, 5 )


		bSizer1.Add( bSizer7, 0, wx.EXPAND, 5 )

		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"添加", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_button2, 0, wx.ALL, 5 )

		self.m_button3 = wx.Button( self, wx.ID_ANY, u"结束", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_button3, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer8, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer71 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText61 = wx.StaticText( self, wx.ID_ANY, u"流水号：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText61.Wrap( -1 )

		bSizer71.Add( self.m_staticText61, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.DelectNote_text = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer71.Add( self.DelectNote_text, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_button8 = wx.Button( self, wx.ID_ANY, u"删除", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer71.Add( self.m_button8, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer1.Add( bSizer71, 0, wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button2.Bind( wx.EVT_BUTTON, self.insertInfo )
		self.m_button3.Bind( wx.EVT_BUTTON, self.cancel )
		self.m_button8.Bind( wx.EVT_BUTTON, self.deleteInfo )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def insertInfo( self, event ):
		event.Skip()

	def cancel( self, event ):
		event.Skip()

	def deleteInfo( self, event ):
		event.Skip()



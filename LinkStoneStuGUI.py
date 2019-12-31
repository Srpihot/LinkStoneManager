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

		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 559,393 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		icon = wx.EmptyIcon()
		icon.CopyFromBitmap(wx.BitmapFromImage(wx.Image(("LOGO1.png"), wx.BITMAP_TYPE_PNG)))
		self.SetIcon(icon)
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"墨石协会CTF平台个人信息", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "字魂87号-乾坤手书" ) )

		bSizer1.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"学号：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer2.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.StudentNo_text = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		bSizer2.Add( self.StudentNo_text, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"查询", wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		bSizer2.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )


		bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"昵称：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		bSizer4.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.NickName_text = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		bSizer4.Add( self.NickName_text, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"个人介绍：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		bSizer4.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.SelfAbout_text = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		bSizer4.Add( self.SelfAbout_text, 1, wx.ALL, 5 )


		bSizer1.Add( bSizer4, 0, wx.EXPAND, 5 )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"正确答题数量：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		bSizer5.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.SolveProblem_text = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.SolveProblem_text, 1, wx.ALL, 5 )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"题解数量：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		bSizer5.Add( self.m_staticText9, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.WriteupNumber_text = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.WriteupNumber_text, 1, wx.ALL, 5 )


		bSizer1.Add( bSizer5, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL|wx.EXPAND, 5 )

		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"答题错误数量：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		bSizer6.Add( self.m_staticText10, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.WrongProblem_text = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.WrongProblem_text, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"正在作答题目：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		bSizer6.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.Working_text = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.Working_text, 1, wx.ALL, 5 )


		bSizer1.Add( bSizer6, 0, wx.EXPAND|wx.ALL, 5 )

		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"积分：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		bSizer8.Add( self.m_staticText12, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.Integral_text = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.Integral_text, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"金币：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		bSizer8.Add( self.m_staticText13, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.Money_text = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.Money_text, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"排名：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		bSizer8.Add( self.m_staticText14, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.Toplist_text = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.Toplist_text, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer1.Add( bSizer8, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button4 = wx.Button( self, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_button5 = wx.Button( self, wx.ID_ANY, u"取消", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer1.Add( bSizer9, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.SelectCourse )
		self.m_button4.Bind( wx.EVT_BUTTON, self.SelCouDet )
		self.m_button5.Bind( wx.EVT_BUTTON, self.SelCouCan )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def SelectCourse( self, event ):
		event.Skip()

	def SelCouDet( self, event ):
		event.Skip()

	def SelCouCan( self, event ):
		event.Skip()



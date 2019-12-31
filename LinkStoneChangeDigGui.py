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
## Class MyDialog1
###########################################################################

class MyDialog1 ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		icon = wx.EmptyIcon()
		icon.CopyFromBitmap(wx.BitmapFromImage(wx.Image(("LOGO1.png"), wx.BITMAP_TYPE_PNG)))
		self.SetIcon(icon)
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.Rdig = wx.StaticText( self, wx.ID_ANY, u"修改成功!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Rdig.Wrap( -1 )

		bSizer7.Add( self.Rdig, 0, wx.ALL, 5 )


		self.SetSizer( bSizer7 )
		self.Layout()
		bSizer7.Fit( self )

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass



#!/usr/bin/env python
# generated by wxGlade 0.6.3 on Fri Aug 31 12:33:35 2012

import wx
from WareboxDialog import WareboxDialog

if __name__ == "__main__":
    import gettext
    gettext.install("app") # replace with the appropriate catalog name

    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    WareboxDialog = WareboxDialog('.',None, -1, "")
    app.SetTopWindow(WareboxDialog)
    WareboxDialog.Show()
    app.MainLoop()
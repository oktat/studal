# -*- coding: UTF-8 -*-
#
# generated by wxGlade 1.0.1 on Wed Dec 29 16:44:18 2021
#

import wx
# begin wxGlade: dependencies
import wx.grid
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MainForm(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MainForm.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((800, 500))
        self.SetTitle("frame")

        # Tool Bar
        self.frame_toolbar = wx.ToolBar(self, -1)
        self.SetToolBar(self.frame_toolbar)
        self.frame_toolbar.Realize()
        # Tool Bar end

        self.panel_1 = wx.Panel(self, wx.ID_ANY)

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)

        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2.Add(sizer_7, 0, wx.EXPAND, 0)

        sizer_7.Add((0, 0), 2, wx.EXPAND, 0)

        sizer_8 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_7.Add(sizer_8, 1, wx.EXPAND, 0)

        self.searchTf = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        self.searchTf.SetMinSize((150, 35))
        sizer_8.Add(self.searchTf, 0, 0, 0)

        self.searchBtn = wx.Button(self.panel_1, wx.ID_ANY, u"Keresés")
        sizer_8.Add(self.searchBtn, 0, wx.LEFT, 10)

        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2.Add(sizer_3, 4, wx.EXPAND, 0)

        self.grid_1 = wx.grid.Grid(self.panel_1, wx.ID_ANY, size=(1, 1))
        self.grid_1.CreateGrid(10, 0)
        sizer_3.Add(self.grid_1, 4, wx.EXPAND, 0)

        sizer_4 = wx.BoxSizer(wx.VERTICAL)
        sizer_3.Add(sizer_4, 2, wx.EXPAND, 0)

        sizer_4.Add((20, 10), 0, wx.EXPAND, 0)

        self.groupCb = wx.ComboBox(self.panel_1, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN)
        self.groupCb.SetMinSize((150, 35))
        sizer_4.Add(self.groupCb, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

        sizer_4.Add((20, 10), 0, wx.EXPAND, 0)

        self.fillStudentsBtn = wx.Button(self.panel_1, wx.ID_ANY, u"Diákok")
        self.fillStudentsBtn.SetMinSize((110, 35))
        sizer_4.Add(self.fillStudentsBtn, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

        sizer_4.Add((20, 10), 0, wx.EXPAND, 0)

        label_1 = wx.StaticText(self.panel_1, wx.ID_ANY, u"Diákok kezelése", style=wx.ALIGN_CENTER_HORIZONTAL)
        label_1.SetMinSize((150, 35))
        sizer_4.Add(label_1, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, 20)

        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4.Add(sizer_5, 1, wx.EXPAND, 0)

        self.newStudentBtn = wx.Button(self.panel_1, wx.ID_ANY, u"Új")
        self.newStudentBtn.SetMinSize((110, 35))
        sizer_5.Add(self.newStudentBtn, 0, wx.LEFT, 15)

        self.modifyStudentBtn = wx.Button(self.panel_1, wx.ID_ANY, u"Szerkesztés")
        self.modifyStudentBtn.SetMinSize((110, 35))
        sizer_5.Add(self.modifyStudentBtn, 0, wx.LEFT, 10)

        label_2 = wx.StaticText(self.panel_1, wx.ID_ANY, u"Csoportok kezelése", style=wx.ALIGN_CENTER_HORIZONTAL)
        label_2.SetMinSize((150, 35))
        sizer_4.Add(label_2, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, 15)

        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4.Add(sizer_6, 1, wx.EXPAND, 0)

        self.newGroupBtn = wx.Button(self.panel_1, wx.ID_ANY, u"Új")
        self.newGroupBtn.SetMinSize((110, 35))
        sizer_6.Add(self.newGroupBtn, 0, wx.LEFT, 15)

        self.modifyGroupBtn = wx.Button(self.panel_1, wx.ID_ANY, u"Szerkesztés")
        self.modifyGroupBtn.SetMinSize((110, 35))
        sizer_6.Add(self.modifyGroupBtn, 0, wx.LEFT, 10)

        sizer_4.Add((20, 60), 0, wx.EXPAND, 0)

        self.exitBtn = wx.Button(self.panel_1, wx.ID_ANY, u"Kilépés")
        sizer_4.Add(self.exitBtn, 0, wx.ALIGN_RIGHT | wx.RIGHT, 10)

        sizer_4.Add((20, 10), 0, wx.EXPAND, 0)

        statusLbl = wx.StaticText(self.panel_1, wx.ID_ANY, "Status label", style=wx.ALIGN_CENTER_HORIZONTAL)
        statusLbl.SetMinSize((150, 35))
        sizer_2.Add(statusLbl, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

        self.panel_1.SetSizer(sizer_1)

        self.Layout()
        self.Centre()
        # end wxGlade

# end of class MainForm

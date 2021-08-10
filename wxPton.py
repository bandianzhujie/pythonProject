# -*- coding: utf-8 -*-
import wx


class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title = title, size = (800, 600))
        self.control = wx.TextCtrl(self, style = wx.TE_MULTILINE)
        self.CreateStatusBar()

        filemenu = wx.Menu()

        menuOpen = filemenu.Append(wx.ID_OPEN, "Open", "Open a file")
        menuAbout = filemenu.Append(wx.ID_ABORT, "About", "information  about app")
        menuExit = filemenu.AppendSeparator()
        filemenu.Append(wx.ID_EXIT, "Quit", "quit app")

        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "File")
        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)

        self.sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        self.buttons = []
        for i in range(0, 6):
            self.buttons.append(wx.Button(self, -1, "Button" + str(i)))
            self.sizer2.Add(self.buttons[i], 1, wx.SHAPED)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.control, 1, wx.EXPAND)
        self.sizer.Add(self.sizer2, 0, wx.GROW)

        self.SetSizer(self.sizer)
        self.SetAutoLayout(True)
        self.sizer.Fit(self)
        self.Show(True)

    def OnAbout(self, e):
        dlg = wx.MessageDialog(self, "A small text editor", "About Sample Editor", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

    def OnExit(self):
        self.Close(True)

    def OnOpen(self, e):
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'r')  # 暂时只读
            self.control.SetValue(f.read())
            f.close()
        dlg.Destroy()


app = wx.App(False)
frame = MainWindow(None, "ProExcel")
app.MainLoop()


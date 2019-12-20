# -*- coding: utf-8 -*-
'''
    Flying Saucer main function.
'''

# This file is part of a flying saucer experience.

# Distributed under the terms of the last Apache License.
# The full license is in the file LICENCE, distributed as part of this software.

__author__ = 'Team Machine'


import taskbar
import wx


class Toolbook(wx.Toolbook) :

    def __init__(self, parent) :
        '''
            Toolbook Constructor
        '''
        wx.Toolbook.__init__(self, parent, wx.ID_ANY, style=wx.BK_DEFAULT)


class Colours(wx.Dialog):
    
    def __init__(self, parent, id, title):
        '''
            Wake yourself up, sirens on
            Cause we are fighting so exciting, now it's on
            Are you ready for the war?
            Show your colours
            Bring your colours to the floor 
        '''
        wx.Dialog.__init__(self, parent, id, title, size=(640,480))
        self.tbIcon = taskbar.CustomTaskBarIcon(self)
        panel = wx.Panel(self)
        toolbook = Toolbook(panel)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(toolbook, proportion=1, flag=wx.ALL|wx.EXPAND, border=5)
        panel.SetSizer(sizer)
        self.Layout()
        self.Bind(wx.EVT_ICONIZE, self.onMinimize)
        self.Bind(wx.EVT_CLOSE, self.onClose)

    def onClose(self, event):
        '''
            Destroy the taskbar icon and the frame
        '''
        self.tbIcon.RemoveIcon()
        self.tbIcon.Destroy()
        self.Destroy()

    def onMinimize(self, event):
        '''
            When minimizing, hide the frame so it "minimizes to tray"
        '''
        self.Hide()


def main():
    '''
        Flying Saucer Experience (EXP)
    '''
    app = wx.App(False)
    Colours(None, -1, 'Space-based Adjutant')
    app.MainLoop()

if __name__ == "__main__":
    main()
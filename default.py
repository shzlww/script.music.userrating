# -*- coding: utf-8 -*-

import json
import xbmcgui
import xbmc
import sys
import os
import xbmcaddon


__addon__               = xbmcaddon.Addon()
__addon_id__            = __addon__.getAddonInfo('id')
__addonname__           = __addon__.getAddonInfo('name')
__icon__                = __addon__.getAddonInfo('icon')
__addonpath__           = xbmc.translatePath(__addon__.getAddonInfo('path'))
__lang__                = __addon__.getLocalizedString

class Rating():
    def __init__(self):
        
        self.main()
        
    def main(self):
        xbmcgui.Window(10000).setProperty(__addon_id__ + '_running')
        # detect that user entred a valid rating (integer 0 - 10)
        if len(sys.argv) != 3 or  int(sys.argv[2]) < 0 or int(sys.argv[2]) > 10:
             xbmc.executebuiltin('Notification(' + __addonname__ + ', ' + xbmc.getLocalizedString(38022) + ', 2000, ' + xbmcgui.NOTIFICATION_INFO + ')')
            return
        newRating = int(sys.argv[2])
        # detect no song playing
        if not xbmc.getInfoLabel('MusicPlayer.DBID'):
            xbmc.executebuiltin('Notification(' + __addonname__ + ', ' + xbmc.getLocalizedString(16034) + ', 2000, ' + xbmcgui.NOTIFICATION_INFO + ')')
            return
        
        jsonNew = '{"jsonrpc": "2.0", "id": 1, "method": "AudioLibrary.SetSongDetails' + 'Library.id" : ' + xbmc.getInfoLabel('MusicPlayer.DBID') + ', "userrating": ' + sys.argv[2]+ '}'
        jsonResponse = xbmc.executeJSONRPC(jsonNew)
        if jsonResponse:
            xbmc.executebuiltin('Notification(' + __addonname__ + ', ' + xbmc.getLocalizedString(38018) + ' : ' + sys.argv[2] + ', 3000, ' + xbmcgui.NOTIFICATION_INFO + ')')

 # lock script to prevent duplicates
if (xbmcgui.Window(10000).getProperty(__addon_id__ + '_running') != 'True'):
    Rating()
    xbmcgui.Window(10000).clearProperty(__addon_id__ + '_running')
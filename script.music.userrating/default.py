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
        xbmcgui.Window(10000).setProperty(__addon_id__ + '_running',  'true')
        # detect that user entred a valid rating (integer 0 - 10)
        if len(sys.argv) != 2 or  int(sys.argv[1]) < 0 or int(sys.argv[1]) > 10:
            # No rating
            xbmc.executebuiltin('Notification(' + __addonname__ + ', ' + xbmc.getLocalizedString(38022) + ', 2000, ' + xbmcgui.NOTIFICATION_INFO + ')')
            return
        newRating = int(sys.argv[1])
        # detect no song playing
        if not xbmc.getInfoLabel('MusicPlayer.DBID'):
            # Couldn't get songs from database
            xbmc.executebuiltin('Notification(' + __addonname__ + ', ' + xbmc.getLocalizedString(16034) + ', 2000, ' + xbmcgui.NOTIFICATION_INFO + ')')
            return
        
        jsonNew = '{"jsonrpc": "2.0", "id": 1, "method": "AudioLibrary.SetSongDetails", "params": { "songid" : ' + xbmc.getInfoLabel('MusicPlayer.DBID') + ', "userrating": ' + sys.argv[1] + ' }}'
        # xbmc.log('music.userrating JOSN call:  ' + jsonNew)
        jsonResponse = xbmc.executeJSONRPC(jsonNew)
        # xbmc.log('music.userrating response:  ' + jsonResponse)
        if jsonResponse and ('OK' in jsonResponse):
            # My rating
            xbmc.executebuiltin('Notification(' + __addonname__ + ', ' + xbmc.getLocalizedString(38018) + ' : ' + sys.argv[1] + ', 3000, ' + xbmcgui.NOTIFICATION_INFO + ')')
        else:
            # Update failed
            xbmc.executebuiltin('Notification(' + __addonname__ + ', ' + xbmc.getLocalizedString(113) + ', 3000, ' + xbmcgui.NOTIFICATION_INFO + ')')
            

 # lock script to prevent duplicates
if (xbmcgui.Window(10000).getProperty(__addon_id__ + '_running') != 'True'):
    Rating()
    xbmcgui.Window(10000).clearProperty(__addon_id__ + '_running')
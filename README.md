# script.music.userrating

A simple addon to set the desired user rating 0 - 10 for a playing song.  This is an alternative to the "setrating" action which pops up a select dialog.

Usage (Kodi 18/19):

Install the script from zip

Script can be run from a skin using built-in "RunScript(script.music.userrating,n)" where n is a string representing integer 0 -10

Example:  bind a keyboard key

我使用的是一个7键的键盘作为播放器控制按钮配置如下：  
#/storage/.kodi/userdata/keymaps/mykeymap.xml
```
<keymap>
  <global>
    <keyboard>
      <f1>PlayerControl(Partymode(music))</f1>
      <f2>PlayPause</f2>
      <f3>PlayerControl(Previous)</f3>
      <f3 mod="longpress">Seek(-10)</f3>
      <f4>PlayerControl(Next)</f4>
      <f4 mod="longpress">Seek(10)</f4>
      <f5>VolumeDown</f5>
      <f6>VolumeUp</f6>
      <f7>RunScript(script.music.userrating,10)</f7>
      <f7 mod="longpress">PlayMedia(/storage/.kodi/userdata/playlists/music/000.xsp)</f7>
      <!-- <power>ShutDown()</power> -->
      <power>Suspend()</power>
    </keyboard>
  </global>
</keymap>  
```

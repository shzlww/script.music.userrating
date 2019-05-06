# script.music.userrating

A simple addon to set the desired user rating 0 - 10 for a playing song.  This is an alternative to the "setrating" action which pops up a select dialog.

Usage (Kodi 18/19):

Install the script from zip

Script can be run from a skin using built-in "RunScript(script.music.userrating,n)" where n is a string representing integer 0 -10

Example:  bind a keyboard key

'<visualisation>'
      '<keyboard>'
	     '<numpadthree>'RunScript(script.music.userrating,3)'</numpadthree>'
	'</keyboard>'
'</visualisation>'

	 

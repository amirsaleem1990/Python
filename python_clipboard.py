def t(n='', tt=''):
	import clipboard
	"""
	(integer, text) -> clipboard
	this function take 2 arguments
	1- n, by default empty string
	2- text
	combine these 2 arguments and copy the reslut to the clipboard, so you can paste to another file.  
	
	>>> t(49, 'The Holy Quran.mp4')
	49_The_Holy_Quran.mp4 # Note the resul is copied to clipbord, nothing you see on your screen.
	"""
	if n:
		clipboard.copy(str(n)+"-"+tt.replace(' ', '_').replace("'", '').strip()+'.mp4')
	else:
		if tt:
			clipboard.copy(tt.replace(' ', '_').replace("'", '').strip()+'.mp4')
		else:
			return "please Enter at least one argument"


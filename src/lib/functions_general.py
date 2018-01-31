import time
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")
speak.Rate = -2




def pp(message, mtype='INFO'):
	mtype = mtype.upper()

	if mtype == "ERROR":
		mtype = red.format(mtype)

	print '[%s] [%s] %s' % (time.strftime('%H:%M:%S', time.gmtime()), mtype, message)

def ppi(channel, message, username):
	print '[%s %s] <%s> %s' % (time.strftime('%H:%M:%S', time.gmtime()), channel, username.lower(), message)

def say(username,message):
	speak.Speak('%s dice: %s' %(username,message))
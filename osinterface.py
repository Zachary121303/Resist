import os

def testos():
	useros = 0
	try:
		os.system(r"cls")
		useros="win"
	except:
		os.system(r"clear")
		useros="unix"
	return useros

def clear():
	getos = testos()
	if getos =="win":
		os.system(r"cls")
	elif getos == "unix":
		os.system(r"clear")
	#clear screen
def exit():
	getos = testos()
	if getos =="win":
		os.system(r"exit")
	elif getos == "unix":
		os.system(r"exit")
	#exit
def pause():
	getos = testos()
	if getos=="win":
		os.system(r"pause")
	elif getos == "unix":
		os.system(r"echo press any key to continue")
		os.system(r"read pause")
	#pause
def pausenomessage():
	getos = testos()
	if getos=="win":
		os.system(r"pause")
	elif getos == "unix":
		os.system(r"read pause")
def copy(copypoint):
	getos = testos()
	if getos=="win":
		os.system(r"copy "+ copypoint)
	elif getos == "unix":
		os.system(r"cp " + copypoint)
	#copy





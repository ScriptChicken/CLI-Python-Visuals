import os
import time

# opt_frame, used with opt_title or without is used to create customizable frames around text.  This creates
# a more appealing looking CLI application and segregates data in a more orginazed way. An explanation of each input
# is below:

# opt_frame(list1,title,length,  q,   s,clr_scn,color,txt_color,ttl_color)
#           list^  str^  int^ str^ str^   int^  str^    str^     str^

# list1    - The list of variables that will make up the opt_box frame.  Used for multiline frames.
# title    - Used to create the single line title box text.
# length   - the amount of void inbetween the longest string and the sides of the frame.
# q        - The character (must always be a single character) used to draw the top and bottom frame line.
# s        - The character (or characters) tha make up the outside frame lines.
#clr_scn   - whether you want to clear the screen before creating or not - default is to clear (1), change to "0" if not wanted.
#color     - choose a color (see list below) to color the frame - default is 'white'
#txt_color - choose a color for the text - default is 'white'
#ttl_color - choose a color for the title text - default is 'white'

# Example #1 - visuals.opt_frame(var,title,20,"=","|!Game!|")

#  |!Game!|========================================================|!Game!|
#  |!Game!|                    Super Fun Game!                     |!Game!|
#  |!Game!|========================================================|!Game!|
#  |!Game!|========================================================|!Game!|
#  |!Game!|                                                        |!Game!|
#  |!Game!|                      1) New Game                       |!Game!|
#  |!Game!|                        2) Exit                         |!Game!|
#  |!Game!|                                                        |!Game!|
#  |!Game!|========================================================|!Game!|


# opt_bar, used as a sort of "loading" screen.  This tool displays the 'title' text and then starts an accending array of a
# a specific character, such as a '.' or '/'

# opt_bar(title,length,char,speed=1,clr_scn=0)
#	     str^  int^   str^  float^     int^

#title  - string - required - Text to display before the accending characters
#length - - not required - the amount of characters you would like the opt_bar to accend to.  Default - 10
#char   - not required - the accending character (or characters) you want to be printed.  Default - "."
#speed  - not required - the pause time inbetween each accending char. Default - 1
#clr_scn - not required - tells the function to clear the screen before running or not.  Default - "0" - not

# Example #1 - opt_bar(title="Loading",length=15,char="/",speed=.5,clr_scn=1)

# Output - Loading////////////////////



def opt_frame(list1,title="0", length=10, q="=", s="||",clr_scn=1,color="0",txt_color="0",ttl_color="0"):
	
	#variables
	title_lgth = 0
	list_lgth = 0
	ctr_lgth = 0

	if color != "0":
		setColor(color)

	if txt_color != "0":
		setTxtColor(txt_color)

	if ttl_color != "0":
		setTtlColor(ttl_color)

	if clr_scn == 1:
		os.system('cls')
		print("\n")


	title,title_lgth = doWork(title)
	list1,list_lgth = doWork(list1)

	if (title_lgth > list_lgth):
		ctr_lgth = title_lgth
	else:
			ctr_lgth = list_lgth
	opt_title(title, length, q, s, ctr_lgth)
	opt_box(list1, length, q, s, ctr_lgth)
	


#opt_title is either used by itself to create a title bar (single line string) or coupled with the opt_frame to create a title
#with a opt_box for the main data
def opt_title(title, length=10, q="=", s="||", ctr_lgth=0,title_lgth=0):

	#variables
	void_lgth = 0
	t_void = 0
	tst_border = 0
	tst_label = 0
	tst_result = 0
	extender = ""

	#sets the title length if it wasn't passed in from the frame module
	if title_lgth == 0:
		title_lgth = len(title)
	else:
		title_lgth = title_lgth

	#set the center length using the title's length if no variable was passed
	if ctr_lgth == 0:
		ctr_lgth = len(title)
	else:
		ctr_lgth = ctr_lgth

	#check that the t_void is not an odd number, if is, add 1
	t_void = (ctr_lgth - title_lgth) / 2
	t_void = round(t_void)

	tst_border = length + ctr_lgth + length
	tst_label = length + t_void + title_lgth + t_void + length
	tst_result = tst_border - tst_label

	#if the border length and the label length are off (due to an odd number) this adds a space at the end to match them up.
	if tst_result != 0:
		extender = " "


	#start printing the title bar.
	print(f"" + C.frame + s + (q * length) + (q * ctr_lgth) + (q * length) + s)
	print(f"" + s + (" " * length) + (" " * int(t_void)) + C.ttl + title + C.frame + (" " * int(t_void)) + (" " * length) + extender + s)
	print(s + q * length + q * ctr_lgth + q * length + s)


#not currently configurable without the opt_frame - later versions will allow running without a title box.
def opt_box(list1, length=10, q="=", s="||",ctr_lgth=0):

	#variables
	void_lgth = 0
	
	#calculate the void length, this is used for the void space below and over the actual text
	void_lgth = (length * 2) + int(ctr_lgth)  

	#start of printing the frame.
	print(s + q * length + q * ctr_lgth + q * length + s)
	print(s + " " * void_lgth + s)
	
	#loop through the list and print each row
	for row in list1:
		x = len(row)	
		t_void = (ctr_lgth - x) / 2
		print(s + " " * length + " " * int(t_void) + C.txt + row + C.frame + " " * int(t_void) + " " * length + s)
	
	#last of the printing for the frame, after the data.
	print(s + " " * void_lgth + s)
	print(s + q * length + q * ctr_lgth + q * length + s)


# if opt_box variables do not match even or odds, this function adds a space to the end of the odds so all entries match
# so that the frames right side lines up correctly.
def chkList(list1,title=""):

	for i in range(len(list1)):
  		lng = len(list1[i])
  		if lng % 2 != 0:
  			list1[i] = list1[i] + " "
	return(list1)


#Gets the length of either a string(the title) or the longest object in a list (the opt_box variables)
#If that object or string is found to be an odd number, it adds a space to the end
def doWork(data):
	if isinstance(data, list):
		data_lgth = 0
		data_lgth = max(data, key = len)
		data_lgth = len(data_lgth)

		if data_lgth % 2 != 0:
			data_lgth = data_lgth + 1
		data = chkList(data)
	else:
		data_lgth = len(data)
		if data_lgth % 2 != 0:
			data_lgth = data_lgth + 1
			data = data + " "
	
	return data,data_lgth


#simple loading bar customizable with the follow:
#title  - string - text to display before the accending characters
#length - int -the amount of characters you would like the opt_bar to display
#char   - string - the accending character (or characters) you want to be printed
#speed  - float - the pause time inbetween each accending char.
def opt_bar(title="Loading",length=10,char=".",speed=1,clr_scn=0):
		x = 0
		dots = [char]

		if clr_scn != 0:
			os.system('cls')
			print("\n")

		while x < length:
				print(f"" + C.bar + "   " + title,*dots, end='\r')
				time.sleep(speed)
				dots.append(char)
				x = x + 1
		print(f"" + C.frame)


#Color class
class C:
	frame = ""
	txt = ""
	bar = ""
	ttl = txt
	H = '\033[95m'
	B = '\033[94m'
	C = '\033[96m'
	G = '\033[92m'
	Y = '\033[93m'
	R = '\033[91m'
	P = '\033[95m'
	E = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'


def setColor(color):
	if color == "red":
		C.frame = C.R
	elif color == "green":
		C.frame = C.G
	elif color == "yellow":
		C.frame = C.Y
	elif color == "blue":
		C.frame = C.B
	elif color == "cyan":
		C.frame = C.C
	elif color == "white":
		C.frame = C.E
	elif color == "purple":
		C.frame = C.P

def setTxtColor(color):
	if color == "red":
		C.txt = C.R
	elif color == "green":
		C.txt = C.G
	elif color == "yellow":
		C.txt = C.Y
	elif color == "blue":
		C.txt = C.B
	elif color == "cyan":
		C.txt = C.C
	elif color == "white":
		C.txt = C.E
	elif color == "purple":
		C.txt = C.P

def setTtlColor(color):
	if color == "red":
		C.ttl = C.R
	elif color == "green":
		C.ttl = C.G
	elif color == "yellow":
		C.ttl = C.Y
	elif color == "blue":
		C.ttl = C.B
	elif color == "cyan":
		C.ttl = C.C
	elif color == "white":
		C.ttl = C.E
	elif color == "purple":
		C.ttl = C.P


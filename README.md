# Visuals - by ScriptChicken

 opt_frame, used with opt_title or without is used to create customizable frames around CLI prints.  This creates
 a more appealing look to your CLI application and segregates data in a more orginazed way. An explanation of each input
 is below:

 opt_frame(list1,title,length,  q,   s,clr_scn,color,txt_color,ttl_color)
           list^  str^  int^ str^ str^   int^  str^    str^     str^

list1    -  Required - The list of variables that will make up the opt_box frame.  Used for multiline frames.
title    - Required - Used to create the single line title box.
length   - the amount of void inbetween the longest string and the sides of the frame.
q        - The character (must always be a single character) used to draw the top and bottom frame line.
s        - The character (or characters) that make up the outside frame lines.
#clr_scn   - whether you want to clear the screen before creating or not - default is to clear (1), change to "0" if not wanted.
#color     - choose a color (see list below) to color the frame - default is 'white'
#txt_color - choose a color for the text - default is 'white'
#ttl_color - choose a color for the title text - default is 'white'

 Example #1 - visuals.opt_frame(var,title,20,"=","|!Game!|")

|!Game!|========================================================|!Game!|
|!Game!|                    Super Fun Game!                     |!Game!|
|!Game!|========================================================|!Game!|
|!Game!|========================================================|!Game!|
|!Game!|                                                        |!Game!|
|!Game!|                      1) New Game                       |!Game!|
|!Game!|                        2) Exit                         |!Game!|
|!Game!|                                                        |!Game!|
|!Game!|========================================================|!Game!|


 opt_bar, used as a sort of "loading" screen.  This tool displays the 'title' text and then starts an accending array of a
 a specific character, such as a '.' or '/'

 opt_bar(title,length,char,speed=1,clr_scn=0)
	     str^  int^   str^  float^     int^

title  - string - required - Text to display before the accending characters
length - - not required - the amount of characters you would like the opt_bar to accend to.  Default - 10
char   - not required - the accending character (or characters) you want to be printed.  Default - "."
speed  - not required - the pause time inbetween each accending char. Default - 1
clr_scn - not required - tells the function to clear the screen before running or not.  Default - "0" - not

 Example #1 - opt_bar(title="Loading",length=15,char="/",speed=.5,clr_scn=1)

 Output - Loading////////////////////
 end

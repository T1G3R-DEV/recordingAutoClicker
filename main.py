 
import platform
import webbrowser
#import pyautogui as pg #python -m pip -insatll pyautogui
import keyboard as kb #https://pypi.org/project/keyboard/
import time
import datetime
import mouse


print("Interaction capture by T1G3R  \n\n")
print("import platform\nimport webbrowser\nimport pyautogui as pg \nimport keyboard as kb \nimport time\nfrom pynput.mouse import Button, Controller\n\nmouse = Controller() \nkb.press(\"a\")\nkb.release(\"a\")")

lockpress= False
keymap=[0]*256
now = time.time()
while True:


	if(mouse.is_pressed("left")):
		if  (lockpress==False):
			lockpress= True
			later = time.time()
			difference = later - now
			print("time.sleep(" + str(difference+0.2) + ")")
			print("mouse.position=("+ str(mouse.get_position()[0]) +","+ str(mouse.get_position()[1])+")\nmouse.click(Button.left, 1)")
			now = time.time()
	else:
		lockpress= False

	i=0;
	for i in range(255):
		if(kb.is_pressed(i) != keymap[i]):
			later = time.time()
			difference = later - now
			print("time.sleep(" + str(difference+0.2) + ")")
			now = time.time()
			keymap[i] = kb.is_pressed(i)

			if(keymap[i]):
				print("kb.press(" + str(i) + ")")
				if(i==1):
					print("Thanks for using!")
					exit()
			else:
				print("kb.release(" + str(i) + ")")





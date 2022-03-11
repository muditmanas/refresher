import pyautogui as dp
import time

def countdown(t=300): #adjust this "t" according to the time you want the system to refresh itself.
	while t:
		mins, secs = divmod(t, 60)
		timer = '{:02d}:{:02d}'.format(mins, secs)
		print(timer, end="\t\r")
		time.sleep(1)
		t -= 1
i=1
while i!=0:
    dp.hotkey('win', 'd')
    time.sleep(1)
    dp.position(x = 1920,y =540)
    dp.click(x = 1920,y =540,button = 'right')
    # dp.click(x = 1800,y =600)
    dp.click(x = 1900,y =620)
    print("\n",i,"\n")
    i+=1
    countdown()    

#Autor HugoIP
#Date: 04 th April 2021
import threading, time
#Depends pip install playsound
from playsound import playsound


print("Hello Kareli")

def callInitSoud():
	#call soud
	print ("call")
	file = "/sounds/IntroEveryHour.mp3"
	##os.system("mpg123" + file)
	playsound('sounds/IntroEveryHour.mp3')

def callInitTink():
	#call soud
	playsound('sounds/Tink.mp3')


callInitSoud()
time.sleep(2)

callInitTink()
time.sleep(1)
callInitTink()
time.sleep(1)
callInitTink()
time.sleep(1)
callInitTink()
time.sleep(1)
callInitTink()
time.sleep(1)
callInitTink()
time.sleep(1)
callInitTink()
time.sleep(1)
callInitTink()
time.sleep(1)
callInitTink()
time.sleep(1)
callInitTink()
time.sleep(1)
callInitTink()
time.sleep(1)
callInitTink()
time.sleep(1)
callInitTink()
#time.sleep(6)
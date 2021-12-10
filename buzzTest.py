import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
buttonPin = 29
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
Buzzer = 11
CL = [0, 131, 147, 165, 175, 196, 211, 248]		# Frequency of Low C notes

CM = [0, 262, 294, 330, 350, 393, 441, 495]		# Frequency of Middle C notes

CH = [0, 525, 589, 661, 700, 786, 882, 990]		# Frequency of High C notes
song_1 = [	CH[3], CH[5], CH[6], CH[6], CH[5], CH[3], CM[3], CM[5], CM[6], CM[6], CM[5], CM[3]]
beat_1 = [1,2,2,2,1,1,1,2,2,2,1,1]
def buzzsetup():
	GPIO.setmode(GPIO.BOARD)		# Numbers GPIOs by physical location
	GPIO.setup(Buzzer, GPIO.OUT)	# Set pins' mode is output
	global Buzz						# Assign a global variable to replace GPIO.PWM
	Buzz = GPIO.PWM(Buzzer, 440)	# 440 is initial frequency.
	Buzz.start(50)
def buzzdestroy():
	Buzz.stop()					# Stop the buzzer
	GPIO.output(Buzzer, 1)

def buzzloop(pin,song, beat):
  i = 0
  if pin == 0:
    Buzz.ChangeFrequency(song)	# Change the frequency along the song note
    time.sleep(beat)
  if pin == 1:
    i+=1
    time.sleep(30)
  if pin == 1 and i == 1:
    buzzdestroy()
    i=0




buzzsetup()
try:
  for i in range(1, len(song_1)):
    buzzloop(GPIO.input(buttonPin),song_1[i], beat_1[i])
except KeyboardInterrupt:
  buzzdestroy()


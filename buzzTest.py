import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
buttonPin = 29
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
Buzzer = 11
CL = [0, 131, 147, 165, 175, 196, 211, 248]		# Frequency of Low C notes

CM = [0, 262, 294, 330, 350, 393, 441, 495]		# Frequency of Middle C notes

CH = [0, 525, 589, 661, 700, 786, 882, 990]		# Frequency of High C notes
song_1 = [	CH[3], CH[5], CH[6], CH[6], CH[5], CH[3], CM[3], CM[5], CM[6], CM[6], CM[5], CM[3],CH[3], CH[5], CH[6], CH[6], CH[5], CH[3], CM[3], CM[5], CM[6], CM[6], CM[5], CM[3],CH[3], CH[5], CH[6], CH[6], CH[5], CH[3], CM[3], CM[5], CM[6], CM[6], CM[5], CM[3],CH[3], CH[5], CH[6], CH[6], CH[5], CH[3], CM[3], CM[5], CM[6], CM[6], CM[5], CM[3],CH[3], CH[5], CH[6], CH[6], CH[5], CH[3], CM[3], CM[5], CM[6], CM[6], CM[5], CM[3]]


mysong = [262,294,330,262,262,294,330,262,330,349,392,330,349,392,392,440,392,349,330,262,392,440,392,349,330,262,262,196,262,262,196,262]
beat = [0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,1,0.5,0.5,1,0.25,0.25,0.25,0.25,0.5,0.5,0.25,0.25,0.25,0.25,0.5,0.5,0.5,0.5,1,0.5,0.5,1]

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
  if pin == 0:
    Buzz.ChangeFrequency(song)	# Change the frequency along the song note
    time.sleep(beat)
  if pin == 1:
    buzzdestroy()

buzzsetup()
try:
  for i in range(1, len(mysong)):
    buzzloop(GPIO.input(buttonPin),mysong[i], beat[i])
    
except KeyboardInterrupt:
  buzzdestroy()


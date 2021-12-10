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

notes = {"B0": 31,"C1": 33,"CS1": 35,"D1": 37,"DS1": 39,"E1": 41,"F1": 44,"FS1": 46,"G1": 49,"GS1": 52,"A1": 55,"AS1": 58,"B1": 62,"C2": 65,"CS2": 69,"D2": 73,"DS2": 78,"E2": 82,"F2": 87,"FS2": 93,"G2": 98,"GS2": 104,"A2": 110,"AS2": 117,"B2": 123,"C3": 131,"CS3": 139,"D3": 147,"DS3": 156,"E3": 165,"F3": 175,"FS3": 185,"G3": 196,"GS3": 208,"A3": 220,"AS3": 233,"B3": 247,"C4": 262,"CS4": 277,"D4": 294,"DS4": 311,"E4": 330,"F4": 349,"FS4": 370,"G4": 392,"GS4": 415,"A4": 440,"AS4": 466,"B4": 494,"C5": 523,"CS5": 554,"D5": 587,"DS5": 622,"E5": 659,"F5": 698,"FS5": 740,"G5": 784,"GS5": 831,"A5": 880,"AS5": 932,"B5": 988,"C6": 1047,"CS6": 1109,"D6": 1175,"DS6": 1245,"E6": 1319,"F6": 1397,"FS6": 1480,"G6": 1568,"GS6": 1661,"A6": 1760,"AS6": 1865,"B6": 1976,"C7": 2093,"CS7": 2217,"D7": 2349,"DS7": 2489,"E7": 2637,"F7": 2794,"FS7": 2960,"G7": 3136,"GS7": 3322,"A7": 3520,"AS7": 3729,"B7": 3951,"C8": 4186,"CS8": 4435,"D8": 4699,"DS8": 4978}
mario = ["E6","E6","E6",
"C6","E6","G6","G5",
"C6","G5","E5",
"A5","B5","B5", "A5"
"G5", "E6","G6","A6",
"F6","G6","E6","C6","D6","B5"
"C6","G5","E5",
"A5","B5","B5","A5",
"G5","E6","G6","A6",
"F6","G6","E6","C6","D6","B5",
"G6","FS6","F6","D6","E6",
"G5","A5","C6",
"A5","C6","D6",
"G6","FS6","F6","D6","E6",
"C7","C7","C7"
"G6","FS6","F6","D6","E6",
"G5","A5","C6",
"A5","C6","D6",
"DS6","D6","C6",
"C6","C6","C6",
"C6","D6","E6","C6","A5","G5"
"C6","C6","C6",
"C6","D6","E6",
"C6","C6","C6",
"C6","D6","E6","C6","A5","G5",
"E6","E6","E6",
"C6","E6","G6",
"G5",
"C6","G5","E5",
"A5","B5","B5","A5",
"G5","E6","G6","A6",
"F6","G6","E6","C6","D6","B5",
"C6","G5","E5",
"A5","B5","B5","A5",
"G5","E6","G6","A6",
"F6","G6","E6","C6","D6","B5",
"E6","C6","G5",
"G5","A5","F6","F6","A5",
"B5","A6","A6","A6","G6","F6",
"E6","C6","A5","G5",
"E6","C6","G5",
"G5","A5","F6","F6","A5",
"B5","F6","F6","F6","E6","D6","C6",
"G5","E5","C5",
"C6","G5","E5",
"A5","B5","A5",
"GS5","B5","GS5",
"G5","FS5","G5"
]
def buzzsetup():
	GPIO.setmode(GPIO.BOARD)		# Numbers GPIOs by physical location
	GPIO.setup(Buzzer, GPIO.OUT)	# Set pins' mode is output
	global Buzz						# Assign a global variable to replace GPIO.PWM
	Buzz = GPIO.PWM(Buzzer, 440)	# 440 is initial frequency.
	Buzz.start(50)
def buzzdestroy():
	Buzz.stop()					# Stop the buzzer
	GPIO.output(Buzzer, 1)


def buzzloop(pin,song):
  if pin == 0:
    Buzz.ChangeFrequency(int(song))	# Change the frequency along the song note
    time.sleep(0.5)
  if pin == 1:
    buzzdestroy()

buzzsetup()
try:
  for i in range(1, len(mysong)):
    buzzloop(GPIO.input(buttonPin),notes[mario[i]])
    
except KeyboardInterrupt:
  buzzdestroy()


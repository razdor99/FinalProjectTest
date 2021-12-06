#!/usr/bin/python37all
import requests
from datetime import datetime, timedelta
import urllib.parse
import json
import pytz
import RPi.GPIO as GPIO
import time
import json
from calendardata import get_busy_times_from_google_calendar

while True: #runs continuously
  with open('final.txt', 'r') as f: #opens json dump file
    data = json.load(f) #sets data to be loaded from json dump file
    m = [data['mhours'],data['mmins'],data['mtime']]
    n = [data['nhours'],data['nmins'],data['ntime']]
    r = [data['rhours'],data['rmins'],data['rtime']]
  timezone = pytz.timezone(LOCAL_TIMEZONE)
  now = timezone.localize(datetime.now())
  currenthour = now.strftime("%H")
  currentminute = now.strftime("%M")
  busy_times, wake, currentday = get_busy_times_from_google_calendar()

  if int(currenthour) == 23:
    if int(currentminute) == 0:
      busy_times, wake, currentday = get_busy_times_from_google_calendar()
      hour = [wake[0]]
      minute = [wake[1]]
      h = 1
      m = 15
      morningh = int(wake[0])- h
      morningm = int(wake[1])- m
      if morningm < 0:
          morningh -= 1
          morningm = 60 - m
      if morningh < 0:
        morningh = 24 + morningh
      print(morningh, morningm)
      sh = 8
      sm = 30
      nighth = morningh - sh
      nightm = morningm - sm
      if nightm < 0:
          nighth -= 1
          nightm = 60 - sm
      if nighth < 0:
        nighth = 24 + nighth
      print(nighth, nightm)
      if int(currenthour) == int(nighth):
        if int(currentminute) == int(nightm):
          print('nightalarm') ###where alarm goes
      if int(currenthour) == int(morningh):
        if int(currentminute) == int(morningm):
          print('dayalarm')  ###where alarm goes
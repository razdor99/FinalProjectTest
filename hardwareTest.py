import LCD1602
import time
x = 'testing'
import pytz
from datetime import datetime, timedelta
while True:
  LOCAL_TIMEZONE = "America/New_York"
  timezone = pytz.timezone(LOCAL_TIMEZONE)
  now = timezone.localize(datetime.now())
  currenthour = now.strftime("%H")
  currentminute = now.strftime("%M")
  currentdayname = now.strftime("%a")
  currentday = now.strftime("%d")
  currentmonth = now.strftime("%b")
  currenthour = now.strftime("%H")
  currentminute = now.strftime("%M")
  currentyear = now.strftime("%y")
  y = '%s, %s %s, %s' % (currentdayname,currentmonth, currentday,currentyear )
  LCD1602.init(0x27, 1)
  LCD1602.write(0, 0, x)
  LCD1602.write(0, 1, y)
  time.sleep(30)
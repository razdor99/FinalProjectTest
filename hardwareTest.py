import LCD1602
import time
x = 'testing'

while True:
  LCD1602.init(0x27, 1)
  LCD1602.write(0, 0, x)
  LCD1602.write(0, 1, 'REXQUALIS!')
  time.sleep(30)
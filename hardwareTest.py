import LCD1602

while True:
  LCD1602.init(0x27, 1)
  LCD1602.write(4, 0, 'Hello')
  LCD1602.write(7, 1, 'REXQUALIS!')
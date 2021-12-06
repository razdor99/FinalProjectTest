import LCD1602

while True:
  LCD1602.init(0x27, 1)
  LCD1602.write(0, 0, 'Hello')
  LCD1602.write(0, 1, 'REXQUALIS!')
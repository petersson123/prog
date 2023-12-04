svar = int (input("gissa på ett tal: "))
while svar != 42:
  if svar > 42:
    print("det är för stort")
    svar = int (input("gissa på ett nytt tal: "))
  elif svar < 42:
    print("det är för litet")
    svar = int (input("gissa på ett nytt tal: "))
print("rätt")
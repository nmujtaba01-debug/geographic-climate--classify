temperatures = [12, 28, 36, 18, 40]
 
def weather(temp) :

  if temp  <= 15:
    print(temp,'cold region')
  elif temp >= 15 and temp < 30:
    print(temp,'moderate region')
 
  else :
    print(temp,'hot region')  


for temp in temperatures:
  weather(temp)

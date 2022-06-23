import random 
cashmoney = float(input("Ayo how much money do you have?\n" ))
want ='y'
while want == 'y':
  print("You got " + str(cashmoney) + " dollars left.")
  cbet= float(input("Ayo how much money do you want to bet? \n")) 
  if cbet > cashmoney:
    print("Go home, you're out")
    break
  cashmoney-= cbet
  ctile = int(input("Pick a number between 1 and 36: "))
  for n in range(0,random.randrange(3,10)):
    print("Spinning...")
  cnumber = random.randrange(1,37,1)
  print("And the winner is " + str(cnumber))
  if cnumber ==ctile:
    cashmoney += cbet*35
    print("Congratulations!")
  else:
    print("Oh no!")
  want = input("Do you want to try again? (y/n)")

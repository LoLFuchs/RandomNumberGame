from random import *
import time
play = True
z1 = 10000000
#FunFact List
FunFact = ["My record is 6","This programm needed less then 100 lines code","This is my first Programm ever", "If you type the same number in row, youll get a message","If you type the same number in a row ,it wont cost you score","If you type 0 it wont tell you if it is to high or to low, i dont know why XD", "My first programming language was HTML, pyhton was just the second","made 25.02.2023","I made this game because i had to much time","This is no Fun Fact","I think python is the simplest programming language","im 15 at the moment","this is Fun Fact number 13",]

print("Game Rules: ")
time.sleep(1)
print("")
time.sleep(1)
print("Hello C:")
print("This is a Random Number game, were you have to guess the right number.")
print("The System will tell you if your Number was to high or to low, then you can try again.")
print("Have Fun :D")
print(" ")
time.sleep(3) 
        #GAME

while play == True:                                    

  Score = 1
  x = randint(1,100)                                   # x = random Number
  #print(x) #ONLY FOR TESTS

  y = 0                                                #z = random Message pick
  y1 = y 
  print("Your Number:")
  y = int(input())                                      # y = User pick
  

  while x != y:   # check if y = x 
      
      if y == 0:
          print("Try again:")
          y  = int(input())

      if y1 == y:
        print("YOU HAD THIS ONE JUST A SECOND AGO ._. ") 
        y = 0 
      elif  y > x: 
        print("Too Big")
        time.sleep(1)
        Score = Score + 1 
        y1 = y                                     #Number befor set 
        y = 0
      elif y < x: 
        print("to small")
        time.sleep(1)
        Score = Score + 1 
        y1 = y                                     #Number befor set
        y = 0
  
  # WON SCREEN
  z = randint(0,12) 
  if z1 == z:                                     #Not the same Fun Facts in a row
    z = z + 1 
  z1 = z  
  print("YOU WON, it was: " + str(x)) 
  time.sleep(1)
  print("You needed : " + str(Score) + " trys")
  time.sleep(1)
  if Score < 6: 
    print("YOU BROKE MY RECORD :O")
    time.sleep(1)
    print("My record is: 6")
    time.sleep(1)
    print("Your Score is: " + str(Score))
  else:
    print(" ")
    time.sleep(1)
    print("Fun Fact:")                              #Fun Fact Output
    time.sleep(1)
    print(FunFact[z])
  
  time.sleep(1)
  print(" ")
 
 

  
  #Again?
  time.sleep(1)
  print("wanna play again?(yes/no)")
  

  Nochmal = input()
  if Nochmal == "yes" or Nochmal == "ja": 
    play = True 
  elif Nochmal == "no" or "nein": 
    play = False
   
  if play == False: 
    print("Creator = LoLFuchs")
    time.sleep(3)
    quit()

    

import random

number = random.randint(1,9)
chances = 5
guess = input("guess the number between 1 to 9 - ")

while chances < 5 :
     
     if guess == number:
          print("Congratulations YOU WON")
          break
if not chances < 5 :
            print("you lose! ! ! the number is" , number)

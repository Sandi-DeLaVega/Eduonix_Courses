"""
Eduonix Project for Introduction to Pythonfor AI and Machine learning
Author: Sandi De La Vega
"""
import random

games = ''

while games == '':
    try:
        #ask the user how many games they would like to play
        games = int(input("How many games would you like to play? "))
    except:
        print("Please select using a number")
   
for game in range(0,games):
    print("Game: ", game + 1)
    
    #ask the player to select a random number between 1 - 25
    pick = random.randint(1,26)
    
    guess = None
    attempts = 0
    guess_list = []
    while pick != guess:
        try:
            guess = int(input("Pick a number between 1 to 25: "))
            
        except:
            print("Please select a number.")
            continue
        
        if guess > 25:
            print("Please choose 25 or below.")
        elif guess < 1:
            print("Please choose only between 1 to 25")
            
        else:
            if guess in guess_list:
                print("You have already picked the number: ", guess)
        
            else:
                if guess != pick:
                    attempts += 1
                    guess_list.append(guess)
                    #inform player if the number is higher or lower
                    if guess > pick:
                        print("Too high")
                    else:
                        print("Too low")
                else:   
                    #When user guesses right, how many guesses it took
                    print("Game: ", game + 1)
                    print("Correct! It took you this many guesses: ", attempts)

                    if attempts > 0:                        
                        string1 = ''
                        for i,g in enumerate(guess_list):
                            if i == 0:
                                string1 = string1 + " "+ str(g)
                            else:
                                string1 = string1 + " , "+ str(g)
                                
                        if len(guess_list) == 1:
                            print("You have guessed the number: ", string1)
                        else:
                            print("You have guessed the numbers: ", string1)
                            

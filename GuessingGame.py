import random

def play_game():
    secret = random.randint(1, 100)
    attempts = 0
    guessed = False
    
    print("Guess a number between 1 and 100")
    while not guessed:
    
        nmbr = int(input("Enter your guess: "))
        attempts += 1
        
        if nmbr < secret:
            print("Your guess is too low!")
            
        elif nmbr > secret:
            print("Your guess is too high!")
        else:
            print(f"Congratulations you guessed it! It took you {attempts} attempts.")
            guessed = True  # This breaks the loop and ends the game
                
play_game()

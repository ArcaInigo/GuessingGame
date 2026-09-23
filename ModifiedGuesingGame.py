import random

def play_game():
    end_game = False
    best = 0
    while not end_game:
        min = int(input())
        max=int(input())
        secret = random.randint(min,max)
        attempts = 0
        guessed = False
        score = 100
        print(f"Guess a number between {min} and {max}")
        while not guessed and attempts < 7: #Set a limit of 7 attempts
            nmbr = int(input("Enter your guess: "))
            attempts += 1
            score -= 10
            if nmbr < secret:
                print("Your guess is too low!")
            elif nmbr > secret:
                print("Your guess is too high!")
            elif nmbr == secret:
                print(f"Congratulations you guessed it! It took you {attempts} attempts.")
                if score > best:
                    best = score
                print (f"score: {score}")
                print (f"Best score: {best}")
                
                guessed = True
        # User ran out of guesses
        if not guessed:
            print(f"Game over! You ran out of attempts. The number was {secret}.\n")
            if score > best:
                best = score
            print (f"score: {score}")
            print (f"Best score: {best}")
        # ask user to play New game
        play = input("Play again? (yes/no): ")
        if play != "yes":
            print("Thanks for playing!")
            end_game = True # This breaks the outer loop and exits the game
play_game()

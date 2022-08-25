import random

print("NUMBER GUESSING GAME")
guesses = 7
no_of_guesses = 0

while True:
    num = random.randrange(1,100)
    while no_of_guesses<guesses:
        player_guess = int(input("enter ur guess\t\t"))
        try:
            if player_guess < num:
                if player_guess + 50 < num:
                    print("Too Low")
                    no_of_guesses+=1
                else:
                    print("Low")
                    no_of_guesses+=1
            elif player_guess > num:
                if player_guess - 50 > num:
                    print("Too High")
                    no_of_guesses+=1
                else:
                    print("High")
                    no_of_guesses+=1
            else:
                break
        except ValueError:
            print("Wrong Input") 
            continue 
        
    if (player_guess==num):
        print(f"CONGO CONGRATS. U GUESSED {num} NUMBER IN {no_of_guesses} GUESSES")  
    else:
        print(f"Ur out of guesses. The number was {num}")

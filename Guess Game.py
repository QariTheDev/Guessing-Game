import random
number = random.randint(0,10)

no_of_guess = 0
while no_of_guess<5:
    print("Enter Number b/w 0 and 10")
    guess = int(input())
    no_of_guess+=1
    if (guess>0 and guess<10):
        if(guess<number):
            print("Low")
        elif(guess>number):
            print("High")
        elif(guess==number):
            break

    else:
        print("wrong input")

if guess == number:
    print(f"Congrats u guessed number {number} in {no_of_guess} guesses")
else:
    print(f"U failed. The Number was {number}") 

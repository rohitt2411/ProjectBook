import random as r

num = r.randrange(100)
Guess = 6

while Guess >=0:

    your_guess = int(input("Enter your guess :"))

    def check(x):

        if your_guess == x:

            print ("CONGRATULATIONS, YOU WIN THE GAME.")
            
        elif your_guess > x:

            print ("You are close, keep trying Lower...")

        else:

            print ("You are close, keep trying Higher...")

    if Guess > 1:

        check (num)

    elif Guess == 1:

        check (num)

        print ("This is your last chance, make the most of it!!!")

    else:

        print ("Sorry, you lost.")

    Guess = Guess - 1

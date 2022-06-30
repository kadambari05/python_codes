import random
r=random.randint(1,50)
guess=None
while guess!=r:
    guess=int(input("Enter your guess"))
    if (guess<r):
        print("guess is too low!")
    elif (guess>r):
        print("guess is too high")
else:
        print("you won!")

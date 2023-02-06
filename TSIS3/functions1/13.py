import random
def guess_the_number(s):
    rand = random.randint(1, 20)
    print("Hello! What is your name?")
    name = input()
    t = "Well, {}, I am thinking of a number between 1 and 20."
    print(t.format(name))
    print("Take a guess.")
    n = 1
    guesses = 0
    while rand != n:
        vvod = int(input())
        guesses +=1
        if vvod > rand:
            print("Your guess is too high.")
            print("Take a guess")
        elif vvod < rand:
            print("Your guess is too low.")
            print("Take a guess.")
        else:
            p = "Good job, {}! You guessed my number in {} guesses!"
            print(p.format(name, guesses))
guess_the_number()           
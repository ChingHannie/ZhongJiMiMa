import random
# set random number
number = random.randint(0, 500)
# initialize start and ending number
start = 0
end = 501
while start != number and end!= number:
    guess = int(input("Guess between {} and {}: ".format(start+1, end-1)))
    if guess > start and guess < end:
        if guess == number:
            print("You lose")
            break
        elif guess < number:
            start = guess
        else:
            end = guess
    else:
        print("Invalid guess. ")

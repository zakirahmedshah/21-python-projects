import random
type_of_range = input("Type a number: ")

if type_of_range.isdigit():
    type_of_range = int(type_of_range)
    if type_of_range <= 0:
        print("Please type a number larger than 0 next time.")
        exit()

random_number = random.randint(0, type_of_range)
print(random_number)
while True:
    user_guess = input("make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("please type a number next time: ")
        continue
    if user_guess == random_number:
        print("you got it")
    else:
        print("you got it wrong")
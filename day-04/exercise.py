name = input("what is your name: ")
age = int(input("How old are you: "))
future_age = age + 10
print(f"Hello {name}, in 10 years you will be {future_age} years old.")
print(f"_________________________________\n")

#get 2 numbers and print their sum, difference, product, and quotient
num_one = int(input("pick a random number: "))
num_two = int(input("pick another random number:"))
print(f"The sum of {num_one} and {num_two} is {num_one + num_two}")
print(f"The difference of {num_one} and {num_two} is {num_one - num_two}")
print(f"The product of {num_one} and {num_two} is {num_one * num_two}")
print(f"The quotient of {num_one} and {num_two} is {num_one / num_two}")
print(f"_________________________________\n")

#ask for a number and print if its positive, negetive, or zero
num = int(input("pick a number: "))
if num >= 1:
    print("positive")
elif num == 0:
    print("zero")
else:
    print("negetive")
print(f"_________________________________\n")

#print even numbers from 1 to 50
print("even numbers from 1-50")
for i in range (0, 50, 2):
    print(i)
print(f"_________________________________\n")

# pick a number and print its times table from 1 to 12
num = int(input ("pick a number: "))
for i in range(1, 13):
    print(f"{num} x {i} = {num * i}")
print(f"_________________________________\n")

# add numbers 1 to 100 and print a total
total = 0
for i in range(1, 101):
    total += i
print(f"The total of adding up numbers 1-100: {total}")
print(f"_________________________________\n")

# ask for a number and calculate its factorial
num = int(input("pick a number: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i
print(f"The factorial of {num} is {factorial}")
print(f"_________________________________\n")

# Number guessig game
guess_num = 7
while guess_num != "7":
    guess = int(input("This is a guessing game. Guess a number between 1-20: "))
    if guess == guess_num:
        break
        print("Yay!!! You got it rigt!")
    elif guess < guess_num:
        print("too low")
    else:
        print("too high")
print(f"_________________________________\n")

# make a pattern
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()
print(f"_________________________________\n")
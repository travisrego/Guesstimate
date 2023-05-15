import random
import time

print("Welcome to Guesstimate")
print("Choose the game mode you want")

# List of Modes 
print("1. Casual Mode")
print("2. Rapid Fire Mode")
print("3. Challenge Mode")
print("4. Custom Mode")
print("5. Help")

# Selection of Mode 
while True:
    try:
        mode_Selection = int(input("Which mode would you like to play: "))
        break
    except ValueError:
        print("Please type a valid option")
        continue

# Casual Mode
if mode_Selection == 1:
    tries = 0
    isWon = False 
    rdm = random.randrange(1, 10)
    print(rdm)
    while tries < 5: 
        tries += 1
        print("Attempt:", tries)
        while True:
            try:
                usrInput = int(input("Please type your guess, it should be between 1 and 10: "))
                if usrInput > 10 or usrInput < 1:
                    print("Please type a number between 1 and 10")
                    continue
                break
            except:
                print("Please type a numeric value")
                continue
        if usrInput == rdm:
            print("You guessed the number!")
            isWon = True
            break
        elif usrInput > rdm:
            print("Lower!")
            continue
        elif usrInput < rdm:
            print("Higher!")
            continue
    
    if isWon:
        print("You have won!")
    else:
        print(f"You have lost! The number was {rdm}")

# Rapid Fire Mode
elif mode_Selection == 2:
    tries = 0
    isWon = False 
    rdm = random.randrange(1, 10)
    print(rdm)
    start_time = time.time()
    while tries < 5 and time.time() - start_time <= 30:        
        tries += 1
        print("Attempt:", tries)
        while True:
            try:
                usrInput = int(input("Please type your guess, it should be between 1 and 10: "))
                if usrInput > 10 or usrInput < 1:
                    print("Please type a number between 1 and 10")
                    continue
                break
            except:
                print("Please type a numeric value")
                continue
        if usrInput == rdm:
            print("You guessed the number!")
            isWon = True
            break
        elif usrInput > rdm:
            print("Lower!")
            continue
        elif usrInput < rdm:
            print("Higher!")
            continue
    
    if time.time() - start_time > 30:
        print("Times Up!")
    elif isWon and not time.time() - start_time > 30:
        print("You have won!")
    else:
        print(f"You have lost! The number was {rdm}")


# Challenge Mode
elif mode_Selection == 3:
    tries = 0
    isWon = False 
    rdm = random.randrange(1, 20)
    print(rdm)
    start_time = time.time()
    while tries < 5 and time.time() - start_time <= 30:        
        tries += 1
        print("Attempt:", tries)
        while True:
            try:
                usrInput = int(input("Please type your guess, it should be between 1 and 20: "))
                if usrInput > 20 or usrInput < 1:
                    print("Please type a number between 1 and 10")
                    continue
                break
            except:
                print("Please type a numeric value")
                continue
        if usrInput == rdm and not time.time() - start_time > 30:
            print("You guessed the number!")
            isWon = True
            break
        elif usrInput > rdm:
            print("Lower!")
            start_time -= 3;  
            continue
        elif usrInput < rdm:
            print("Higher!")
            start_time -= 3;
            continue
    
    if time.time() - start_time > 30:
        print("Times Up!")
    elif isWon and not time.time() - start_time > 30:
        print("You have won!")
    else:
        print(f"You have lost! The number was {rdm}")

# Custom Mode
elif mode_Selection == 4:
    tries = 0
    isWon = False 
    while True:
        x = int(input("Please type the first number: "))
        if x < 1:
            print("Please type valid numbers. The first number should be smaller than the second number, and both should be greater than or equal to 1.")
            continue
        y = int(input("Please type the second number: "))
        if x >= y or x < 1 or y < 1:
            print("Please type valid numbers. The first number should be smaller than the second number, and both should be greater than or equal to 1.")
            continue
        else:
            break
            
    attempts = int(input("Please type the number of attempts: "))
    rdm = random.randrange(x, y)
    print(rdm)
    while tries < attempts: 
        tries += 1
        print("Attempt:", tries)
        while True:
            try:
                usrInput = int(input(f"Please type your guess, it should be between {x} and {y}: "))
                if usrInput > y or usrInput < x:
                    print(f"Please type a number between {x} and {y}")
                    continue
                break
            except:
                print("Please type a numeric value")
                continue
        if usrInput == rdm:
            print("You guessed the number!")
            isWon = True
            break
        elif usrInput > rdm:
            print("Lower!")
            continue
        elif usrInput < rdm:
            print("Higher!")
            continue

    if isWon:
        print("You have won!")
    else:
        print(f"You have lost! The number was {rdm}")

# Help
elif mode_Selection == 5:
    print("Guesstimate is a number guessing game with different modes:")
    print("1. Casual Mode: Guess a number between 1 and 10 within 5 attempts.")
    print("2. Rapid Fire Mode: Guess a number between 1 and 10 within 5 attempts and 30 seconds.")
    print("3. Challenge Mode: Guess a number between 1 and 20 within 5 attempts and 30 seconds. Every incorrect guess reduces the time.")
    print("4. Custom Mode: Set a custom range and guess a number within custom number of attempts.")
    print("Choose a mode by entering the corresponding number.")
else:
    print("Invalid mode selection.")
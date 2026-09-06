import random

random_number = random.randint(1, 100)
total_attempt =7
attempt_used= 0
print(random_number)

while True:
    guess_number= input("Enter number:  ")
    if guess_number.lower() == "quit":
        break
    guess= int(guess_number)
    total_attempt -=1
    if guess > random_number:
        print("Too high! 🔼")
        print ( f"You have {total_attempt} attempts left")
    elif guess < random_number:
        print("Too low! 🔽")
        print ( f"You have {total_attempt} attempts left")

    attempt_used +=1
    if guess==random_number:
        print( f"🎉 You got it in {attempt_used} attempts!")
        choice =input("Restart the game? (y/n)")
        if choice=="y":
            continue
        elif choice=="n":
            break
        else:
            print ("Invalid input")
    elif attempt_used==7:
        print( f"💀 Game over! The number was {random_number}")
        

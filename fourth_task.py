import time
import random as rd

print("Welcome to Rock, Paper, Scissors")

cd = ["rock", "paper", "scissors"]
x = input("Enter your choice ('rock', 'paper', 'scissors')\n").lower()
while True:
    if x == 'exit':
        print("Thank you for giving your valuable time")
        time.sleep(2)
        break
    
    com = rd.choice(cd)
    print(f"Computer chose: {com}")

    if x == com:
        print("It's a tie!")
    elif (com == 'scissors' and x == 'paper') or (com == 'paper' and x == 'rock') or (com == 'rock' and x == 'scissors'):
        print("You lose")
    elif (com == 'paper' and x == 'scissors') or (com == 'rock' and x == 'paper') or (com == 'scissors' and x == 'rock'):
        print("You win")
        print("if you want to continue then you can press 1 or 0")
        g = input("1 or 0\n")
        if (g=='1'):
            x = input("Enter your choice ('rock', 'paper', 'scissors')\n").lower()
            continue    
        else:
            break
    else:
        print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
    
    x = input("Enter your choice ('rock', 'paper', 'scissors') or type 'exit' to quit:\n").lower()
    time.sleep(2)

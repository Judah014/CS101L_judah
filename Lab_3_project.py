import math
import random


def_val = float(1000)
print("Welcome to KC bank!")
print("")
attempts = int(0)

while True:
    print(f"KC Bank Menu:     Bank account balance: ${def_val:.2f}")
    print("_ _ _ _ _ _ _\n")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check balance")
    print("4. Exit")
    print("")
    user_input = int(input("->"))
   
    if user_input == 1:
        dep = float(input("Enter the amount you would like to Deposit: "))
        def_val += dep
        print("")
        print(f"New balance ${def_val}")
        print("")
    
    elif user_input == 2:
        wit = float(input("Enter the amount you would like to Withdraw: "))
        if def_val < wit:
            print("𝘌𝘳𝘳𝘰𝘳! 𝘵𝘩𝘦 𝘢𝘮𝘮𝘰𝘶𝘯𝘵 𝘦𝘯𝘵𝘦𝘳𝘦𝘥 𝘦𝘹𝘤𝘦𝘦𝘥𝘦𝘥 𝘣𝘢𝘯𝘬 𝘢𝘮𝘰𝘶𝘯𝘵")
            continue

        def_val -= wit
        print("") 
        print(f"New balance ${def_val}")
        print("")

    elif user_input == 3:
        print("Checking balance...")
        print("")
        print(f"${def_val}")
        print("")

    elif user_input == 4:
        print("Exiting bank menu...")
        break
    elif user_input > 4:
        print("Invalid option please enter a number between 1 and 4")
        attempts +=1

    if attempts >= 3:
        print("Maximmum number of attempts reached (3) Exiting bank...")
        break
    
        
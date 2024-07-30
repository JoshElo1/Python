import os
import time

# Main Function
def mainFunc():

    # Print
    print("Want to find out if a number is Even or Odd?")

    try:
        # Print and assign the User Input as an Integer
        userInput = int(input("Enter a Number: "))

        # Check if the number is divisible by 2 (if so 0 will be the remainder)
        if userInput % 2 == 0:
            print("This number is Even\n")
    
        # Otherwise
        else: 
            print("This number is Odd\n")

        # Wait 2 Seconds & Clear the screen
        time.sleep(2)
        os.system('cls')

    # If an invalid input is entered
    except ValueError:
        print("Invalid Input, try again.")

        # Wait 2 Seconds & Clear the screen
        time.sleep(2) 
        os.system('cls')

# Loop
while True: 
    
    # Call this Function
    mainFunc()
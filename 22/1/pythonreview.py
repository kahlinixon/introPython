# Sve this as pythonReview.py

# In your own words describe, what a computer program is?
#a computer program is a program that has a function for your computer


# In your own words, describe what it mean to call a function? 
#It means to tell the computer to run

# Create a elevator function that will run specific lines of code 
# based on the conditions provided by a user. If the user types in 101,
# the function should print out they are going to the boys latin office, 
# if they type in 203, they are going to the gym, 
# and if they type in the letter g, the lobby. else, 
# if the input doesnt match any of the values provided, 
# tell the user that floor doesn't exist and to please
# enter a valid floor number.
def elevator(floor):
    if floor == '101':
        print("You are going to the Boys Latin office.")
    elif floor == '203':
        print("You are going to the gym.")
    elif floor.lower() == 'g':
        print("You are in the lobby.")
    else:
        print("Floor doesn't exist. Please enter a valid floor number.")

# Example usage:
#user_input = input("Enter floor number or letter: ")
#elevator(user_input)

#user_input = input("Enter floor number or letter: ")
#elevator(user_input)
# Create a function that will do the following calculation.
# Your function should take in three argument. it should add the first
# two arguments and then the sum of the first two (2) should be divided 
# by the third argument. You function should then print the result.

def custom_calculation(arg1, arg2, arg3):
    result = (arg1 + arg2) / arg3
    print("Result:", result)


custom_calculation(1, 2, 3)

#you got to put the numbers next to custom calculation
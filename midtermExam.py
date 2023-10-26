
# 1. Describe what a computer program is and what does it do. 
'A computer program is  a sequence or set of instructions in a program.'
# 2. Describe what complexitity and abstraction are, then provide an example
# of complexity in the real world and how we apply abstraction to that thing (you example must be original and cannot be an example
# used in our lecture slides ie car, grocery store, etc.). 
'Complexitity and abstraction is a factor in a hard equation or sitution and abstraction is the ability to think about complex situations.and a example of abstraction is using a computer and not knowing what the computer does for the websites to work.'
# 3. What is Syntax in Python and why is it important to write proper syntax?
'Syntax in python is rules that mkes a python work and its important to have proper syntax because without proper syntaxx the code isnt going to work.'
# 4. What is a function, and why do we wrap our code inside of functions?
'A function is a code that runs and we wrap our code inside of a function because it can mess up the function'
# 5. Name and describe the three (3) naming conventions for variables in python? Then provide three (3) name rules for Python
# variables. 

# 6. What will be the output of the print functons when this code is ran, explain why
name = 'Bill'
student = name
name = 'Walter'
student= 'Richard'

print(name)
print(student)
'the output would be Walter and richard because if student=name and the name is walter and student is Richard then Richard and walter would be the output.'
# 7. Describe the difference between each of the following assignment operators:
# = 
# ==
# !=
'each one of them would do something diffrent as one only have 1 equal sign, 1 have 2, and 1 of them  have a exlamation mark.'
 
# 8. What type of data can be stored in a python list?
'All variables can be stored inside a python list'
# 9. Create a function that will take in a word provided by a user and then output that word back to the user but in reverse. fruits = ["apple", "banana", "cherry"]
def my_function(x):
  return x[::-1]

word = my_function("friend,foe")

print(word)

# 10. Create three (3) seperate functions that will do addition, subtraction, and multiplication respectively. 
# each of these functions should take two (2) arguments. When the user passes these arguments into the function, they will be
# calculated together and return the output in your terminal. 
def add(x, y):
    return x - y


def multiply(x, y):
    return x * y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")


while True:
    
    choice = input("Enter choice(1/2/3): ")

    if choice in ('1', '2', '3'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

       
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")

# 11. What is the difference between a function argument and a function parameter. 
'the diffrence between a function parameter and a function argument is that a function parameter is the names listed in the function definition while function arguments are the real values passed to and received by the function.'
# 12. You have been hired by a software company and your first assignment is to develop a password authenticator program. 
# the goal of your program is to check a user's password and make sure it meets the company's password requirements. 
# the company has provided you with the following requirements for the passcode program:
# a. the passcode must NOT contain any numbers
# b. the passcode must NOT contain any capital letters
# c. the passcode can NOT be any longer than five (5) characters
# d. the passcode can NOT shorter the three (3) characters
# e. the user should be able to enter their password and if it meets the requirements, should print a message saying that 
# their password was created successfully, and if it was not, should send back a message with one of the following issues. 


# 13. When you run your code and see typeError in your terminal, what does that typically mean and how would you try to solve
# the issue? 
'It typically means that there is a problem with the operation and so there is a error with the type'


# 14. When you run your code and see indentError in your terminal, what does that typically mean and how would you try to solve 
# the issue?
'This means that there is a indent error so you havr to indent to fix the issue'
# 15. Create a while loop that check a user's password. If they enter the password correct, they will get a message saying 
# that the password was entered successfully. If they enter the password incorrectly, it will tell the user to try again. 
# The user should only have three (3) attempts to get the password correct. If they enter the password incorrect on the fourth 
# attempt, a message should appear telling them that have been locked out and need to talk to the administrator. 

# 16. Which item is at index 5
giftShopping=['xbox','sneakers','necklace','clothing','laptop','gift card']
"gift card"
# 17. Create a for loop that will print ONLY the even numbers within the range of the variable provided below.
# HINT: You will need to use the range() function. 
uptonumber = range(0,30,2)
for n in uptonumber:
  print(n)

# 18. Create a function that uses a conditional statement that checks if a person qualifies for a raise on their salary. 
# The user should be able to enter their name, their salary (how much money they make in an entire year), and how long they have
# worked at the company. If the user has been working at the company longer than four (4) years, they will get a 15% raise. 
# Your program should be able to calculate what their salary is with the 15% increase. If the user qualifies, your program
# should return the a message congratulating the user by name, and telling them what their new salary is with the 15%
# increase (this must be the actual number). If they do not qualify inform the user that unfortunately they do not qualify. 

# 19. Create a function that checks which value is greater than the other. Your function should take two (2) integer parameters. 
# and should evaluate which number is larger. Your function should then print the largest number. 

# 20. Create a while loop function that will add gift items to a list. Your function should ask the user to enter an item name. 
# The item name should then be added to a list variable called gift_bag. Your gift bag should have a limit of six (6) items. 
# Once your gift bag hits its limit of six (6) items your program should print a message saying 
# that the gift bag is full and print the list of items in the gift bag.   
 


 
# write a conditional statement for if the sun is out

sun_is_out = False

if sun_is_out == True:
    print("do not turn on street lamps")
else:
    print("turn on street lamps.")

# write a conditional statement for purchasing a phone
money_in_account = 1000.00
price_of_phone = 700.00

if money_in_account > price_of_phone:
    print('congrats, you got the new phone.')
else:
    print("sorry, insufficient funds.")

# write a function that will accept a user's password. the password should be a
# string parameter. IF the password matches, let the user in. If the password
# does not match, return "incorrect password". 

# IF password matches- let them in
# ELSE it does not match- do not let them in
# keywords in question are = string, parameter, and function

def login_password():
    user_password = input('please enter a password')
    if user_password == 'zionWashington':
        print('welcome, you are logged in.')
    else:
        print('sorry, incorrect password.')

#login_password() 

def data_types():
   user_types=4
    
    print('that is a integer')
   if user_types=float
print('that is a float')
else 
user_types=str
print('that is a string')
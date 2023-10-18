
def passcode_attempt_logic():
    passcode = 1234
    passcodeAttempt_Count =0

    while passcodeAttempt_Count < 4:
        passcodeAttempt = int(input('please put a passcode:'))
        if passcodeAttempt != passcode:
            print('incorrect passcode. Try again')
        else:
            print('correct! you may enter') 
            break
    passcodeAttempt_Count +=1
    
passcode_attempt_logic()
    

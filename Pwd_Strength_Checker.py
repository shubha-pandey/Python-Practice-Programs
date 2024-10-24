''' Check how strong a password is. '''

def PasswordStrength(password) :

    n = len(password)
    hasLower = False
    hasUpper = False
    hasDigit = False
    specialChar = False 

    normalChars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    for i in range(n) :
        if password[i].islower() :
            hasLower = True
        if password[i].isupper() :
            hasUpper = True
        if password[i].isdigit() :
            hasDigit = True
        if password[1] not in normalChars :
            specialChar = True

    print("Strength of the password : ", end = " ")

    if (hasLower and hasUpper and hasDigit and specialChar and n>=8) :
        print("Strong !")
    elif((hasLower or hasUpper) and specialChar and n>=6) :
        print("Moderate !")
    else :
        print("Weak !")
        

if __name__ == "__main__" :
    pwd = input("Enter password : ")
  #  print(pwd, end = " ")
    PasswordStrength(pwd)

        

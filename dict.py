

def ping(n) :
    if (n%2 == 0) :
        return True
    return False

def printing(num) :
    val = ping(num)
    if (val == True) :
        print("Number is even")
    else :
        print("Number is odd")

number = int(input("enter : "))
printing(number)        
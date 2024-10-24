''' Convert Number into Words '''


def convert() :

  num = int(input("Enter the number : "))

  rev = 0

# reversing the no

  while num > 0 :
    rev = rev*10 + num%10
    num = num//10

  num = rev 

# no is reversed so the first letter which is now the last will be taken out first and then converted

  while num > 0 :
    r = num%10

    if r == 0 :
        print("Zero", end=" ")

    elif r == 1 :
        print("One", end=" ")

    elif r == 2 :
        print("Two", end=" ")
    
    elif r == 3 :
        print("Three", end=" ")

    elif r == 4 :
        print("Four", end=" ")    

    elif r == 5 :
        print("Five", end=" ")

    elif r == 6 :
        print("Six", end=" ")

    elif r == 7 :
        print("Seven", end=" ")

    elif r == 8 :
        print("Eight", end=" ")

    elif r == 9 :
        print("Nine", end=" ")

    else :
        print("Invalid Entry")

    num = num//10


if __name__ == "__main__"  :
    convert()
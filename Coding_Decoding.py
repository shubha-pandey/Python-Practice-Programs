'''
Coding:

if the word contains atleast 3 characters, remove the first letter and append it at the end

   now append three random characters at the starting and the end
else:
   simply reverse the string

Decoding:

if the word contains less than 3 characters, reverse it
else:
  remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

Your program should ask whether you want to code or decode
'''


# the commented code bits are what i did at first

import random
import string

def randm() :
    '''
    random_char = ["a", "b" , "c" , "d", "e" , "f" , "g", "h" , "i" , "j" , "k" , "l" , "m" , "n" , "n" , "o" , "p" , "q" , "r" , "s" , "t" , "u" , "v" , "w" , "x" , "y" , "z"]
    r = random.choice(random_char)
    return r
    '''
    return random.choice(string.ascii_lowercase)


def coding() :

    word = input("\nEnter the word you want to be coded : ")
                                                                 
    l = list(word)                                               # can also use this in the if else

    if len(l)>=3 :
        '''
        l.append(l[0])
        del(l[0])
        '''
        l.append(l.pop(0))                                        # Rotate first character to the end
        
        ''''
        l.insert(0, randm())
        l.insert(1, randm())
        l.insert(2, randm())
        '''
        l = [randm(), randm(), randm()] + l                        # Insert three random characters at the beginning

        '''
        l.append(randm())                                          # using append here instead of insert coz the previous insert operation remains same that is the first letter remains at the last(-1) and the rest of the elements are getting inserted before it at -2, -3 and -4 positions
        l.append(randm())
        l.append(randm())
        '''
        l.extend([randm(), randm(), randm()])                       # Append three random characters at the end

    else :
        '''
        temp = l[0]
        l[0] = l[1]
        l[1] = temp
        '''
        l[0], l[1] = l[1], l[0]                                       # Swap first and second character
    
    ''''
    return ''.join(map(str, l))                                       # don't need to use map(str, l) as l is already a list of characters.
    '''
    return ''.join(l)


def decoding() :

    word = input("\nEnter the word you want to be decoded : ")

    l = list(word)

    if len(word)>=3 :
        '''
        for i in range(3) :
            del(l[0], l[-1])
        l.insert(0,l[-1])
        del(l[-1])
        '''
        l = l[3:-3]                                                    # Remove the first three and last three random characters

        l.insert(0, l.pop())                                            # Rotate last character to the beginning

    else :
        '''
        temp = l[0]
        l[0] = l[1]
        l[1] = temp
        '''
        l[0], l[1] = l[1], l[0]                                           # Swap first and second character

    '''
    return ''.joim(map(str, l))                                           # don't need to use map(str, l) as l is already a list of characters.
    '''
    return ''.join(l)
    

def choices() :

    choice = input("\nSelect your choice : 1. Code\n                     2. Decode\n")
    if choice == "1" :
        print(coding())
    elif choice == "2" :
        print(decoding())
    else : 
        print("\nInvalid Input !")


if __name__ == "__main__" :
    
    choices()

    while True : 
        again = input("\nAgain ? (Yes/No)  ").lower().capitalize()
        if again == "Yes" :
            choices()
        else :
            print("\nBye-Bye")
            break
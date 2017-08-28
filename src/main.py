#!C:/Program Files/Python36/python.exe

'''
Created on Aug 28, 2017

@author: jlearx
'''

if __name__ == '__main__':
    number = int(input("Please enter a number: "))
    
    if (number % 4 == 0):
        print("The number is divisible by four.")
    elif(number % 2 == 0):
        print("The number is even.")
    else:
        print("The number is odd.")
        
    numStr = input("Please enter a number to check: ")
    num = int(numStr)
    checkStr = input("Please enter the number to divide by: ")
    check = int(checkStr)
    
    if (num % check == 0):
        print(checkStr + " evenly goes into " + numStr + ".")
    else:
        print(checkStr + " does not evenly go into " + numStr + ".")
        
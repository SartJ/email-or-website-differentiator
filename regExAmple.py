# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 07:37:42 2021

@author: sartaj
"""


# Taking a number as an input which is the number of lines that will be read to check:
n = int(input("Number of lines:")) 

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
             'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']

otherSymbols = ['-','.','_','!','#','$','%','&','*',
                '+','-','/','=','?','^','_','`','{','|'] 

otherSymbols2 = ['-','.']

# Checks if it is a valid email address or not:
def email_orNot(x):
    returnee = 1
    fragments = x.split('@')
    #print(fragments)
    
    # Checking if the syntax before at sign is valid or not:
    beforeAt = list(fragments[0])
    #print(beforeAt)

    if beforeAt[0] in alphabets:
        returnee = 1
        #print("Alright.")
    if beforeAt[0] in numbers:
        returnee = 2
        #print("Can't start with a number.")
    if beforeAt[0] in otherSymbols or beforeAt[len(beforeAt)-1] in otherSymbols:
        returnee = 2
        #print("Can't have a symbol like that at start or before at sign.")
    
    # Checking if the syntax after at sign is valid or not:
    afterAt = list(fragments[1])
    #print(afterAt)
    
    if afterAt[0] in alphabets:
        returnee = 1
        #print('Alright 2')
    if afterAt[0] in otherSymbols:
        returnee = 2
        #print('NOPE')
    if '.' not in afterAt:
        returnee = 2
        #print('Does not look like an email')
    if afterAt[len(afterAt)-1] in otherSymbols:
        returnee = 2
        #print("NOPEEEE")
    
        
    
    
    return returnee

# Checks if it is a valid web address or not:
def web_orNot(x):
    returnee = 0
    wholeLineCharList = list(x)
    fragments = x.split('.')
    print(fragments)
    
    if (fragments[0] == 'www') and int(len(fragments))>=3:
        returnee = 0
        print("Works")
    
    afterWWW = list(fragments[1])
    
    if afterWWW[0] in alphabets or afterWWW[0] in numbers:
        returnee = 0
        
    if afterWWW[0] in otherSymbols:
        returnee = 2
        
    if wholeLineCharList[len(wholeLineCharList)-1] in numbers or wholeLineCharList[len(wholeLineCharList)-1] in otherSymbols:
        returnee = 2
    
    
    
    
    
    return returnee


# This method checks whether it's an email address or a website address:
def differ(x):
    if '@' in x:
        chk = email_orNot(x)
    elif 'www' in x:
        chk = web_orNot(x)
    else:
        return 2  #given input is neither mail or web address.
    return chk
    


# Taking the lines as input and processing them and giving outputs:
for i in range(n):
    lineNumber = 1
    x = input("Please enter a line:")
    typeCheck = differ(x)
    
    if typeCheck == 1:
        print("Email,", lineNumber)
    elif typeCheck == 0:
        print("Web,", lineNumber)
    else:
        print("The given input is neither,", lineNumber)
        
    lineNumber += 1






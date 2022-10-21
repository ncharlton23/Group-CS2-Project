'''
author = Dylan_Joseph 
10/19/22
this codes objective is to shift to the right 
'''



'''
this function shifts the number to the right 
command: the command that the user gives you(string)
rshift : the right shift command is when they give you a (string)
letter : the last x letters in string iinput(string)
number : the number the user gave you(integer)
text : the string input(string)
product : the varible for yhe return statement (string)
'''
def rightShift(command,text):
    rightshift = command.split("-")
    number = rightshift[1]
    number=int(number)
    letters = text[number:]
    product = letters+"#"*number
    return(product)
def main():
    ans = "LS-3/RS-1/LC-3/RC-5/COMPUTER"
    ans = ans.split("/")        #split the answer by /
    text = ans[-1]
    userinput = input("LS or RS or LC or RC")
    if userinput == "LS":
        command = ans[0]
        print(leftShift(command,text))
    elif userinput == "RS":
        command = ans[1]
        print(rightShift(command,text))
    elif userinput == "LC":
        command = ans[2]
        print(leftCirculate(command,text))
    elif userinput == "RC":
        command = ans[3]
        print(rightCirculate(command,text))

def leftShift(command,text):
    '''
    Arguments
        command: the command that the user gives you (string)
        lshift: the left shift command that they give you (string)
        letters: the last X letters in the string input (string)
        number: the number the user gave you (integer)
        text: the string input the user put in (string)
        product: the variable for the return statement (string)
    Takes:
        command variable from main
        text variable from main
    Returns:
        sends product back to main
    '''
    lshift = command.split("-")
    number = int(lshift[1])
    letters = text[number:]
    product = letters + "#"*number
    return(product)

def leftCirculate(command,text):
    lshift = command.split("-")
    number = int(lshift[1])
    firstletters = text[number:]
    lastletters = text[:number]
    product = firstletters + lastletters
    return(product)
def rightCirculate(command,text):
    rshift = command.split("-")
    number = int(rshift[1])
    move = len(text) - number
    lastletters = text[:move]
    firstletters = text[move:]
    product =  firstletters + lastletters
    return product

def rightShift(command,text):
    '''
    Arguments
        command: the command that the user gives you (string)
        rshift: the left shift command that they give you (string)
        letters: the last X letters in the string input (string)
        number: the number the user gave you (integer)
        text: the string input the user put in (string)
        product: the variable for the return statement (string)
    Takes:
        command variable from main
        text variable from main
    Returns:
        sends product back to main
    '''
    rshift = command.split("-")
    number = int(rshift[1])
    move = len(text) - number
    letters = text[:move]
    product = "#"*(number) + letters
    return product

main()
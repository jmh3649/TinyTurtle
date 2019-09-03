import turtle

"""
CSAPX Lab 1: Tiny Turtle

A program that takes an enhanced TT program, expands it into basic TT commands,
and then does turtle drawing from it.

author: Jake Hunter
"""



"""
evaluate takes in a string composed of basic turtle functions and advanced turtle functions. It then translates the
advanced instructions into basic instructions by calling the expand_iterate and expand_polygon methods. Finally, it
prints the full string of basic instructions then executes them, printing out each instruction that it executes.

Argument: A string composed of basic and/or advanced turtle functions
Return: A string of basic turtle instructions to execute
Visual Output: A turtle drawing of the interpreted instructions that were passed into the method

"""
def evaluate(string1):
    while string1.find('I') >= 0:
        beginIndex = string1.find('I')
        endIndex = string1.find('@')
        string1 = string1[:beginIndex] + expand_iterate(string1[beginIndex:endIndex+1]) + string1[endIndex+1:]

    while string1.find('P') >= 0:
        beginIndex = string1.find('P')
        endIndex = beginIndex + 6
        string1 = string1[:beginIndex] + expand_polygon(string1[beginIndex:endIndex + 1]) + string1[endIndex + 1:]



    print('Expanded program: ' + string1)
    print('Evaluating...')

    
    parsed = string1.split()


    for i in range(len(parsed)):
            nums = parsed[i][1:]
            if parsed[i][0:1] == "U":
                turtle.up()
                print('up()')
            elif parsed[i][0:1] == "D":
                turtle.down()
                print('down()')
            elif parsed[i][0:1] == "F":
                turtle.forward(int (nums))
                print('forward(' + nums + ')')
            elif parsed[i][0:1] == "L":
                turtle.left(int (nums))
                print('left(' + nums + ')')
            elif parsed[i][0:1] == "C":
                turtle.circle(int (nums))
                print('circle(' + nums + ')')
            elif parsed[i][0:1] == "B":
                turtle.backward(int (nums))
                print('backward(' + nums + ')')
            elif parsed[i][0:1] == "R":
                turtle.right(int (nums))
                print('right(' + nums + ')')

"""
expand_iterate takes in a string and translates it into basic turtle instructions.

Argument: A string that follows the pattern I# . . . @
Return: A string composed of basic turtle functions

"""
def expand_iterate(string1):
    parsed = string1.split()
    output = ''
    numTimes = parsed[0][1:2]
    instructions = parsed[1:len(parsed)-1]
    i = int(numTimes)
    while i > 0:
        for j in range(len(instructions)):
            output += instructions[j]
            output += ' '
        i -= 1

    return output.strip()

"""
expand_polygon takes in a string and translates it into basic turtle instructions.

Argument: A string that follows the pattern P# ###
Return: A string composed of basic turtle functions

"""
def expand_polygon(string1):
    parsed = string1.split()
    output = ''
    numSides = int(parsed[0][1:2])
    distance = parsed[1]
    interiorAngle = str(int(360 / numSides))

    while len(interiorAngle) < 3:
        interiorAngle = '0' + interiorAngle

    i = numSides
    while i > 0:
        output += 'F' + distance + ' ' + 'L' + interiorAngle + ' '
        i -= 1

    return output



def main() -> None:

    rawInput = input("Enter a string of TT commands: \n")
    evaluate(rawInput)
    turtle.done()

if __name__ == '__main__':
    main()



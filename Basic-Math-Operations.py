#Write the function "arnntetik", taking 3 arguments:
#the first 2 - the number, the third - the operation that should be performed on them.
#If the third argument is +, add them; If -, then subtract; Multiply; / - divide (the first into the second). In other cases, return the string "Unknown operation" ..

print ("Hi. This function (arithmetic(1,2,'+')) use for math operation whith 2 numbers. Use +,-,*,/")
def arithmetic (a, b, c):
    if c == '+':
        return a + b
    elif c == '-':
        return a - b
    elif c == '*':
        return a * b
    elif c == '/':
        return a / b
    else:
        print ('Unknown operation. Use +,-,*,/')

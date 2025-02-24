digits = [1,2,3]

digits = [4,3,2,1]

digits = [9]

def plus_one(digit):
    a = ""
    for i in digit:

        a=a+str(i)
    a = int(a)+1
    print([i for i in str(a)])

plus_one(digits)

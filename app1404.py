#4. The nested if stetement
def testNestedIf():
    num = float(input("Enter number:"))
    if(num >= 0):
        if(num == 0):
            print(num,"is Zero numbr")
        else:
            print(num,"is Positive number")
    else:
        print(num,"is Negative number")            
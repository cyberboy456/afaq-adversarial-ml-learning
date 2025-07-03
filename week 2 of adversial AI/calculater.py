a=int(input("enter a fisrt number"))
b=int(input("enter a second number"))
operation=input("enter operation +,-,*,/")
def calculate(a,b,operation):
    if operation=="+":
        return a+b
    elif operation=="-":
        return a-b
    elif operation=="*":
        return a*b
    elif operation=="/":
        return a/b
result =calculate(a,b,operation)
print(result)
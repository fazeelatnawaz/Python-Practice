def values(a,b):
    if a%b==0:
        print(a,"is even number")
    else:
        print(b,"is odd number")


a = int(input("Enter your first value:"))
b = int(input("Enter your second value:"))
values(a, b)
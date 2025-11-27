def add(a,b):
    return(a+b)
def sub(a,b):
    return(a-b)
def mul(a,b):
    return(a*b)
def div(a,b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print("cannot divide by zero")   
def menu():
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")
    print("-----------------")
    choose=int(input("Enter your choice: "))
    return choose
while True:
    try:
        number1=int(input("Enter the first number:"))
        number2=int(input("Enter the second number:"))
    except ValueError:
        print("enter digits only")     
    choice=menu()
    if choice==1:
        print(add(number1,number2))
    elif choice==2:
        print(sub(number1,number2))
    elif choice==3:
        print(mul(number1,number2))
    elif choice==4:
        div(number1,number2)
    elif choice==5:
        print("Exit from the calculation")
        break   
    else:
        print("Invalid choice enter between 1 to 4")     
choice()                       

                

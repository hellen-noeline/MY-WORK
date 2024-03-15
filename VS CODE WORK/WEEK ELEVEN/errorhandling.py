#syntax error
print("Hellen")
      
number=10000

if(number<20):
    print("Less than 20")


#Runtime Error
    try:
        x=int(input("Enter first number:"))
        y=int(input("Enter second number:"))
        divide=x/y
        print(divide)
    except:
        print("Erroroccured")
print("Hellen")



iterator= True

x=0
y=0

while iterator:
    try:
        if x<=0:
            x=int(input("Enter first number:"))
        if y<=0:    
            y=int(input("Enter second number:"))
        divide=x/y
        print(divide)
    except ZeroDivisionError:
        print("Please dont divide by zero")  
        iterator=False  
    
try:
    x=int(input("Enter first number:"))
    y=int(input("Enter second number:"))
    divide=x/y
    print(divide)
except ValueError:
    print("Please only enter numeric values")

#ASSIGNMENT
#LET YOUR BROTHER ENTER TWO RANDOM NUMBERS THE FIRST NUMBER
#  SECOND NUMBER MARK YOUR BROTHER TELL HIM ITS WRONG
#  ITS CORRECT MAKE SURE THE PROGRAM IS SMART WITH ADDITION MULTIPLICATION AND DIVISION
#  THERE IS A BONUS FOR SOMEONE WHO LETS THE BROTHER DO IT FIVE TIMES
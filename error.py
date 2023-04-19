try:
    num1=int(input("enter the first number :"))
    num2=int(input("enter the second number :"))
    result=num1/num2

except ZeroDivisionError:
    print("zero can't be devide")

else:
    print(f"the result is {result}")

finally:
    print("all fine")




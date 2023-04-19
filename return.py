def greet(name, greeting="hello"):
    message = greeting + "," + name
    return message


greeting1 = greet("dilux")
greeting2 = greet("John", greeting="Hi")
greeting3 = greet(greeting="hi", name="dilux")

print(greeting1)
print(greeting2)
print(greeting3)


def add_sub(x, y):
    add = x + y
    sub = x - y
    return add, sub


result = add_sub(10, 5)
print(result)


def circle(pi, r):
    perimeter = 2 * pi * r
    area = pi * r ** 2
    return perimeter, area


result = circle(3.14, 7)
print(result)


# resusrsion
def fact(num):
    if num == 1:
        return 1
    else:
        return num * fact(num - 1)


result = fact(5)
print(result)


def sum(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n + sum(n - 1)


result = sum(5)
print(result)


# fibanicco
def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


result = fib(5)
print(result)

#greatest common divisor (GCD)


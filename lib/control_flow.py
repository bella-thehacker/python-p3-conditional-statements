#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    if username == "admin" and password == "12345":
        return "Access granted"
    else:
        return "Access denied"
    
admin_login("admin","12345")
admin_login("sudo", "4567")

def hows_the_weather(temperature):
    # your code here
    if temperature < 40:
        return("It's brisk out there!")
    elif temperature < 65:
        return("It's a little chilly out there!")
    elif temperature > 85:
        return("It's too dang hot out there!")
    else:
        return("It's perfect out there!")

hows_the_weather(35)
hows_the_weather(55)
hows_the_weather(75)
hows_the_weather(90)

def fizzbuzz(num):
    # your code here
    if num % 3 == 0  and  num % 5 == 0:
        return("FizzBuzz")
    elif num % 5 == 0:
        return("Buzz")
    elif num %  3 == 0:
        return("Fizz")
    else:
        return num

fizzbuzz(10)
fizzbuzz(15)
fizzbuzz(22)
fizzbuzz(52)
fizzbuzz(13)
fizzbuzz(59)

def calculator(operation, num1, num2):
    # your code here
    if operation == "+" :
        print(num1 + num2)
        return num1 + num2
    elif operation == "-":
        print(num1 - num2)
        return num1 - num2
    elif operation == "*":
        print(num1 * num2)
        return num1 * num2
    elif operation == "/":
        print(num1 / num2)
        return num1 / num2
    else:
        print("Invalid operation!")
        
calculator("+", 4, 4)
calculator("-", 9, 6)
calculator("*", 6, 6)
calculator("/", 15, 3)
calculator("pip", 4, 10)

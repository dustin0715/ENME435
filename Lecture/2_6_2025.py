import numpy
import matplotlib
import imutils
import cv2

print("    *")
print("   * *")
print("  *****")
print(" *     *")
print("*       *")

a = 14*12
b = 33*144-187
c = a/b
print(c)

num1 = input("Enter a number:")
num2 = input("Enter another number:")
num1 = float(num1)
num2 = float(num2)
num3 = num1 + num2
print("Total:",num3)

name = input('Enter your name: ')
print("Your name is "+name,name,name)

x = float(input("Enter a number:"))
if x < 10:
    print("You entered a number less than 10")
else:
    print("You entered something else")
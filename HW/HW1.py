import random

#Problem 3
#Declared two list for the dices and a variable called count
dice1 = []
dice2 = []
count = 0
#Generate random numbers between 1 and 6 10000 times 
for i in range(10000):
      dice1.append(random.randint(1, 6))
      dice2.append(random.randint(1, 6))
      if dice1[i] == dice2[i]:
            count += 1
print("Percentage of rolls that are doubles:",count/10000*100)

#Problem 4
#Ask the user to input a number for w,x,y,z
w = float(input("Enter a number for w:"))
x = float(input("Enter a number for x:"))
y = float(input("Enter a number for y:"))
z = float(input("Enter a number for z:"))
#Compare the w to x and y to z, then swap the smallest number of the two
if w < x and y < z:
    hold = w
    w = y
    y = hold
elif w < x and y > z:
    hold = w
    w = z
    z = hold
elif w > x and y > z:
    hold = x
    x = z
    z = hold
else:
    hold = x
    x = y
    y = hold
print("w:",w, "x:",x, "y:",y, "z:",z)

#Problem 5
#Decalare one empty list and two value list
num = []
ans = [0,0]
#Ask the user to enter 10 numbers
print("Enter 10 numbers:")
for i in range(10):
    num.append(float(input()))
#Sort the list then store the 2 smallest into the two value list
num.sort()
ans[0] = num[0]
for i in range(10):
    if ans[0]<num[i]:
        ans[1]=num[i]
        break
print("Two smallest numbers:",ans)

#Problem 6
#Enter a number of letter A
n = int(input("Enter a number:"))
for i in range(n):
    print("A", end = " ")
print()

#Problem 7
#Print a series of 10 random 0 and 1 all on the same line
#Repeat this for or a total of 50 lines
#each with one more random value (1 or 0) than the previous lin 
for i in range(50):
    for i in range(10+i):
        print(random.randint(0, 1), end="")
    print()

#Problem 8
#Declare 2 variables and 1 list
q = 0
t = []
c = 0
#Stop asking the user to enter a number when 5 is entered
#Keep count of how many numbers were enterd
while q != 5:
    q = int(input("Enter a number between 1 and 10:"))
    t.append(q)
    c += 1
print("The total numbers that was entered:", c)
#If the user entered any numbers less than 3, print yes
a = False
for i in range(len(t)):
    if t[i] < 3:
        a = True
if a == 1:
    print("User entered any numbers less than 3: yes")
else:
    print("User entered any numbers less than 3: no")
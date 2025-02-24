import numpy as np
import matplotlib.pyplot as plt
import imutils
import cv2

# num=int(input("Enter a number:"))
# if num%7==0:
#     print("It is divisible by 7")
# else:
#     print("It is not divisible by 7")

# number = 0
# while number < 10:
#     number+=1
# print("Thanks for playing!")

# for i in range(5,10):
#     print(i)

# terps = np.array([47,72,50,2,99])
# print(terps)
# print(terps[:3])
# print(np.shape(terps))
# print(np.size(terps))
# print(len(terps))

# a = np.arange(5, 20, 0.5)
# print(a)

# b = np.linspace(1, 10, 20)
# print(b)

x = np.linspace(-10, 10, 100)
y = np.sin(x)
print(x,y)
plt.plot(x,y,'-')
plt.show()
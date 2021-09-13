#Write a program that takes three numbers and prints their sum.Every number is given on a separate line.
a = int(input())
b = int(input())
c = int(input())
print(a + b + c)

#Write a program that greets the person by printing the word "Hi" and the name of the person. See the examples below.
a = input()
print("Hi" ,a)

#Write a program that takes a number and print its square.
a=int(input())
print(a*a)

#Write a program that reads the length of the base and the height of a right-angled triangle and prints the area. Every number is given on a separate line.
b = int(input())
h= int(input())
c=b*h
d=c/2
print(d)

#Write a program that greets the user by printing the word "Hello", a comma, the name of the user and an exclamation mark after it. See the examples below.
#Warning. Your program's output should strictly match the desired one, character by character. There shouldn't be any space between the name and the exclamation mark. You can use + operator to concatenate two strings. See the lesson for details.
name = input()
a=name+"!"
print("Hello,",a)


#N students take K apples and distribute them among each other evenly. The remaining (the undivisible) part remains in the basket. How many apples will each single student get? How many apples will remain in the basket?
#The program reads the numbers N and K. It should print the two answers for the questions above.
n = int(input())
b=int(input())
print(b // n)
print(b % n)

#Write a program that reads an integer number and prints its previous and next numbers. See the examples below for the exact format your answers should take. There shouldn't be a space before the period.
#Remember that you can convert the numbers to strings using the function str.
a=int(input())
k=a+1
p=a-1
print("The next number for the number",a,' is ',k)
print("The previous number for the number",a," is ",p)



#A timestamp is three numbers: a number of hours, minutes and seconds. Given two timestamps, calculate how many seconds is between them. The moment of the first timestamp occurred before the moment of the second timestamp.
a = int(input())*3600
b = int(input())*60
c = int(input())
d = int(input())*3600
e = int(input())*60
f = int(input())
k=a+b+c
p=d+e+f
if k>=p:
    print(k-p)
else:
    print(p-k)
    

#A school decided to replace the desks in three classrooms. Each desk sits two students. Given the number of students in each class, print the smallest possible number of desks that can be purchased.
#The program should read three integers: the number of students in each of the three classes, a, b and c respectively.
#In the first test there are three groups. The first group has 20 students and thus needs 10 desks. The second group has 21 students, so they can get by with no fewer than 11 desks. 11 desks is also enough for the third group of 22 students. So we need 32 desks in total.

import math
a= float(input())
b= float(input())
c= float(input())
print(math.ceil(a/2)+math.ceil(b/2)+math.ceil(c/2))

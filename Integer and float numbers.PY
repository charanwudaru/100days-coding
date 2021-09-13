#Given an integer number, print its last digit.
a = int(input())
print(a%10)


#In all the problems input the data using input() and print the result using print().
a = int(input())
print(a//10%10)


#Given a three-digit number. Find the sum of its digits.
number = int(input())
a = number // 100
b = number // 10 % 10
c = number % 10
print(a + b + c)


#Given a positive real number, print its fractional part.
a = float(input())
c= int(a)
b= a-c
print(b)


#In all the problems input the data using input() and print the result using print().
b = float(input())
c=b*10
a=c%10
print(int(a))


#A car can cover distance of N kilometers per day. How many days will it take to cover a route of length M kilometers? The program gets two numbers: N and M.
import math
a = int(input())
b = int(input())
print(math.ceil(b/a))


#Given the integer N - the number of minutes that is passed since midnight - how many hours and minutes are displayed on the 24h digital clock?
#The program should print two numbers: the number of hours (between 0 and 23) and the number of minutes (between 0 and 59).
#For example, if N = 150, then 150 minutes have passed since midnight - i.e. now is 2:30 am. So the program should print 2 30.
a = int(input())
c=a//60
b=a%60
print(c,b)


##A cupcake costs A dollars and B cents. Determine, how many dollars and cents should one pay for N cupcakes. A program gets three numbers: A, B, N. It should print two numbers: total cost in dollars and cents.
a = int(input())
b=int(input())
c=int(input())
cost=c*(100*a+b)
print(cost//100,cost%100)

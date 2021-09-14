#Given two integers, print the smaller value
a = int(input())
b = int(input())
if a<b:
    print(a)
else:
    print(b)
    

#For the given integer X print 1 if it's positive, -1 if it's negative, or 0 if it's equal to zero.
#Try to use the cascade if-elif-else for it.
a = int(input())
if a>0:
    print(1)
elif a<0:
    print(-1)
elif a==0:
    print(0)

    
#Given three integers, print the smallest value.
a = int(input())
b = int(input())
c = int(input())
if (a<b) and (a<c):
    print(a)
elif (b<a) and (b<c):
    print(b)
else:
    print(c)



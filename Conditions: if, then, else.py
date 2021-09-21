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


#Given three integers, determine how many of them are equal to each other. The program must print one of these numbers: 3 (if all are the same), 2 (if two of them are equal to each other and the third is different) or 0 (if all numbers are different).
a=int(input())
b=int(input())
c=int(input())
if a==b==c :
    print(3)
elif b==a or b==c :
    print(2)
elif (a==b) or (a==c):
    print(2)
else:
    print(0)
              #(or)
a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print(3)
elif a == b or b == c or a == c:
    print(2)
else:
    print(0)

    
   #Chess rook moves horizontally or vertically. Given two different cells of the chessboard, determine whether a rook can go from the first cell to the second in one move.
#The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and then the last two - for the second cell. The program should output YES if a rook can go from the first cell to the second in one move, or NO otherwise.
a=int(input())
b=int(input())
c=int(input())
d=int(input())
if (a==c) or (b==d):
    print('YES')
else:
    print("NO")
    
   

#Given two cells of a chessboard. If they are painted in one color, print the word YES, and if in a different color - NO.
#The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and then the last two - for the second cell.
a=int(input())
b=int(input())
c=int(input())
d=int(input())
if (a+b+c+d)%2 == 0:
    print("YES")
else:
    print('NO')
    

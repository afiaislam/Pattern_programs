"""
Pattern 18:    
              *
            * * *
          * * * * *
            * * * 
              *
"""

n=int(input("Enter Odd Row no.: "))

mid=int(n/2+1)
stop=n-1
start=1
for i in range(1,n+1):
    for j in range(1,stop):
        print(" ",end=" ")
    for k in range(1,start+1):
        print("*",end=" ")
    
    if i<mid:
        stop-=1
        start+=2
    else:
        stop+=1
        start-=2
    print()

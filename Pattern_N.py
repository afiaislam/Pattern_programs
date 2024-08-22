"""
Pattern 14:    
              1 
            1 2 1
          1 2 3 2 1 
        1 2 3 4 3 2 1
      1 2 3 4 5 4 3 2 1
"""

n=int(input("Enter the Row no.: "))

for i in range(n+1):
    a=1
    
    for j in range(n-i):
        print(" ",end=" ")

    for k in range(i):
        print(a,end=" ")
        a+=1

    for l in range(1,i):
        print(i-1,end=" ")
        i-=1

    print()
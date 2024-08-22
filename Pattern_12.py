"""
Pattern 12:    
              1 
            1 2 3
          1 2 3 4 5 
        1 2 3 4 5 6 7 
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
        print(a,end=" ")
        a+=1
        
    print()
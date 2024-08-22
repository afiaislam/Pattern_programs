"""
Pattern 17:    
            1 2 3 4 5 
            A B C D
            1 2 3
            A B
            1
"""

n=int(input("Enter the Row no.: "))

for i in range(1,n+1):
    a=1
    for j in range(1,n-i+1):
        
        if i%2==0:
            c=chr(j+64)
            print(c,end=" ")
            a+=1

        else:
            print(j,end=" ")
            
    print()

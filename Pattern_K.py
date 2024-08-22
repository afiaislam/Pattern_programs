"""
Pattern 11:    
               * 
             * * *
           * * * * * 
         * * * * * * *
"""
n=int(input("Enter the Row no.: "))

for i in range(n+1):

    for j in range(n-i):
        print(" ",end=" ")

    for k in range(i):
        print("*",end=" ")

    for l in range(1,i):
        print("*",end=" ")
        
    print()

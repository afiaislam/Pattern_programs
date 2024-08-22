"""
Pattern 13:    
              A 
            A B C
          A B C D E 
        A B C D E F G
      A B C D E F G H I 
"""
n=int(input("Enter the Row no.: "))

for i in range(n+1):
    a=1
    for j in range(n-i):
        print(" ",end=" ")

    for k in range(i):
        c=chr(a+64)
        print(c,end=" ")
        a+=1

    for l in range(1,i):
        c=chr(a+64)
        print(c,end=" ")
        a+=1
        
    print()
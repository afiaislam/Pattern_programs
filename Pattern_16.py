"""
Pattern 16:    
              A 
            A B A
          A B C B A
        A B C D C B A
      A B C D E D C B A 
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
        c=chr(a+62)
        print(c,end=" ")
        a-=1       

    print()
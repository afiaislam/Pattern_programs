"""
Pattern 10:   A
            A B
          A B C
        A B C D
      A B C D E
"""
n=int(input("Enter the size of Row:") )

for i in range(n+1):
    a=1
    for j in range(n-i):
        print(" ",end=" ")

    for k in range(i):
        c=chr(a+64)
        a+=1
        print(c,end=" ")
        
    print()
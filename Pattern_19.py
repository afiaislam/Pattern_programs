"""
Pattern 19:    
              * * * * * * * 
              * * *   * * *
              * *       * *
              *           *
"""

n=int(input("Enter Odd Row no.: "))
st=n-1
sp=1
for i in range(1,n*2):
    print("*",end=" ")
print()

for i in range(1,n+1):
    for j in range(1,st+1):
        print("*",end=" ")
    for k in range(1,sp+1):
        print(" ",end=" ")
    for l in range(1,st+1):
        print("*",end=" ")
    st-=1
    sp+=2

    print()
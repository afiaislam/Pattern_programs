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
sp=n-1
st=1
for i in range(1,n+1):
    for j in range(1,sp):
        print(" ",end=" ")
    for k in range(1,st+1):
        print("*",end=" ")
    
    if i<mid:
        sp-=1
        st+=2
    else:
        sp+=1
        st-=2
    print()

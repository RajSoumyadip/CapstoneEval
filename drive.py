from mul import mul
from sub import sub
from add import add
print("enter add mul sub 0 1 2")
n = int(input())
print("enter number")
n1 = 8
n2 = 10
if n==0:
    print(add(n1,n2))
elif n==1:
    print(mul(n1, n2))
elif n==2:
    print(sub(n1,n2))
else:
    pass

#Implemented Driver function defination
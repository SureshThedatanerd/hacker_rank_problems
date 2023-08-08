from itertools import product
A=list(map(int,input().split()))
B=list(map(int,input().split()))
lst=list(product(A,B))
for i in range(0,len(lst)):
    print(lst[i],end=" ")
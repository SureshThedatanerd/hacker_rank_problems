from itertools import permutations
S,k = input().split()
r=int(k)
lst=list(permutations(S,r))
lst.sort()
print(lst)
for i in range(len(lst)):
    lst1=list(lst[i])
    str=' '
    for j in range(len(lst1)):
        str=str+lst1[j]
    print(str)
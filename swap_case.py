'''You are given a string and your task is to swap cases. In other words, 
convert all lowercase letters to uppercase letters and vice versa'''
n=input("enter a string : ")
l1=list(n)
l2=[]
for i in range(0,len(l1)):
    if l1[i]>='a' and l1[i]<='z':
        l2.append(l1[i].upper())
    else:
        l2.append(l1[i].lower())
str=' '
for j in range(len(l2)):
    str=str+l2[j]
print(str)
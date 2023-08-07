s=input("enter a string : ")
k=int(input("enter k value : "))
l1=list(s)
if len(s)%k==0:
    i=0
    count=0
    while i!=len(s):
        l2=list(s[i:i+k])
        l3=[]
        for i in range(len(l2)):
            if l2[i] not in l3:
                l3.append(l2[i])
        str=''
        for i in range(len(l3)):
            str=str+l3[i]
        print(str)
        count=count+1
        i=count*k



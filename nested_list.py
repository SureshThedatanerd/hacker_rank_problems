'''Finding the name  of student with  second lowest scores. if two name consists of same score as 2nd 
lowest score, sort their names in alphabetical order and print their names.
If one name consists of 2nd highest score  then print that name
example: 
python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2],
                 ['Akriti', 41], ['Harsh', 39]]


'''

l1=[]
for i in range(int(input())):
            l=[]
            name = input()
            score = float(input())
            l.append(name)
            l.append(score)
            l1.append(l)
l=[]
for k in range(len(l1)):
            l.append(l1[k][1])
l.sort()
m=min(l)
m1=l[1]
for i in range(2,len(l)):
            if l[i]<=m1 and l[i]>m:
                    m1=l[i]
s=[]
for j in range(0,len(l1)):
            if l1[j][1]==m1:
                    s.append(l1[j][0])
s.sort()
for x in range(len(s)):
        print(s[x],end=" ")
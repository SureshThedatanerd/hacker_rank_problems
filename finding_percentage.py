'''The provided code stub will read in a dictionary containing
 key/value pairs of name:[marks] for a list of students.
 Print the average of the marks array for the student name provided
 example:
    arnold 50 30 60
    mia 58 60 40    
    ram 52 20 30 
    suresh 20 30 20
    mia 
 '''

n = int(input())
marks = {}
for i in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    marks[name] = scores
query_name = input("enter a name to be queried : ")
for j in marks:
    if j==query_name:
        lst=marks[j]
        sum=0.0
        for x in range(0,len(lst)):
            sum=sum+lst[x]
        avg=sum/len(lst)
        x=round(avg,2)
        print(x)
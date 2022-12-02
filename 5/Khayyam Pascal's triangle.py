n = int(input())

column = []
for i in range(n):
    row = []
    for j in range(i+1):
        if j==0 :
            row.append(1)        
        elif i!=0:
            if i==j:
                row.append(column[i-1][j-1])
            else:
                row.append(column[i-1][j-1]+column[i-1][j])
        else:
            break
    column.append(row)      

for i in range(len(row)):
    for j in range(n-i+1):
        print(end=" ")
    print(column[i])
#i = int(input('Enter the number of rows'))
#j = int(input('Enter the number of columns'))
i,j = map(int,input().split(',')) # in case of comma separated inputs
matrix = []
for x in range(i):
    a = []
    for y in range(j):
        a.append(x*y)
    matrix.append(a)

print(matrix)
import Pascal as ps

t=ps.PascalTriangle(5)
for i in t:
    [print(j, end=' ') for j in i]
    print('')
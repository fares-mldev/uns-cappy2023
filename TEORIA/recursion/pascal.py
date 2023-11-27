def pascal(i,j):
    if j == 0 or i == j:
        return 1
    else:
        return pascal(i-1, j) + pascal(i-1, j-1)

for row in range(10):
    row_list = []
    index_list = []
    for col in range(row+1):
        row_list.append(pascal(row,col))
        index_list.append((row,col))
    print(row_list)
        
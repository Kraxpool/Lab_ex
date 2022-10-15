col = int(input('col->'))
row = int(input('row->'))

for i in range(col):
    for j in range(row):
        if i == 0 or i == col-1:
            print(f'*', end=" ")
        else:
            if j == 0 or j == row-1:
                print(f'*', end = " ")
            else:
                print(f' ', end = " ")
    print()
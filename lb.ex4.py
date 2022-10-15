import sys
try:
    length = int(input('Введіть довжину - '))
    width = int(input('Введіть ширину - '))
    for i in range(width):
        for j in range(length):
            if i == 0 or j == 0 or i==width-1 or j==length-1:
                sys.stdout.write("*")
            else:
                sys.stdout.write(" ")
        print()
except Exception as ex:
    print(f'Eror information: {ex}')
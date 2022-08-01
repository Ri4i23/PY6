#стандартный вывод 

def print_operation_table(operation, columns=6, rows=9):
    for col in range(1, columns + 1):
        print()
        for row in range(1, rows + 1):
            print(operation(col, row), end='\t')

print_operation_table(lambda x, y: x*y, 5)
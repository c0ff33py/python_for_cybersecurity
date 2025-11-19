def matrix(initial_number, end_of_first_row):
    n1 = initial_number
    n2 = end_of_first_row + 1

    for column in range(n1, n2):
        for row in range(n1, n2):
            print(column * row, end=" ")
        print()

matrix(1,4)

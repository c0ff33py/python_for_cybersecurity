#   Use a while loop to count the number of digits in a numerical value

def X_figure(salary):
    
    tally = 0

    if salary == 0:
        tally += 1

    while salary >= 1:
        salary = salary/10
        tally += 1
    return tally

print("The CEO has a "+ str(X_figure(2300000)) + "-figure salary.")
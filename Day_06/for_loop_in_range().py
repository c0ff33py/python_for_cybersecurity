def count_by_10(end):
    count = ""

    for number in range(0, end+1, 10):
        count += str(number)+ " "

    return count.strip()

print(count_by_10(100)) # should print 0,10,20,30,40,50,60,70,80,90,100
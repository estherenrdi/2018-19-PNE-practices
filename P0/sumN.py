def sum(n):
    total = 0
    for i in range(n):
        total = total + 1 + i

    return total


# .. Maain program
num = int(input("please introduce n: "))
total_sum = sum(num)
print("The total number sum is {}".format(total_sum))

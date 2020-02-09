
# Enter positive integer and perform calculation on it - divide by two if odd and multiply by three and add one if odd

a = int(input("Enter Positive Number: "))

while a != 1:
    if (a % 2) == 0:
        a = a/2
        print(a)

    elif (a % 2) != 0:
        a = (a * 3) + 1
        print(a)
       
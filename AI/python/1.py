# Number = int(input("Enter a number: "))
# for i in range(1, Number + 1):
#     if Number % i == 0:
#         print(i, "is factor of", Number)


# prime

Number = int(input("Enter a number: "))
for i in range(2, Number):
    if Number % i == 0:
        print(Number, "is not a prime number")
        break
    else:
        print(Number, "is a prime number")
        break


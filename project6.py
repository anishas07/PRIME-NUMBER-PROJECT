from math import sqrt
print("Here we are trying find out if a 2 digit number is a prime number or not.")
Num = int(input("Enter a number"))
if Num > 9:
    for k in range(2, int(sqrt(Num))+1):
        if (Num % k) ==0:
            print(Num, "This is not a prime number")
            break
        else:
            print(Num,"This is a prime number")
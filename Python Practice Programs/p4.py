#!usr/bin/python
a = 7
for i in range(1, a-1):
    if a % i == 0 :
        print("The given number ", a, "is not prime")
    else:
        print("The given number ", a, "is prime")

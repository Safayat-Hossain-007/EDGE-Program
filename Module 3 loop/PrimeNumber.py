
def isPrime(loweLimit,upperLimit):
    for n in range(loweLimit, upperLimit):
     for x in range(2, n):
        if n % x == 0:
            print(n," = ", x," x ", n//x)
            break
    else:
        print(n, " is a prime number")

isPrime(1,20);


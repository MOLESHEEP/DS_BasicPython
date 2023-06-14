from math import sqrt


a = input("aの値を入力: ")
b = input("bの値を入力: ")
a = int(a)
b = int(b)
# TODO
def isPrime(n):
    for i in range(2,int(sqrt(n))):
        if n%i==0:
            return False
            break
    return True

print(isPrime(a))
print(isPrime(b))

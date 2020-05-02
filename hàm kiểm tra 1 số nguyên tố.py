def check_prime(number):
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True
def Primes(max):
    number = 1
    while number < max:
        number += 1
        if check_prime(number):
            yield number
primes = Primes(100000000000)
print(primes)
for x in primes:
    print(x)
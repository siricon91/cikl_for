numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for number_one in numbers:
    if number_one == 1:
        continue
    is_prime = True
    for i in range(2, number_one):
        if number_one % i == 0:
            is_prime = False
    if is_prime:
        primes.append(number_one)
    else:
        not_primes.append(number_one)
print("Numbers:", numbers)
print("Primes:", primes)
print("Not Primes:", not_primes)

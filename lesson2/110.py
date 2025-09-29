'''10. Вивести всі елементи масиву, які є простими числами.'''
import random

arr = [random.randint(1, 100) for _ in range(10)]
print("Масив:", arr)
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

primes = [x for x in arr if is_prime(x)]
print("Прості числа з масиву:", primes)

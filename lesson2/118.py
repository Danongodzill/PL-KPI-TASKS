'''8. Замінити всі від’ємні елементи масиву на їх квадрати.'''
import random

arr = [random.randint(1, 100) for _ in range(10)]
print("Масив:", arr)
arr = [random.randint(-50, 50) for _ in range(10)]
print("Початковий масив:", arr)
arr = [x if x >= 0 else x**2 for x in arr]
print("Після заміни:", arr)

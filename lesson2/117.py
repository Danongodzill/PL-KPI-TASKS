'''7. Порахувати кількість елементів масиву, які діляться на 3.'''
import random

arr = [random.randint(1, 100) for _ in range(10)]
print("Масив:", arr)

count = sum(1 for x in arr if x % 3 == 0)
print("Кількість елементів, що діляться на 3:", count)


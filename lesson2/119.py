'''9. Знайти середнє арифметичне елементів масиву, розташованих на
непарних позиціях.'''
import random

arr = [random.randint(1, 100) for _ in range(10)]
print("Масив:", arr)
odd_elements = [arr[i] for i in range(1, len(arr), 2)]
average = sum(odd_elements) / len(odd_elements)
print("Середнє на непарних позиціях =", average)

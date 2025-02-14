numbers = [1, 2, 3, 4, 5]
print("Сумма всех чисел:", sum(numbers))

print("Четные числа:")
for num in numbers:
    if num % 2 == 0:
        print(num)

print("Самое большое число:", max(numbers))

print("Список в обратном порядке:")
for i in range(len(numbers) - 1, -1, -1):
    print(numbers[i])
 
print("Таблица умножения на 5:")
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")
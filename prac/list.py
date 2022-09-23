numbers = [5, 2, 1, 7, 4]
numbers.append(20)
numbers.insert(1, 10)
numbers.remove(5)
numbers.clear()

numbers = [5, 2, 1, 7, 4, 5]
print(numbers.index(7))

print(numbers.count(5))
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

numbers2 = numbers.copy()
print(numbers2)

numbers2.append(10)
numbers.append(14)
print(numbers)
print(numbers2)

numbers = [1, 1, 2, 2, 3, 3]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
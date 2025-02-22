numbers = [2, 5, 7, 4, 11, 5, 18, 10]
largest = 0
for i in numbers:
    if largest < i:
        largest = i

print(largest)

# Methods
print(max(numbers))

numbers.append(12)
print(numbers)

numbers.pop()
print(numbers)

numbers.insert(2, 1)
print(numbers)

numbers.remove(1)
print(numbers)

print(18 in numbers)

print(numbers.index(18))

print(numbers.count(5))

numbers2 = numbers.copy()
print(numbers2)

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

numbers.clear()
print(numbers)

def is_increasing(numbers):
    for i in range(1, len(numbers)):
        if numbers[i] <= numbers[i - 1]:
            return False
    return True

def find_missing(numbers):
    missing= []
    for i in range(min(numbers), max(numbers) + 1):
        if i not in numbers:
            missing.append(i)
    return missing
numbers = [3, 5, 4, 8, 10, 8, 7]

print("Is increasing:", is_increasing(numbers))
print("missing_numbers:", find_missing(numbers))


print(is_increasing([1, 2, 3, 5, 6, 7]))
print(is_increasing([3, 5, 4, 8, 10, 8, 7]))
print(is_increasing([1, 2, 2, 3]))
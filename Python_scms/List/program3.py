#problem 5: Second Largest Number in a List

numbers = [12, 45, 23, 67, 34, 89, 90, 11]
first_largest = second_largest = float('-inf')
for num in numbers:
    if num > first_largest:
        second_largest = first_largest
        first_largest = num
    elif num > second_largest and num != first_largest:
        second_largest = num
print(f"First Largest: {first_largest}, Second Largest: {second_largest}")
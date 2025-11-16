A = [10, 4, 7, 9, 2, 11]

# Initialize largest and smallest
largest = smallest = A[0]

for num in A:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

# Find second largest and second smallest
second_largest = second_smallest = None

for num in A:
    if num != largest:
        if second_largest is None or num > second_largest:
            second_largest = num
    if num != smallest:
        if second_smallest is None or num < second_smallest:
            second_smallest = num

# Calculate average of even numbers
even_sum = 0
even_count = 0

for num in A:
    if num % 2 == 0:
        even_sum += num
        even_count += 1

if even_count > 0:
    avg_even = even_sum / even_count
else:
    avg_even = 0

# Output
print("Second Largest =", second_largest)
print("Second Smallest =", second_smallest)
print("Average of Even numbers = {:.2f}".format(avg_even))

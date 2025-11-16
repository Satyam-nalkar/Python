#problem 6: Unique Elements in a List
elements = [1, 2, 2, 3, 4, 4, 5]
unique_elements = []
for elem in elements:
    if elem not in unique_elements:
        unique_elements.append(elem)
print(f"Unique elements: {unique_elements}")
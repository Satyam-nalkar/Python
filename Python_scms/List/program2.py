list1 = [1, 2, 3, 4, 5]
print(list1)
largest = 0

for num in list1:
    if num > largest:
        largest = num

if largest:
    list1.pop(list1.index(largest))
print(list1)

'''largest = 0
for num in list1:
    if num > largest:
        largest = num

print(largest)'''


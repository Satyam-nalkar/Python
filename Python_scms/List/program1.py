'''nums = [10, 20, 30, 40, 50]
total = 0
for num in nums:
    total += num
average = total / len(nums)
print(f"Sum: {total}, Average: {average}")

# take the input from the user
nums = input("Enter a list of numbers separated by spaces: ")
nums = list(map(int, nums.split()))
print(nums)
nums = [int(x) for x in input("Enter numbers: ").split()]
print(nums)'''


nums = []
while True:
    val = input("Enter a number (or press Enter to stop): ")
    if not val:
        break
    nums.append(int(val))
print(nums)
 


print(f"The given list is: {nums}")
total = sum(nums)
average = total / len(nums) if nums else 0
print(f"Sum: {total}, Average: {average}")
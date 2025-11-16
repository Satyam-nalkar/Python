# nums = [2,7,11,15,4,5]
# target = 9

# result = []
# for num in nums:
#     for num_2 in nums[nums.index(num) +1:]:
#         if(num + num_2 == target):
#             result.append([nums.index(num),nums.index(num_2)])
# print(result)  

# nums = [2,7,11,15,4,5]
# target = 9

# result = []
# for index, num in enumerate(nums):
#     for index_2 num_2 in enumerate(nums[index + 1:]):
        
#         if(num + num_2 == target):
#             result.append((index,index + 1 + index_2))
# print(result)  


s = input("Enter the string :")

max_len = 0
left = 0

x = set()

for right in range(len(s)):
    while s[right] in x:
        x.remove(s[left])
        left += 1
    x.add(s[right])
    max_len = max(max_len,right - left + 1)

print(max_len)




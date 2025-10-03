names = ("alice","bob","eve","devid","alice")

a = names.count("alice")
print(a)


y = names.index("bob")
print(y)

sliced_tuple = names[1:3]
print(f"sliced tuple:{sliced_tuple}")



sorted_tuple = sorted(names)
print(f"the sorted tuple is:{sorted_tuple}")

print(len(names))



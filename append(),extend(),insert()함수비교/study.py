nums = [1,2,3]
nums.append(4)

print(nums)

nums.append([5,6])
print(nums)

nums.extend([4, 5])
print(nums)

a = [10]
nums.extend(a)

print(nums)

nums.insert(0, [10, 20])

print(nums)

nums.insert(len(nums), 100)
print(nums)
nums1 = [1, 3, 2, 4, 5, 3, 10, 11]
nums2 = [1, 2, 3, 1, 4, 5, 5, 3, 12]
nums3 = []
for num in nums1:
    if num in nums2 and num not in nums3:
        nums3.append(num)
print(nums3)
# Given an array of integers, find the first missing positive integer in linear time and constant space.
# In other words, find the lowest positive integer that does not exist in the array.
# The array can contain duplicates and negative numbers as well.
#
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
#
# You can modify the input array in-place.


def find_first_missing(nums):
    for num in nums:
        if 0 < num <= len(nums):
            nums[num - 1] = True
    for i in range(0, len(nums)):
        if nums[i] is not True:
            return i + 1
    return len(nums) + 1


if __name__ == '__main__':
    print(find_first_missing([3, 4, -1, 1]))
    print(find_first_missing([1, 2, 0]))

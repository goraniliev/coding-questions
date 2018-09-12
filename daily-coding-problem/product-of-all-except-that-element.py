# Given an array of integers, return a new array such that
# each element at index i of the new array is the product of
# all the numbers in the original array except the one at i.
#
# For example, if our input was [1, 2, 3, 4, 5],
# the expected output would be [120, 60, 40, 30, 24].
# If our input was [3, 2, 1],
# the expected output would be [2, 3, 6].

def product_of_all_except_current_el(nums):
    product = 1
    for num in nums:
        product *= num
    return [product // num for num in nums]


if __name__ == '__main__':
    print(product_of_all_except_current_el([1, 2, 3, 4, 5]))
    print(product_of_all_except_current_el([3, 2, 1]))

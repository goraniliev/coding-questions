# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#
# Bonus: Can you do this in one pass?


def has_pair_with_sum_k(nums, k):
    seen_set = set()

    for num in nums:
        complement = k - num
        if complement in seen_set:
            return True
        seen_set.add(num)

    return False


if __name__ == '__main__':
    nums = [10, 15, 3, 7]
    k = 17
    print(has_pair_with_sum_k(nums, k))
    print(has_pair_with_sum_k(nums, 23))
    print(has_pair_with_sum_k(nums, 25))


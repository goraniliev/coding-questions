# Given an integer k and a string s, find the length of
# the longest substring that contains at most k distinct characters.
#
# For example, given s = "abcba" and k = 2,
# the longest substring with k distinct characters is "bcb".

def get_longest(k, s):
    counts = dict()
    left = 0
    max_len_s = ''
    for i, val in enumerate(s):
        if val in counts:
            counts[val] += 1
        else:
            counts[val] = 1
            while len(counts) > k:
                counts[s[left]] -= 1
                if counts[s[left]] == 0:
                    counts.pop(s[left])
                left += 1
        if i - left + 1 > len(max_len_s):
            max_len_s = s[left:i + 1]
    return max_len_s


if __name__ == '__main__':
    print(get_longest(2, 'abcba'))
    print(get_longest(3, 'abcbcadfdaa'))
    print(get_longest(3, 'abcbacdfdaaaaaaaa'))
    print(get_longest(1, 'abcdefghiijklmnoprstq'))
    print(get_longest(2, 'abcdefghijklmabcdefii'))
    print(get_longest(1, 'aabcd'))
    print(get_longest(3, 'abcabc'))

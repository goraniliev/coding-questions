# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
#
# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
#
# You can assume that the messages are decodable. For example, '001' is not allowed.

def decode_message_ways(encoded):
    n = len(encoded) + 1
    dp = [0 for i in range(n)]
    encoded = '0' + encoded
    dp[0] = 1
    for i in range(1, n):
        dp[i] += dp[i - 1]
        if i > 1 and 1 <= int(encoded[i - 1:i + 1]) <= 26:
            dp[i] += dp[i - 2]
    print(dp)
    return dp[-1]


if __name__ == '__main__':
    print(decode_message_ways('111'))
    print(decode_message_ways('1111'))
    print(decode_message_ways('11111'))
    print(decode_message_ways('125'))
    print(decode_message_ways('128'))
    print(decode_message_ways('999'))
    print(decode_message_ways('9123'))
    print(decode_message_ways('9876543212345'))

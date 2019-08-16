# Eggs and sand (0 and 1)
input = '111100000001111010101111001111101011000001010100010101100100001011010110111111111100000110100010000101001111100100000110101100110000100100010101011100111101001010101101110111101010010100001111'

# The wheel, repeated to be >192 bits
wheel = '11100101100'
for i in range(0, 18):
    wheel += '11100101100'

# Permutations of wheel
# 'iter' is the offset to test
for iter in range(0, 11):
    password = ''
    for idx, bit in enumerate(list(input)):
        if bit != list(wheel)[idx+iter]:
            password += '1'
        else:
            password += '0'

    print('Password %d: %s' % (iter, password))
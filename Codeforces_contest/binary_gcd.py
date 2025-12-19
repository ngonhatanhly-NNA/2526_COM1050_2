def binary_gcd (a, b):
    if a == 0: return b
    if b == 0: return a

    shift = 0
    # The belowing is to ask if a and b even numbers -> 1 is 001
    # when a and b is even, their last digit is 0 -> whatever the comparision is 001 will check if a and b is both even, if none, their is one odd or both odd
    while ((a | b) & 1) == 0:
        a >>= 1  # if even divide by 2 110 -> 011 ( <<: multiple by 2: 110 -> 1100)
        b >>= 1
        shift += 1
    # | bitwise or: Ex: 5 | 3 <=> 101 | 011 -> result = 111 (either or both is 1)
    # & bitwise and Ex: 5 & 3 <=> 101 & 011 -> result = 001 = 1
    while (a & 1) == 0: # while a is even, a //= 2 -> find the smallest common even
        a >>= 1
    while b != 0:
        while (b & 1) == 0:
            b >>= 1

        if a > b:
            a, b = b, a
        b = b - a

    return a << shift
#Given an array of integers, where all elements but one occur twice, find the unique element.

def lonelyinteger(a):
    hash = {}
    for i in a:
        if i in hash:
            hash[i] += 1
        else:
            hash[i] = 1
    print(hash)
    for k in hash:
        if hash[k] == 1:
            return k
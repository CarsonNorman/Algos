# Sherlock considers a string to be valid if all characters of the string appear the same number of times. 
# It is also valid if he can remove just  character at  index in the string, and the remaining characters will occur the same number of times. 
# Given a string , determine if it is valid. If so, return YES, otherwise return NO.

def isValid(s):
    hash = {}
    for char in s:
        if char in hash: hash[char] = hash[char] + 1;
        else: hash[char] = 1
    vals = list(hash.values())
    print(vals)
    if all(val == vals[0] for val in vals):
        return 'YES'
    elif (1 in vals):
        vals.remove(1)
        if all(val == vals[0] for val in vals):
            return 'YES'
        else:
            return 'NO'
    else:
        vals[vals.index(max(vals))] -=1
        if all(val == vals[0] for val in vals):
            return 'YES'
        else:
            return 'NO'

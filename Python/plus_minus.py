# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with 6 places after the decimal.

# Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to 10^-4 are acceptable.


def plusMinus(arr):
    #initialize our base for each of our counts
    pos, neg, zero = 0,0,0
    #loop through given list assigning each item to the associated variable
    for num in arr:
        if num == 0: zero +=1
        elif num > 0: pos +=1
        else: neg += 1
    total = len(arr)
    #return our answers rounded to 6 decimal places
    print(round((pos/total), 6))
    print(round((neg/total), 6))
    print(round((zero/total), 6))
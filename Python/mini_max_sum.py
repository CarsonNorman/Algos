#Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. 
#Then print the respective minimum and maximum values as a single line of two space-separated long integers.

#Explanation
#The smallest number we can get out of an arr of n elements by adding n-1 elements together is always going to be every index added except for the largest number
#The same logic applies to getting the largest possible sum of n-1 elements
#therefore all we need to do is identify the max and min in our given set of values to get our answer
def miniMaxSum(arr):
    maxInt = max(arr)
    minInt = min(arr)
    total = sum(arr)
    print((total - maxInt), (total - minInt))
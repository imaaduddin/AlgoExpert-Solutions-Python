# My solution so far:
def twoNumberSum(array, targetSum):
    # Write your code here.
    for i in range(len(array)):
        for j in range(len(array + 1)):
            if array[i] + array[j] == targetSum:
                return [i, j]
            else:
                return []
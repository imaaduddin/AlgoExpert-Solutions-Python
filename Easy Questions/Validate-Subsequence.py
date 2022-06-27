# My solution: (passed 9/24 test cases)
def isValidSubsequence(array, sequence):
    # Write your code here.
    for num in range(len(array)):
        position = []
        if array[num] == sequence[num]:
            position.append(num)
    if position == sequence:
        return True
    else:
        return False
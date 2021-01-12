# O(n^2) time | O(1) Space
# def twoNumberSum(array, targetSum):
#     for i in range(len(array)):
#         firstNum = array[i]
#         for j in range(i+1, array[j]):
#             secondNum = array[j]
#             if firstNum + secondNum == targetSum:
#                 return [firstNum,secondNum]
#     return []


# O(n) time | O(n) space
# def twoNumberSum(array, targetSum):
#     nums = {}
#     for num in array:
#         if targetSum - num in nums:
#             return [targetSum-num, num]
#         else:
#             nums[num] = True
#     return []

# O(nlog(n)) time | O(1) space
def twoNumberSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1
    return []


arrays = [6, 5, -1, -4, 8, 6, 11]
target = 10

print(twoNumberSum(arrays, target))

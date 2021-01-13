# O(n) time | O(1) space

# def isMonotonic(array):
#     if len(array) <= 2:
#         return True
#
#     direction = array[1] - array[0]
#     for i in range(2, len(array)):
#         if direction == 0:
#             direction = array[i] - array[i - 1]
#             continue
#         if breaksDirection(direction, array[i - 1], array[i]):
#             return False
#
#     return True
# def breaksDirection(direction, previousInt, currentInt):
#     difference = currentInt - previousInt
#     if direction > 0:
#         return difference < 0
#     return difference > 0

# O(n) times | O(1) Space
def isMonotonic(array):
    isNonDecreasing = True
    isNonIncreasing = True
    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            isNonDecreasing = False
        if array[i] > array[i - 1]:
            isNonDecreasing = False
    return isNonDecreasing or isNonIncreasing


array = [-1, -5, -10, -110, -120, -1100, -1100, -1900, -9000]
result = isMonotonic(array)
print(result)

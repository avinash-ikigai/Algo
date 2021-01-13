# O(n) time | O(1) Space

def moveElementToEnd(array, toMove):
    i = 0
    j = len(array) - 1
    while i < j:
        while i < j and array[j] == toMove:
            j -= 1
        if array[i] == toMove:
            array[i], array[j] = array[j], array[i]
        i += 1
    return array


array = [2, 1, 2, 3, 2, 2, 4, 2, 2, 2]
move = 2
result = moveElementToEnd(array, move)
print(result)

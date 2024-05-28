a = [[1, 2, 3], [4, 5, 6]]
b = [{f'k{index + 1}': array[index] for index in range(len(array))} for array in a]
print(b)

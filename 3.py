a = [[1, 2, 3], [4, 5, 6]]
b = [{f'k{index + 1}': value for index, value in enumerate(array)} for array in a]
print(b)

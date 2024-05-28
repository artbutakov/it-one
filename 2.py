m = [{11, 3, 5}, {2, 17, 87, 32}, {4, 44}, {24, 11, 9, 7, 8}]

all_numbers_in_tuple = tuple(number for array in m for number in array)
amount_of_numbers = len(all_numbers_in_tuple)
total_summary = sum(all_numbers_in_tuple)
average = total_summary / amount_of_numbers

for index, result in enumerate((amount_of_numbers, total_summary, average, all_numbers_in_tuple)):
    print(f'{index + 1}. {result}')

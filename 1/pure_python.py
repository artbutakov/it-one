import csv


def find_unique_rows(array: list or tuple):
    return tuple({'_'.join(row.values()): row for row in array}.values())


def find_rows_with_the_same_id(array: list or tuple):
    sorted_rows = dict()
    rows_with_the_same_id = dict()
    for row in array:
        id_ = row.get('id')
        value = sorted_rows.get(id_)
        if value:
            sorted_rows[id_].append(row)
        else:
            sorted_rows[id_] = [row]
    for id_, rows in sorted_rows.items():
        if len(rows) > 1:
            unique_strings = set()
            unique_data_rows = list()
            for row in rows:
                row.pop('id')
                string = '_'.join(row.values())
                if string not in unique_strings:
                    unique_strings.add(string)
                    unique_data_rows.append(row)
                    if len(unique_strings) > 1:
                        rows_with_the_same_id[id_] = unique_data_rows
    return rows_with_the_same_id


with open('f.csv', 'r', encoding='utf-8') as file:
    data = tuple(row for row in csv.DictReader(file, delimiter='|'))


unique_rows = find_unique_rows(data)
same_id_rows = find_rows_with_the_same_id(data)

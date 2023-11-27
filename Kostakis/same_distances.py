def same_distances(dictionary):
    unique_values = {}
    duplicates = []

    for value in dictionary.values():
        if value in unique_keys:
            duplicates.append(value)
        else:
            unique_keys[value] = None

    return duplicates


d = {(1,2):4,(2,3):5,(7,6):10,(5,9):4}
print(same_distances(d))

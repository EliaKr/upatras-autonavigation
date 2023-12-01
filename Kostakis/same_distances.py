def same_distances(dictionary):
    result = {}
    for key, value in dictionary.items():
        result.setdefault(value, []).append(key)
    return {k: v for k, v in result.items() if len(v) > 1}

d = {(1,2):6,(2,3):5,(7,6):5,(5,9):6}
print(same_distances(d))

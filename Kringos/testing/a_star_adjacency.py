# Reference: https://stackabuse.com/courses/graphs-in-python-theory-and-implementation/lessons/a-star-search-algorithm/
# Δημιουργία του adjacency list που περιέχει μόνο τα ελεύθερα σημεία από τον πίνακα για χρήση με τον παραπάνω αλγόριθμο.

# example of adjacency list (or rather map)
# adjacency_list = {
# 'A': [('B', 1), ('C', 3), ('D', 7)],
# 'B': [('D', 5)],
# 'C': [('D', 12)]
# }

def gen_adjacency_list(coord_matrix):
    adjacency_list = {}
    check_list = [-1,1]
    for x in coord_matrix:
        for y in x:
            temp_list = []
            for i in check_list:
                for l in check_list:
                    try:
                        if type(coord_matrix[coord_matrix.index(x) + i][coord_matrix[coord_matrix.index(x)].index(y) + l]) == tuple:
                            temp_list.append(coord_matrix[coord_matrix.index(x) + i][coord_matrix[coord_matrix.index(x)].index(y) + l])
                    except Exception as err:
                        print(err)
            adjacency_list.update({y: temp_list})

    return adjacency_list
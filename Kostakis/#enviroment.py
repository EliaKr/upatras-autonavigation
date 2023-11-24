#enviroment.py

matrix = [[1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 1, 0, 0, 1, 1], [1, 0, 0, 0, 1, 0, 0, 1, 1], [1, 0, 0, 0, 1, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 'end', 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1]]
start_x = 2
start_y = 3
end_x = 3
end_y = 5
dimension_x = 4
dimension_y = 6
#επιστρέφει λίστα της μορφής [(x,y)]
def detect_poss():
    current_x = start_x
    current_y = start_y
    can_do_moves=[]
    for i in range (-1,2):
        for p in range(-1,2):
            if matrix[current_x + i][current_y + p]==0:
                can_do_moves.append((current_x + i, current_y + p))
    try:
        can_do_moves.remove((current_x, current_y))

    return can_do_moves

print(detect_poss())








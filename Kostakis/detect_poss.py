
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
    except Exception:
        pass

    return can_do_moves
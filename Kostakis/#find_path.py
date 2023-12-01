#find_path


matrix = [[1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 1, 0, 0, 1, 1], [1, 0, 0, 0, 1, 0, 0, 1, 1], [1, 0, 0, 0, 1, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 'end', 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1]]
start_x = 2
start_y = 3
end_x = 3
end_y = 5
dimension_x = 4
dimension_y = 6

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

print(detect_poss())

def find_path():
    can_do_moves = detect_poss()
    for i in can_do_moves:
        x = (can_do_moves[can_do_moves.index(i)][0])
        y = (can_do_moves[can_do_moves.index(i)][1])
        distance = (((end_x - x)**2 + (end_y - y)**2)**0.5)
        d = {}
        d.update({can_do_moves[i]: distance})
    return d


print(find_path())






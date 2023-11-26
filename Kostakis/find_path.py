
def find_path():
    can_do_moves = detect_poss()
    for i in can_do_moves:
        x = (can_do_moves[i][0])
        y = (can_do_moves[i][1])
        distance = (((end_x - x)**2 + (end_y - y)**2)**0.5)
        d = {}
        d.update({can_do_moves[i]: distance})
    return d

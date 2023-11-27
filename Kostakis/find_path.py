
def find_path():
    can_do_moves = detect_poss()
    for i in can_do_moves:
        x = i[0]
        y = i[1]
        distance = (((end_x - x)**2 + (end_y - y)**2)**0.5)
        d = {}
        d.update({distance : can_do_moves[can_do_moves.index(i)] })
    d = sorted(d)
    return d

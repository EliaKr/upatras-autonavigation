def check_blockage( next_point_x,  next_point_y, current_x, current_y):
    available_points = []
    z = detect_poss(next_point_x, next_point_y) 
    z.remove((current_x, current_y))
    if not (next_point_x, next_point_y + 1) and (next_point_x, next_point_y - 1) and (next_point_x + 1, next_point_y) and (next_point_x - 1, next_point_y) in z:
        return (next_point_x, next_point_y)
    else:
        return None






    

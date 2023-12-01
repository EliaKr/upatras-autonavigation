def check_blockage( next_point[0],  next_point[1], current_x, current_y):
    available_points = []
    z = detect_poss(next_point[0], next_point[1]) 
    z.remove((current_x, current_y))
    if not (next_point[0], next_point[1] + 1) and (next_point[0], next_point[1] - 1) and (next_point[0] + 1, next_point[1]) and (next_point[0] - 1, next_point[1]) in z:
        return (next_point[0], next_point[1])
    else:
        return None



    
        




    

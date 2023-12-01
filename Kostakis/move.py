def move(current_x=start_x,current_y=start_y):
    done_moves = [(start_x,start_y)]
    ban_moves = []
    while check_position(current_x,current_y,end_x,end_y)== True:
        d_pos_moves= find_path(current_x,current_y)
        del d_pos_moves[check_diagonal_blockage(current_x,current_y)]
        if same_distances(d_pos_moves)=={}:
            next_point= list(d_pos_moves.keys())[0]
            if check_blockage( next_point[0],  next_point[1], current_x, current_y) == (next_point[0],  next_point[1]):
                del d_pos_moves[(next_point[0],  next_point[1])]
            elif check_blockage( next_point[0],  next_point[1], current_x, current_y) == None:
                current_x =next_point[0]
                current_y =next_point[1]
                done_moves.append(next_point)
                check_position(current_x,current_y,end_x,end_y)
        elif same_distances(d_pos_moves)!={}:
            ban_point= bsdr(current_x,current_y) 
            del d_pos_moves[ban_point]
            next_point= list(d_pos_moves.keys())[0]#κατι λειπει απο την check_diagonal_blockage εχει παιχτει μαλακια
             if check_blockage( next_point[0],  next_point[1], current_x, current_y) == (next_point[0],  next_point[1]):
                del d_pos_moves[(next_point[0],  next_point[1])]
            elif check_blockage( next_point[0],  next_point[1], current_x, current_y) == None:
                current_x =next_point[0]
                current_y =next_point[1]
                done_moves.append(next_point)
                check_position(current_x,current_y,end_x,end_y)
    return done_moves

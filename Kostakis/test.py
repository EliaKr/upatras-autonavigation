matrix = [[1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 1, 1, 1], [1, 1, 1, 0, 1, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1]]
start_x = 2
start_y = 3
end_x = 3
end_y = 5

def bsdr(current_x,current_y):
    res = same_distances(find_path(current_x,current_y))
    sorted_res = dict(sorted(res.items()))
    sd_pos=list(sorted_res.values())[0]
    f_p = sd_pos[0]
    s_p = sd_pos[1]
    f_d = find_path(f_p[0],f_p[1])
    s_d = find_path(s_p[0],s_p[1])
    
    if same_distances(find_path(f_p[0],f_p[1]))==same_distances(find_path(s_p[0],s_p[1]))=={}:
        if list(f_d.values())[0] < list(s_d.values())[0]:
            return s_p #Κανουμε return s_p διοτι εν συνεχεια θελουμε να διαγραφει απο το dictionary της find_path αφου το f_p αποτελει καταλληλοτερη επιλογη
        elif list(f_d.values())[0] > list(s_d.values())[0]:
            return f_p
    else: 
        print('ισες και δευτερες αποστασεις επιστρεφω s_p')
        return s_p #να επιδιορθωθει

def check_blockage( next_point_x,  next_point_y, current_x, current_y):
    available_points = []
    z = detect_poss(next_point_x, next_point_y) 
    z.remove((current_x, current_y))
    if not (next_point_x, next_point_y + 1) and (next_point_x, next_point_y - 1) and (next_point_x + 1, next_point_y) and (next_point_x - 1, next_point_y) in z:
        return (next_point_x, next_point_y)
    else:
        return None


def check_diagonal_blockage(done_moves,current_x=start_x,current_y=start_y):
    if matrix[current_x + 1][current_y]==1 and matrix[current_x][current_y + 1]==1:
        return (current_x + 1 , current_y + 1)
    if matrix[current_x + 1][current_y]==1 and matrix[current_x][current_y - 1]==1:
        return (current_x + 1, current_y - 1)
    if matrix[current_x - 1 ][current_y]==1 and matrix[current_x][current_y + 1]==1:
        return (current_x - 1,current_y + 1)
    if matrix[current_x - 1][current_y]==1 and matrix[current_x][current_y - 1]:
        return (current_x - 1 , current_y - 1)

def check_position(current_x,current_y,end_x,end_y):
    if current_x!=end_x or current_y!=end_y:
        return True
    elif current_x==end_x and current_y==end_y:
        return False 

def detect_poss(current_x=start_x,current_y=start_y):
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

def find_path(current_x=start_x,current_y=start_y):
    can_do_moves = detect_poss(current_x,current_y)
    d = {}
    for i in can_do_moves:
        x = i[0]
        y = i[1]
        distance = (((end_x - x)**2 + (end_y - y)**2)**0.5)
        d.update({can_do_moves[can_do_moves.index(i)] : distance })
    sorted_d = dict(sorted(d.items(), key=lambda x:x[1]))

    return sorted_d

def move(current_x=start_x,current_y=start_y):
    done_moves = [(start_x,start_y)]
    ban_moves = []
    while check_position(current_x,current_y,end_x,end_y)== True:
        d_pos_moves= find_path(current_x,current_y)
        try:
            del d_pos_moves[check_diagonal_blockage(current_x,current_y)]
        except: None
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
            next_point= list(d_pos_moves.keys())[0]
            if check_blockage( next_point[0],  next_point[1], current_x, current_y) == (next_point[0],  next_point[1]):
                del d_pos_moves[(next_point[0],  next_point[1])]
            elif check_blockage( next_point[0],  next_point[1], current_x, current_y) == None:
                current_x =next_point[0]
                current_y =next_point[1]
                done_moves.append(next_point)
                check_position(current_x,current_y,end_x,end_y)
    return done_moves

def same_distances(dictionary):
    result = {}
    for key, value in dictionary.items():
        result.setdefault(value, []).append(key)
    return {k: v for k, v in result.items() if len(v) > 1}


print(move(start_x,start_y))

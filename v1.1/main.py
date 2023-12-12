import random
import flet
from matplotlib import pyplot as plt
import time
import datetime

def initialise():
    while True:
        try:
            dimension_x = int(input("Παρακαλώ εισάγετε την διάσταση της πίστας στον άξονα των x, λαμβάνοντας υπ'όψιν ότι η πίστα περιβάλλεται από τοίχο πάχους 1 pixel. (x>6):"))
            if dimension_x > 6: 
                break
            else: 
                print("Προσπαθήστε Ξανά.") 
        except Exception:
            print("Προσπαθήστε Ξανά.")
    
    while True:
        try:
            dimension_y = int(input("Παρακαλώ εισάγετε την διάσταση της πίστας στον άξονα των y, λαμβάνοντας υπ'όψιν ότι η πίστα περιβάλλεται από τοίχο πάχους 1 pixel. (x*y>=36):"))
            if dimension_x * dimension_y >= 36: 
                break
            else: 
                print("Προσπαθήστε Ξανά.")
        except Exception:
            print("Προσπαθήστε Ξανά.")

    while True:
        try:
            start_coords = input("Παρακαλώ εισάγετε τις συντεταγμένες όπου θα ξεκινήσει το όχημα σε μορφή (x,y), λαμβάνοντας υπ'όψιν ότι η πίστα περιβάλλεται από τοίχο πάχους 1 pixel.:")
            coord_list = start_coords.split(",")
            start_x = int(coord_list[0])
            start_y = int(coord_list[1])
            if start_x > 1 and start_x < dimension_x - 1 and start_y > 1 and start_y < dimension_y - 1: 
                break
            else: 
                print("Προσπαθήστε Ξανά.")
        except Exception:
            print("Προσπαθήστε Ξανά.")

    while True:
        try:
            end_coords = input("Παρακαλώ εισάγετε τις συντεταγμένες όπου θέλετε να τερματίσει το όχημα σε μορφή (x,y), λαμβάνοντας υπ'όψιν ότι η πίστα περιβάλλεται από τοίχο πάχους 1 pixel.:")
            coord_list = end_coords.split(",")
            end_x = int(coord_list[0])
            end_y = int(coord_list[1])
            if end_x > 1 and end_x < (dimension_x - 2) and end_y > 1 and end_y < (dimension_y - 2): 
                break
            else: 
                print("Προσπαθήστε Ξανά.")
        except Exception:
            print("Προσπαθήστε Ξανά.")
    
    while True:
        try:
            density = int(input("Παρακαλώ εισάγετε την πυκνότητα των εμποδίων σε βαθμό 1-3:"))
            if density > 0 and density <= 3: 
                break
            else: 
                print("Προσπαθήστε Ξανά.")
        except Exception:
            print("Προσπαθήστε Ξανά.")
    
    return dimension_x, dimension_y, start_x, start_y, end_x, end_y, density

def gen_matrix(dimension_x, dimension_y, start_x, start_y, end_x, end_y, density):
    # Δημιουργία λίστας ανάλογα με το density των εμποδίων
    elements = []
    for i in range(10):
        elements.append(0)
    for i in range(density):
        elements[i] = 1

    # Δημιουργία πίνακα, όπου 1 σημαίνει πως έχω εμπόδιο
    while True: 
        matrix = []
        for y in range(dimension_y):
            matrix.append([])
            for x in range(dimension_x):
                matrix[y].append(random.choice(elements))
        # Δημιουργία τοίχων
        for i in range(0,dimension_y): 
            matrix[i][0]=1
            matrix[i][dimension_x - 1]=1
        for i in range(0,dimension_x): 
            matrix[0][i]=1
            matrix[dimension_y - 1][i]=1

        #Τοποθέτηση αρχής, τέλους.
        matrix[start_y][start_x] = "start"
        matrix[end_y][end_x] = "end"
        break
        
        # Έλεγχος εαν αρχικά το όχημα ή ο στόχος βρίσκεται "παγιδευμένο" μέσα σε εμπόδια σε ακτίνα ενός pixel. # Δεν χρειάζεται αφού γίνεται έλεγχος μην επιλύσιμης διαδρομής.
        results = []
        for i in range(-1,2):
            for z in range(-1,2):
                if matrix[start_y + i][start_x + z] != 1: 
                    results.append(0)
                else: 
                    results.append(1)
                if matrix[end_y + i][end_x + z] != 1: 
                    results.append(0)
                else: 
                    results.append(1)
        if sum(results) == 0:
            break
    
    return matrix

def gen_layout(x):
    layout = x.copy()

    for x in layout:
        for y in x:
            if y == 0: 
                layout[layout.index(x)][layout[layout.index(x)].index(y)] = [255, 255, 255]
            elif y == 1: 
                layout[layout.index(x)][layout[layout.index(x)].index(y)] = [0, 0, 0]
            elif y == "start": 
                layout[layout.index(x)][layout[layout.index(x)].index(y)] = [0, 255, 0]
            elif y == "end": 
                layout[layout.index(x)][layout[layout.index(x)].index(y)] = [255, 0, 0]
    
    return layout

def solve(matrix):
    for i in range(len(matrix)):
        inner_list = matrix[i]
        if 'start' in inner_list:
            start_y = i
            start_x = inner_list.index('start')

    for p in range(len(matrix)):
        inner_list = matrix[p]
        if 'end' in inner_list:
            end_y = p
            end_x = inner_list.index('end')


    matrix[end_y][end_x] = 0
    matrix[start_y][start_x] = 0

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
            #print('ισες και δευτερες αποστασεις επιστρεφω s_p')
            return s_p #να επιδιορθωθει

    def check_blockage( next_point_x,  next_point_y, current_x, current_y):
        available_points = []
        z = detect_poss(next_point_x, next_point_y) 
        z.remove((current_y,current_x))
        if not ( next_point_y + 1,next_point_x) and (next_point_y - 1,next_point_x ) and (next_point_y,next_point_x + 1 ) and (next_point_y,next_point_x - 1 ) in z:
            return (next_point_y,next_point_x )
        else:
            return None


    def check_diagonal_blockage(done_moves,current_x=start_x,current_y=start_y):
        if matrix[current_y][current_x + 1]==1 and matrix[current_y + 1][current_x]==1:
            return ( current_y + 1,current_x + 1 )
        if matrix[current_y][current_x + 1]==1 and matrix[current_y - 1][current_x]==1:
            return (current_y - 1,current_x + 1 )
        if matrix[current_y][current_x - 1 ]==1 and matrix[current_y + 1][current_x]==1:
            return (current_y + 1,current_x - 1)
        if matrix[current_y][current_x - 1]==1 and matrix[current_y - 1][current_x]==1:
            return (current_y - 1 ,current_x - 1 )

    def check_position(current_x,current_y,end_x,end_y):
        if current_x!=end_x or current_y!=end_y:
            return True
        elif current_x==end_x and current_y==end_y:
            return False 

    def detect_poss(current_x=start_x,current_y=start_y):
        can_do_moves=[]
        for i in range (-1,2):
            for p in range(-1,2):
                if matrix[current_y + p][current_x + i]==0:
                    can_do_moves.append(( current_y + p,current_x + i))
        try:
            can_do_moves.remove((current_y,current_x ))
        except Exception:
            pass

        return can_do_moves

    def find_path(current_x=start_x,current_y=start_y):
        can_do_moves = detect_poss(current_x,current_y)
        d = {}
        for i in can_do_moves:
            y = i[0]
            x = i[1]
            distance = (((end_x - x)**2 + (end_y - y)**2)**0.5)
            d.update({can_do_moves[can_do_moves.index(i)] : distance })
        sorted_d = dict(sorted(d.items(), key=lambda x:x[1]))

        return sorted_d

    def move(current_x=start_x,current_y=start_y):
        done_moves = [(start_y,start_x)]
        ban_moves = []
        global unsolvable 
        unsolvable = False
        while check_position(current_x,current_y,end_x,end_y)== True and unsolvable == False:
            d_pos_moves= find_path(current_x,current_y)
            try:
                del d_pos_moves[check_diagonal_blockage(current_x,current_y)]
            except Exception : None
            if same_distances(d_pos_moves)=={}:
                next_point= list(d_pos_moves.keys())[0]
                if check_blockage( next_point[1],  next_point[0], current_x, current_y) == (next_point[0],  next_point[1]):
                    del d_pos_moves[(next_point[0],  next_point[1])]
                elif check_blockage( next_point[1],  next_point[0], current_x, current_y) == None:
                    current_x =next_point[1]
                    current_y =next_point[0]
                    done_moves.append(next_point)
                    check_position(current_x,current_y,end_x,end_y)
                    try:
                        if done_moves[-1]==done_moves[-3]==done_moves[-5]==done_moves[-7]==done_moves[-9]:
                            unsolvable = True
                            done_moves = done_moves[:len(done_moves) - 8]
                        
                    except Exception:
                        pass

            elif same_distances(d_pos_moves)!={}:
                ban_point= bsdr(current_x,current_y) 
                try: 
                    del d_pos_moves[ban_point]
                except Exception: pass
                next_point= list(d_pos_moves.keys())[0]
                if check_blockage( next_point[1],  next_point[0], current_x, current_y) == (next_point[0], next_point[1]):
                    del d_pos_moves[(next_point[0],  next_point[1])]
                elif check_blockage( next_point[1],  next_point[0], current_x, current_y) == None:
                    current_x =next_point[1]
                    current_y =next_point[0]
                    done_moves.append(next_point)
                    check_position(current_x,current_y,end_x,end_y)
        return done_moves

    def same_distances(dictionary):
        result = {}
        for key, value in dictionary.items():
            result.setdefault(value, []).append(key)
        return {k: v for k, v in result.items() if len(v) > 1}
    

    return move()

def plot(positions, solvingtime_ms = "Unknown", distance_travelled = "Unknown", unsolvable = False):
    x = []
    y = []
    for i in positions:
        x.append(i[0])
        y.append(i[1])
    if unsolvable == False:
        plt.xlabel(f"Solving Time: {solvingtime_ms}ms, Distance Travelled: {distance_travelled}")
    else:
        plt.xlabel(f"Unsolvable")
    
    plt.plot(x, y, "b-", linewidth=8.0)

def calcdist(positions):
    distance = 0
    for i in positions:
        x_prev = positions[(positions.index(i) - 1)][0]
        x_current = i[0]
        y_prev = positions[(positions.index(i) - 1)][1]
        y_current = i[1]

        if positions.index(i) > 0:
            distance += ((x_current - x_prev)** 2 + (y_current - y_prev)** 2)** 0.5
    return distance

def savefile(matrix):
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H-%M-%S") 
    f = open(f"matrix_{formatted_datetime}.txt", 'w', encoding = 'utf-8' )
    f.write(str(matrix))
    f.close
    print (f.name)

matrix = gen_matrix(*initialise())
savefile(matrix)

start_time =  time.process_time()
positions = solve(matrix)
solvingtime_ms = (time.process_time() - start_time) * 1000

distance_travelled = calcdist(positions)

plt.imshow(gen_layout(matrix))
print(positions)
plot(positions, solvingtime_ms, distance_travelled, unsolvable)
plt.show()
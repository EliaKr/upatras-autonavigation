import random
import flet
from matplotlib import pyplot as plt
import time
import copy
import flet as ft

def ginit(page: ft.Page):
    # Βασικές Παράμετροι
    page.window_resizable = True
    page.window_maximized = True
    
    page.title = "Initialise Parameters"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Ορισμός Συναρτήσεων
    def checkparameters(e):
        global values
        try:
            if int(dimension_x.value) > 6 and (int(dimension_x.value) * int(dimension_y.value)) >= 36 and int(start_x.value) > 1 and int(start_x.value) < int(dimension_x.value) and int(start_y.value) > 1 and int(start_y.value) < int(dimension_y.value) and int(end_x.value) > 1 and int(end_x.value) < (int(dimension_x.value) - 1) and int(end_y.value) > 1 and int(end_y.value) < (int(dimension_y.value) - 1) and int(density.value) >= 0 and int(density.value) <= 3:
                print(dimension_x.value, dimension_y.value, start_x.value, start_y.value, end_x.value, end_y.value, int(density.value))
                values = (int(dimension_x.value), int(dimension_y.value), int(start_x.value), int(start_y.value), int(end_x.value), int(end_y.value), int(density.value))
                page.window_close()
            else:
                page.banner.open = True
                page.update()
        except Exception as err:
            print(err)
            page.banner.open = True
            page.update()

    def close_banner(e):
        page.banner.open = False
        page.update()

    def slider_change(e):
        if int(density.value) > 4:
            density.active_color = ft.colors.RED_900
            density.inactive_color = ft.colors.RED_400

        elif int(density.value) < 4 and int(density.value) > 2:
            density.active_color = ft.colors.DEEP_ORANGE
            density.inactive_color = ft.colors.DEEP_ORANGE_300

        elif int(density.value) < 3 and int(density.value) > 0:
            density.active_color = ft.colors.LIGHT_BLUE_ACCENT_700
            density.inactive_color = ft.colors.LIGHT_BLUE_ACCENT_100
        
        elif int(density.value) == 0:
            density.active_color = ft.colors.GREEN_ACCENT_700
            density.inactive_color = ft.colors.LIGHT_GREEN_ACCENT_200

        page.update()

    # Χτίσιμο Layout
    page.banner = ft.Banner(
        bgcolor=ft.colors.AMBER_100,
        leading=ft.Icon(ft.icons.WARNING_SHARP, color=ft.colors.AMBER, size=40),
        content=ft.Text(
            f"Παρακαλώ ελέγξτε τις εισόδους σας!"
        ),
        actions=[
            ft.TextButton("Δοκιμή ξανά", on_click=close_banner)
        ],
    )

    logo = ft.Container(
                    content=ft.Image(src=f"logo.png"),
                    margin=3,
                    padding=3,
                    alignment=ft.alignment.center,
                    #height=80
                        )

    dimensions_txt = ft.Container(
                    content=ft.Text(
                    "Διαστάσεις Επιπέδου:",
                    size=22,
                    color=ft.colors.BLACK,
                    bgcolor=ft.colors.WHITE,
                    weight=ft.FontWeight.BOLD
                                    ),
                    margin=0,
                    padding=-1,
                    alignment=ft.alignment.center,
                        )

    dimension_x = ft.TextField(label="Διάσταση Χ", width = 200, hint_text="x>6", input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9]", replacement_string=""), border=ft.InputBorder.UNDERLINE)
    x_txt = ft.Text(
                    "x",
                    size=22,
                    color=ft.colors.BLACK,
                    bgcolor=ft.colors.WHITE,
                    weight=ft.FontWeight.BOLD)
    dimension_y = ft.TextField(label="Διάσταση Y", width = 200, hint_text="x*y>=36", input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9]", replacement_string=""), border=ft.InputBorder.UNDERLINE)
    
    dimensions_input = ft.Row(
            [
                dimension_x,
                x_txt,
                dimension_y,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
                            )
    
    coords_txt = ft.Container(
                    content=ft.Text(
                    "Συντεταγμένες Εκκίνησης/Τερματισμού:",
                    size=22,
                    color=ft.colors.BLACK,
                    bgcolor=ft.colors.WHITE,
                    weight=ft.FontWeight.BOLD
                                    ),
                    margin=3,
                    padding=0,
                    alignment=ft.alignment.center,
                        )

    coords_warntxt = ft.Container(
                    content=ft.Text(
                    "Λάβετε υπ'όψιν ότι το επίπεδο περιβάλλεται από τοίχο πάχους 1 pixel και το όχημα δεν πρέπει να ακουμπά σε αυτόν.",
                    size=14,
                    color=ft.colors.BLACK,
                    bgcolor=ft.colors.WHITE,
                    weight=ft.FontWeight.NORMAL
                                    ),
                    margin=0,
                    padding=0,
                    alignment=ft.alignment.center,
                        )

    start_x = ft.TextField(label="X Εκκίνησης", width=135, input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9]", replacement_string=""), border=ft.InputBorder.UNDERLINE)
    start_y = ft.TextField(label="Υ Εκκίνησης", width=135, input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9]", replacement_string=""), border=ft.InputBorder.UNDERLINE)
    end_x = ft.TextField(label="Χ Τερματισμού", width=135, input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9]", replacement_string=""), border=ft.InputBorder.UNDERLINE)
    end_y = ft.TextField(label="Υ Τερματισμού", width=135, input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9]", replacement_string=""), border=ft.InputBorder.UNDERLINE)

    coords_input = ft.Row(
            [
                start_x,
                start_y,
                end_x,
                end_y
            ],
            alignment=ft.MainAxisAlignment.CENTER,
                            )

    density_txt = ft.Text("Πυκνότητα Εμποδίων:", weight=ft.FontWeight.BOLD, size=18)
    density = ft.Slider(min=0, max=3, divisions=3, label="Πυκνότητα: {value}", on_change=slider_change)
    density_slider = ft.Row(
            [
                density_txt,
                ft.Container(content = density, width = 250, alignment=ft.alignment.center)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
                            )
    
    start_button_style = ft.ButtonStyle({ft.MaterialState.DEFAULT: ft.colors.GREEN, ft.MaterialState.FOCUSED: ft.colors.GREEN_400})
    start_button = ft.FilledButton("Έναρξη Επίλυσης", icon="play_arrow_sharp", on_click=checkparameters)
    start_button_display = ft.Row(
            [
                ft.Container(content = start_button, width = 250, alignment=ft.alignment.center)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
                                )
    

    content = ft.Column(
                        [
                            logo,
                            dimensions_txt,
                            dimensions_input,
                            coords_txt,
                            coords_warntxt,
                            coords_input,
                            density_slider,
                            start_button_display
                        ])
    
    page.add(content)
    page.update()

def openGUI(x):
    ft.app(target=x)

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

def solve(matrix):
    for t in range(len(matrix)):
        inner_list = matrix[t]
        if 'start' in inner_list:
            start_y = t
            start_x = inner_list.index('start')

    for m in range(len(matrix)):
        inner_list = matrix[m]
        if 'end' in inner_list:
            end_y = m
            end_x = inner_list.index('end')

    matrix[start_y][start_x]= 0
    matrix[end_y][end_x]=0
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
        z.remove((current_x,current_y))
        if not ( next_point_x,next_point_y + 1) and (next_point_x ,next_point_y - 1) and (next_point_x + 1,next_point_y ) and (next_point_x - 1,next_point_y ) in z:
            return (next_point_x,next_point_y )
        else:
            return None


    def check_diagonal_blockage(done_moves,current_x=start_x,current_y=start_y):
        diagonal_blockage_points=[]
        if matrix[current_y][current_x + 1]==1 and matrix[current_y + 1][current_x]==1:
            diagonal_blockage_points.append(( current_x + 1 ,current_y + 1))
        if matrix[current_y][current_x + 1]==1 and matrix[current_y - 1][current_x]==1:
            diagonal_blockage_points.append((current_x + 1,current_y - 1 ))
        if matrix[current_y][current_x - 1 ]==1 and matrix[current_y + 1][current_x]==1:
            diagonal_blockage_points.append((current_x - 1,current_y + 1))
        if matrix[current_y][current_x - 1]==1 and matrix[current_y - 1][current_x]==1:
            diagonal_blockage_points.append((current_x - 1,current_y - 1  ))
        return diagonal_blockage_points

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
                    can_do_moves.append(( current_x + i,current_y + p))
        try:
            can_do_moves.remove((current_x,current_y ))
            for a in range (0,4):
                can_do_moves.remove(check_diagonal_blockage(current_x,current_y)[a])
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
        global unsolvable 
        unsolvable = False
        while check_position(current_x,current_y,end_x,end_y)== True and unsolvable == False:
            d_pos_moves= find_path(current_x,current_y)
            if same_distances(d_pos_moves)=={}:
                next_point= list(d_pos_moves.keys())[0]
                if check_blockage( next_point[0],  next_point[1], current_x, current_y) == (next_point[0],  next_point[1]):
                    del d_pos_moves[(next_point[0],  next_point[1])]
                elif check_blockage( next_point[0],  next_point[1], current_x, current_y) == None:
                    current_x =next_point[0]
                    current_y =next_point[1]
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
                if check_blockage( next_point[0],  next_point[1], current_x, current_y) == (next_point[0], next_point[1]):
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

    return move()

openGUI(ginit)
matrix = gen_matrix(*values)

generated_matrix = copy.deepcopy(matrix)
start_time =  time.process_time()
positions = solve(matrix)
solvingtime_ms = (time.process_time() - start_time) * 1000

distance_travelled = calcdist(positions)

plt.imshow(gen_layout(generated_matrix))
print(positions)
plot(positions, solvingtime_ms, distance_travelled, unsolvable)
plt.show()

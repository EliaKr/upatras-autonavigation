import random
from matplotlib import pyplot as plt
import flet as ft

def ginit(page: ft.Page):
    # Βασικές Παράμετροι
    #page.window_width = 600
    #page.window_height = 750
    page.window_resizable = True
    
    page.title = "Initialise Parameters"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Ορισμός Συναρτήσεων
    def checkparameters(e):
        global values
        try:
            if int(dimension_x.value) > 6 and (int(dimension_x.value) * int(dimension_y.value)) >= 36 and int(start_x.value) > 1 and int(start_x.value) < int(dimension_x.value) - 1 and int(start_y.value) > 1 and int(start_y.value) < int(dimension_y.value) - 1 and int(end_x.value) > 1 and int(end_x.value) < (int(dimension_x.value) - 2) and int(end_y.value) > 1 and int(end_y.value) < (int(dimension_y.value) - 2) and int(density.value) >= 0 and int(density.value) <= 6:
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

    # Χτίσιμο generated_matrix
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
                    f"Λάβετε υπ'όψιν ότι το επίπεδο περιβάλλεται από τοίχο πάχους 1 pixel και το όχημα δεν πρέπει να ακουμπά σε αυτόν.",
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
    density = ft.Slider(min=0, max=6, divisions=6, label="Πυκνότητα: {value}", on_change=slider_change)
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
    print("Λιστα δημιουργηθηκε")
    # Δημιουργία πίνακα, όπου 1 σημαίνει πως έχω εμπόδιο
    while True: 
        matrix = []
        for x in range(dimension_x):
            matrix.append([])
            for y in range(dimension_y):
                matrix[x].append(random.choice(elements))
                print("Νέο στοιχείο δημιουργηθηκε")
        print("Τυχαία δημιουργηθηκε")
        # Δημιουργία τοίχων
        for i in range(0,dimension_x): 
            matrix[i][0]=1
            matrix[i][dimension_y - 1]=1
        for i in range(0,dimension_y): 
            matrix[0][i]=1
            matrix[dimension_x - 1][i] = 1
        print("Τοιχοι δημιουργηθηκε")

        #Τοποθέτηση αρχής, τέλους.
        matrix[start_x][start_y] = "start"
        matrix[end_x][end_y] = "end"

        # Έλεγχος εαν αρχικά το όχημα ή ο στόχος βρίσκεται "παγιδευμένο" μέσα σε εμπόδια σε ακτίνα ενός pixel
        results = []
        for i in range(-1,2):
            for z in range(-1,2):
                if matrix[start_x + i][start_y + z] != 1: 
                    results.append(0)
                else: 
                    results.append(1)
                if matrix[end_x + i][end_y + z] != 1: 
                    results.append(0)
                else: 
                    results.append(1)
        if sum(results) == 0:
            break
    
    return matrix

def a_star(matrix, start, end):
    start_x = start[0]
    start_y = start[1]
    end_x = end[0]
    end_y = end[1]
    distance_travelled = 0
    generated_matrix = matrix.copy()
    path = []
    # Reference: https://www.geeksforgeeks.org/a-search-algorithm/
    # Reference: https://stackoverflow.com/questions/45577114/a-star-algorithm-open-and-closed-lists
    # Reference: https://stackabuse.com/courses/graphs-in-python-theory-and-implementation/lessons/a-star-search-algorithm/
    # Αρχικά μετασχηματίζουμε τον πίνακα με τις θέσεις που δεν έχουν εμπόδια να αναπαρίστανται με τις συντεταγμένες τους και τις θέσεις που έχουν να παραμένουν 1.
    for x in generated_matrix:
        for y in x:
            if y == 0: 
                generated_matrix[generated_matrix.index(x)][generated_matrix[generated_matrix.index(x)].index(y)] = (generated_matrix.index(x), generated_matrix[generated_matrix.index(x)].index(y))
            elif y == "start": 
                generated_matrix[generated_matrix.index(x)][generated_matrix[generated_matrix.index(x)].index(y)] = (generated_matrix.index(x), generated_matrix[generated_matrix.index(x)].index(y))
            elif y == "end": 
                generated_matrix[generated_matrix.index(x)][generated_matrix[generated_matrix.index(x)].index(y)] = (generated_matrix.index(x), generated_matrix[generated_matrix.index(x)].index(y))


    # Ορίζουμε ως f το άθροισμα των g,h όπου g το κόστος της κίνησης από το σημείο start έως ένα σημείο Α στο επίπεδο και h το εκτιμώμενο κόστος κίνησης από το
    # σημείο Α έως το τέλος της διαδρομής. Το h ονομάζεται heuristic και είναι εκτίμηση και όχι η βέβαιη τιμή. Σε κάθε βήμα επιλέγουμε να επεξεργαστούμε το σημείο
    # που έχει το μικρότερο f=g+h.

    # Αρχικοποιούμε τη λίστα open που θα περιέχει όσα στοιχεία έχουμε περάσει αλλά δεν έχουν ελεγχθεί πλήρως
    q = start
    open_l = set([q])
    # Αρχικοποιούμε τη λίστα closed που θα περιέχει όσα στοιχεία έχουμε περάσει και έχουν ελεγχθεί πλήρως
    closed_l = set([])

    while open_l != []:
        # Βρίσκουμε το σημείο με το λιγότερο f στη λίστα. Έστω q. Για να το κάνουμε αυτό θα χρειαστούμε μία μεταβλητή που να βρίσκει το g και μία το h.
        # Επίσης χρησιμοποιούμε την απόσταση που έχει διανυθεί έως εκείνη τη στιγμή. Επιλέγουμε η κίνησή μας να γίνεται μόνο πάνω, κάτω, αριστερά, δεξιά και όχι διαγώνια.
        # Επειδή η κίνηση γίνεται μόνο σε αυτές τις κατευθύνσεις έχουμε σταθερά g = ήδη_διανυθείσα_απόσταση + 1.
        f_positions = {}
        for i in open_l:
            g = distance_travelled + 1
            # Υπολογισμός του h (Απόσταση Manhattan)
            h = abs(i[0] - end_x) + abs(i[1] - end_y)
            #Υπολογισμός του f
            f = g + h
            f_positions.update({f: i})
        # Εύρεση θέσης με μικρότερο f
        q = sorted(f_positions.items())[0][1]
        #print(f_positions, min_f_pos)
        open_l.pop(q)

        q_succesors = []
        for l in range(-1, 2):
            for z in range(-1, 2):
                for e in generated_matrix:
                    if (q[0] + l, q[1] + z) in e:
                        q_succesors.append((q[0] + l, q[1] + z))
        
        # Αντιστροφή keys,values στο f_positions
        posq_f = {v: k for k, v in f_positions.items()}
        # Section (d)
        for i in q_succesors:
            #   Υπολογισμός f για το κάθε successor
                i_g = distance_travelled + 1
                # Υπολογισμός του h (Απόσταση Manhattan)
                i_h = abs(i[0] - end_x) + abs(i[1] - end_y)
                i_f = i_g + i_h
                q_succesors_f_pos.append((i_f, i))
            if i == end:
                open_l = []
                break
            elif i[1] in open_l and posq_f[i] < i_f:
                pass
            elif i[1] in closed_l and posq_f[i] < i_f:
                pass
            else:
                # O Kodikas xreiazetai epektasi meta apo afto to simeio.



openGUI(ginit)

start_pos = (values[2], values[3])
end_pos = (values[4], values[5])

random_matrix = gen_matrix(*values)
best = a_star(random_matrix, start_pos, end_pos)
print(best)
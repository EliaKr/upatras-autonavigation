from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
import flet as ft
import random
from matplotlib import pyplot as plt
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
            if int(dimension_x.value) > 6 and (int(dimension_x.value) * int(dimension_y.value)) >= 36 and int(start_x.value) > 1 and int(start_x.value) < int(dimension_x.value) and int(start_y.value) > 1 and int(start_y.value) < int(dimension_y.value) and int(end_x.value) > 1 and int(end_x.value) < (int(dimension_x.value) - 1) and int(end_y.value) > 1 and int(end_y.value) < (int(dimension_y.value) - 1) and int(density.value) >= 0 and int(density.value) <= 6:
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

def gen_matrix_inverted(dimension_x, dimension_y, start_x, start_y, end_x, end_y, density):
    # Δημιουργία λίστας ανάλογα με το density των εμποδίων
    elements = []
    for i in range(10):
        elements.append(1)
    for i in range(density):
        elements[i] = 0
    # Δημιουργία πίνακα, όπου 0 σημαίνει πως έχω εμπόδιο
    q = 1
    while True:
        print(f"Πίνακας {q}")
        q += 1
        matrix = []
        for y in range(dimension_y):
            matrix.append([])
            for x in range(dimension_x):
                matrix[y].append(random.choice(elements))
        # Δημιουργία τοίχων
        for i in range(0,dimension_y): 
            matrix[i][0]=0
            matrix[i][dimension_x - 1]=0
        for i in range(0,dimension_x): 
            matrix[0][i]=0
            matrix[dimension_y - 1][i]=0

        #Τοποθέτηση αρχής, τέλους.
        matrix[start_y][start_x] = 1.02
        matrix[end_y][end_x] = 1.01

        break
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
                    results.append(0)
        if sum(results) == 0:
            break
    
    return matrix

def gen_layout_inverted(x):
    layout = x.copy()

    for x in layout:
        for y in x:
            if y == 1: 
                layout[layout.index(x)][layout[layout.index(x)].index(y)] = [255, 255, 255]
            elif y == 0: 
                layout[layout.index(x)][layout[layout.index(x)].index(y)] = [0, 0, 0]
            elif y == 1.02: 
                layout[layout.index(x)][layout[layout.index(x)].index(y)] = [0, 255, 0]
            elif y == 1.01: 
                layout[layout.index(x)][layout[layout.index(x)].index(y)] = [255, 0, 0]
    
    return layout

def plot(positions, solvingtime = "Unknown", distance_travelled = "Unknown"):
    x = []
    y = []
    for i in positions:
        x.append(i[0])
        y.append(i[1])
    
    plt.xlabel(f"Solving Time: {solvingtime}ms, Distance Travelled: {distance_travelled}")
    plt.plot(x, y, "b-", linewidth=8.0)
    
def poslist(path, end):
    positions = []
    for i in path:
        positions.append(tuple(i))
    positions.append(end)

    return positions

# Γραφική Έναρξη και Καταχώρηση Μεταβλητών
openGUI(ginit)
matrix = gen_matrix_inverted(*values)

# Αρχικοποίηση μεταβλητών για βιβλιοθήκη Pathfinding
grid = Grid(matrix=matrix)
start = grid.node(values[2], values[3])
end = grid.node(values[4], values[5])

# Δημιουργία αντικειμένου finder για χρήση με βιβλιοθήκη Pathfinding και προσδιορισμός χρήσης βιβλιοθήκης A*
finder = AStarFinder(diagonal_movement=DiagonalMovement.never)

# Εύρεση διαδρομής με χρήση αλγορίθμου Α*
path, runs = finder.find_path(start, end, grid)

# Δημιουργία λίστας με τις θέσεις που πέρασε το όχημα με χρήση της συνάρτησης poslist()
end_pos = (values[4], values[5])
positions = poslist(path, end_pos)

# Προβολή διαδρομής
plt.imshow(gen_layout_inverted(matrix))
print(positions)
plot(positions)
plt.show()
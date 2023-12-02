# Reference: https://llego.dev/posts/implementing-the-a-search-algorithm-python/ (MIT License)
import random
from matplotlib import pyplot as plt
import flet as ft
import numpy as np

class AStar:

    def __init__(self, map_grid):
        self.open = [] #open list
        self.closed = [] #closed list
        self.map_grid = map_grid

    def search(self, start_node, goal_node):

        self.open.append(start_node)

        while self.open:

            #sort open list to get node with lowest cost first
            self.open.sort()
            current_node = self.open.pop(0)

            #add current node to closed list
            self.closed.append(current_node)

            if current_node == goal_node:
                #reached goal node
                return self.reconstruct_path(goal_node)

            #check every neighbor
            neighbors = self.get_neighbors(current_node)

            for neighbor in neighbors:
                if neighbor in self.closed:
                    continue

                g_cost = current_node.g_cost + 1 #cost to move
                h_cost = self.heuristic(neighbor, goal_node)
                f_cost = g_cost + h_cost

                #check if we found cheaper path
                if neighbor in self.open:
                    if neighbor.f_cost > f_cost:
                        self.update_node(neighbor, g_cost, h_cost)
                else:
                    self.update_node(neighbor, g_cost, h_cost)

        #no path found
        return None

    def get_neighbors(self, node):
        pass #calculate valid adjacent nodes

    def heuristic(self, node, goal):
        pass #estimate cost to goal

    def reconstruct_path(self, goal_node):
        pass #follow parents back to start

    def update_node(self, node, g_cost, h_cost):
        pass  #update if we find better path
    
    def get_neighbors(self, node):
        dirs = [[1,0], [0,1], [-1,0], [0,-1]]
        neighbors = []

        for dir in dirs:
            neighbor_pos = (node.pos[0] + dir[0], node.pos[1] + dir[1])

            #check if new pos in bounds
            if (0 <= neighbor_pos[0] < self.map_grid.shape[0] and
                0 <= neighbor_pos[1] < self.map_grid.shape[1]):

                #check if traversable
                if self.map_grid[neighbor_pos] != 1:
                    neighbors.append(neighbor_pos)

        return neighbors
    
    def heuristic(self, node, goal):
        d = abs(node.pos[0] - goal.pos[0]) + abs(node.pos[1] - goal.pos[1])
        return d

    def reconstruct_path(self, goal_node):
        path = [goal_node]
        current = goal_node

        while current.parent != start_node:
            path.append(current.parent)
            current = current.parent

        return path[::-1]  #reverse path
        
    def update_node(self, node, g_cost, h_cost):
        node.g_cost = g_cost
        node.h_cost = h_cost
        node.f_cost = g_cost + h_cost
        node.parent = current_node

def ginit(page: ft.Page):
    # Βασικές Παράμετροι
    #page.window_width = 600
    #page.window_height = 750
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
    density = ft.Slider(min=1, max=6, divisions=5, label="Πυκνότητα: {value}", on_change=slider_change)
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

openGUI(ginit)
matrix = np.array(gen_matrix(*values))

start_pos = (values[2], values[3])
end_pos = (values[4], values[5])

start = Node(start_pos)
goal = Node(end_pos)

astar = AStar(matrix)
path = astar.search(start, goal)
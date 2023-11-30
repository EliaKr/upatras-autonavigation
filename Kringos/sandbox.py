import random
from matplotlib import pyplot as plt

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
            if start_x > 1 and start_x < dimension_x and start_y > 1 and start_y < dimension_y: 
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
            density = int(input("Παρακαλώ εισάγετε την πυκνότητα των εμποδίων σε βαθμό 0-6 (Συνίσταται <4):"))
            if density >= 0 and density <= 6: 
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
        for x in range(dimension_x):
            matrix.append([])
            for y in range(dimension_y):
                matrix[x].append(random.choice(elements))
        # Δημιουργία τοίχων
        for i in range(0,dimension_x): 
            matrix[i][0]=1
            matrix[i][dimension_y - 1]=1
        for i in range(0,dimension_y): 
            matrix[0][i]=1
            matrix[dimension_x - 1][i]=1

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

matrix = gen_matrix(*initialise())

plt.imshow(gen_layout(matrix))
plt.show()

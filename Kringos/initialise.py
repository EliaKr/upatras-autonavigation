def initialise():
    while True:
        global dimension_x
        try:
            dimension_x = int(input("Παρακαλώ εισάγετε την διάσταση της πίστας στον άξονα των x, λαμβάνοντας υπ'όψιν ότι η πίστα περιβάλλεται από τοίχο πάχους 1 pixel. (x>4):"))
            if dimension_x > 4: break
            else: print("Προσπαθήστε Ξανά.")
        except:
            print("Προσπαθήστε Ξανά.")
    
    while True:
        global dimension_y
        try:
            dimension_y = int(input("Παρακαλώ εισάγετε την διάσταση της πίστας στον άξονα των y, λαμβάνοντας υπ'όψιν ότι η πίστα περιβάλλεται από τοίχο πάχους 1 pixel. (x*y>24):"))
            if dimension_x * dimension_y > 24: break
            else: print("Προσπαθήστε Ξανά.")
        except:
            print("Προσπαθήστε Ξανά.")

    while True:
        global start_x
        global start_y
        try:
            start_coords = tuple(input("Παρακαλώ εισάγετε τις συντεταγμένες όπου θα ξεκινήσει το όχημα σε μορφή (x,y), λαμβάνοντας υπ'όψιν ότι η πίστα περιβάλλεται από τοίχο πάχους 1 pixel."))
            start_x = int(start_coords[0])
            start_y = int(start_coords[1])
            if start_x > 0 and start_x < dimension_x and start_y > 0 and start_y < dimension_y: break
            else: print("Προσπαθήστε Ξανά.")
        except:
            print("Προσπαθήστε Ξανά.")

    while True:
        global end_x
        global end_y
        try:
            end_coords = tuple(input("Παρακαλώ εισάγετε τις συντεταγμένες όπου θέλετε να τερματίσει το όχημα σε μορφή (x,y), λαμβάνοντας υπ'όψιν ότι η πίστα περιβάλλεται από τοίχο πάχους 1 pixel."))
            end_x = int(end_coords[0])
            end_y = int(end_coords[1])
            if end_x > 0 and end_x < dimension_x and end_y > 0 and end_y < dimension_y: break
            else: print("Προσπαθήστε Ξανά.")
        except:
            print("Προσπαθήστε Ξανά.")
    
    while True:
        global density
        try:
            density = int(input("Παρακαλώ εισάγετε την πυκνότητα των εμποδίων σε βαθμό 0-99:"))
            if density >= 0 and density <= 99: break
            else: print("Προσπαθήστε Ξανά.")
        except:
            print("Προσπαθήστε Ξανά.")
    
initialise()
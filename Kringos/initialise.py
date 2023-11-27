def initialise():
    while True:
        try:
            dimension_x = int(input("Παρακαλώ εισάγετε την διάσταση της πίστας στον άξονα των x, λαμβάνοντας υπ'όψιν ότι η πίστα περιβάλλεται από τοίχο πάχους 1 pixel. (x>6):"))
            if dimension_x > 6: break
            else: print("Προσπαθήστε Ξανά.")
        except:
            print("Προσπαθήστε Ξανά.")
    
    while True:
        try:
            dimension_y = int(input("Παρακαλώ εισάγετε την διάσταση της πίστας στον άξονα των y, λαμβάνοντας υπ'όψιν ότι η πίστα περιβάλλεται από τοίχο πάχους 1 pixel. (x*y>=36):"))
            if dimension_x * dimension_y >= 36: break
            else: print("Προσπαθήστε Ξανά.")
        except:
            print("Προσπαθήστε Ξανά.")

    while True:
        try:
            start_coords = input("Παρακαλώ εισάγετε τις συντεταγμένες όπου θα ξεκινήσει το όχημα σε μορφή (x,y), λαμβάνοντας υπ'όψιν ότι η πίστα περιβάλλεται από τοίχο πάχους 1 pixel.:")
            coord_list = start_coords.split(",")
            start_x = int(coord_list[0])
            start_y = int(coord_list[1])
            if start_x > 0 and start_x < dimension_x and start_y > 0 and start_y < dimension_y: break
            else: print("Προσπαθήστε Ξανά.")
        except:
            print("Προσπαθήστε Ξανά.")

    while True:
        try:
            end_coords = input("Παρακαλώ εισάγετε τις συντεταγμένες όπου θέλετε να τερματίσει το όχημα σε μορφή (x,y), λαμβάνοντας υπ'όψιν ότι η πίστα περιβάλλεται από τοίχο πάχους 1 pixel.:")
            coord_list = end_coords.split(",")
            end_x = int(coord_list[0])
            end_y = int(coord_list[1])
            if end_x > 1 and end_x < (dimension_x - 1) and end_y > 1 and end_y < (dimension_y - 1): break
            else: print("Προσπαθήστε Ξανά.")
        except:
            print("Προσπαθήστε Ξανά.")
    
    while True:
        try:
            density = int(input("Παρακαλώ εισάγετε την πυκνότητα των εμποδίων σε βαθμό 0-6 (Συνίσταται <4):"))
            if density >= 0 and density <= 6: break
            else: print("Προσπαθήστε Ξανά.")
        except:
            print("Προσπαθήστε Ξανά.")
    
    return dimension_x, dimension_y, start_x, start_y, end_x, end_y, density
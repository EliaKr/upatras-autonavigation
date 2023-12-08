""" 
Η συγκεκριμένη συνάρτηση δημιουργεί ένα πίνακα διαστάσης x*y με βάση τις τιμές που ορίστηκαν από τον χρήστη με την εκτέλεση του προγράμματος και τη συνάρτηση initialise().
Ο πίνακας είναι της μορφής matrix = [[c1,c2,c3], [c1,c2,c3], [c1,c2,c3]] και οι τιμές του σε κάθε σημείο του 
μπορούν να προσπελαστούν με βάση τις συντεταγμένες του με χρήση της έκφρασης matrix[y][x]

* Σημείωση: Τα c1,c2,c3 είναι οι στήλες(columns) που αντιστοιχούν σε κάθε x
"""
# Ο κώδικας για το κυρίως πρόγραμμα αρχίζει από εδώ

import random

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

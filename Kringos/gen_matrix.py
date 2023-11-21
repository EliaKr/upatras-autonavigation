""" 
Η συγκεκριμένη συνάρτηση δημιουργεί ένα πίνακα διαστάσης x*y με βάση τις τιμές που ορίστηκαν από τον χρήστη με την εκτέλεση του προγράμματος και τη συνάρτηση initialise().
Ο πίνακας είναι της μορφής matrix = [[r1,r2,r3], [r1,r2,r3], [r1,r2,r3]] και οι τιμές του σε κάθε σημείο του 
μπορούν να προσπελαστούν με βάση τις συντεταγμένες του με χρήση της έκφρασης matrix[x][y]

* Σημείωση: Τα r1,r2,r3 είναι οι γραμμές(rows) που αντιστοιχούν σε κάθε y
"""

# Οι μεταβλητές είναι για σκοπούς δοκιμής. Στον κανονικό κώδικα θα παράγονται απο την initialise().
dimension_x = 4
dimension_y = 6
density = 3
start_x = 2
start_y = 3
# Ο κώδικας για το κυρίως πρόγραμμα αρχίζει από εδώ

import random

def gen_matrix():
    # Δημιουργία λίστας ανάλογα με το density των εμποδίων
    elements = []
    for i in range(10):
        elements.append(0)
    for i in range(density):
        elements[i] = 1

    print(elements)

    # Δημιουργία πίνακα, όπου 1 σημαίνει πως έχω εμπόδιο
    while True: 
        matrix = []
        for x in range(dimension_x):
            matrix.append([])
            for y in range(dimension_y):
                matrix[x].append(random.choice(elements))
        # Δημιουργία τοίχων
        for i in range(0,dimension_x): matrix[i][0]=1; matrix[i][dimension_y - 1]=1
        for i in range(0,dimension_y): matrix[0][i]=1; matrix[dimension_x - 1][i]=1

        # Έλεγχος εαν αρχικά το όχημα βρίσκεται "παγιδευμένο" μέσα σε εμπόδια
        results = []
        for i in range(-1,1):
            for z in range(-1,1):
                if matrix[start_x + i][start_y + z] != 1: results.append(0)
                else: results.append(1)
        if sum(results) == 0:
            break
    
    return matrix

gen_matrix()
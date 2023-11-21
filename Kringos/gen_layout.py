# Δημιουργία της εικόνας της πίστας σε αρχείο gif με βάση τον πίνακα που παράχθηκε στην συνάρτηση gen_matrix().

# Οι μεταβλητές είναι για σκοπούς δοκιμής. Στον κανονικό κώδικα θα παράγονται απο την initialise().
matrix = [[1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 1, 1, 1], [1, 1, 1, 0, 1, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1]]
start_x = 2
start_y = 3
end_x = 3
end_y = 5
dimension_x = 4
dimension_y = 6
# Ο κώδικας για το κυρίως πρόγραμμα αρχίζει από εδώ. Τα χρώματα ορίζονται με τις τιμές RGB = [R, G, B]

from matplotlib import pyplot

def gen_layout():
    layout = matrix.copy()

    #Καθορισμός χρώματος των θέσεων έναρξης/τερματισμού (πράσινο,κόκκινο αντίστοιχα)
    layout[start_x][start_y] = [0, 255, 0]
    layout[end_x][end_y] = [255, 0, 0]

    for x in layout:
        for y in x:
            if y == 0: layout[layout.index(x)][layout[layout.index(x)].index(y)] = [255, 255, 255]
            elif y == 1: layout[layout.index(x)][layout[layout.index(x)].index(y)] = [0, 0, 0]
    
    return layout

pyplot.imshow(gen_layout())
#print(gen_layout())
# Δημιουργία της εικόνας της πίστας σε αρχείο gif με βάση τον πίνακα που παράχθηκε στην συνάρτηση gen_matrix().

# Οι μεταβλητές είναι για σκοπούς δοκιμής. Στον κανονικό κώδικα θα παράγονται απο την initialise().
import time
matrix = [[1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 1, 1, 1], [1, 1, 1, 0, 1, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1]]
start_x = 2
start_y = 3
end_x = 3
end_y = 5
dimension_x = 4
dimension_y = 6
# Ο κώδικας για το κυρίως πρόγραμμα αρχίζει από εδώ. Τα χρώματα ορίζονται με τις τιμές RGB = [R, G, B]
# Κατεβάστε την βιβλιοθήκη Array2GIF από εδώ: https://pypi.org/project/array2gif/. Χρήση εντολής πχ. write_gif(array, "filename.gif")

from matplotlib import pyplot as plt

def gen_layout(x):
    layout = x.copy()

    for x in layout:
        for y in x:
            if y == 0: layout[layout.index(x)][layout[layout.index(x)].index(y)] = [255, 255, 255]
            elif y == 1: layout[layout.index(x)][layout[layout.index(x)].index(y)] = [0, 0, 0]
            elif y == "start": layout[layout.index(x)][layout[layout.index(x)].index(y)] = [0, 255, 0]
            elif y == "end": layout[layout.index(x)][layout[layout.index(x)].index(y)] = [255, 0, 0]
    
    return layout

gen_layout(matrix)
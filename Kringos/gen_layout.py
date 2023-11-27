# Δημιουργία της εικόνας της πίστας με βάση τον πίνακα που παράχθηκε στην συνάρτηση gen_matrix().
# Ο κώδικας για το κυρίως πρόγραμμα αρχίζει από εδώ. Τα χρώματα ορίζονται με τις τιμές RGB = [R, G, B]

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

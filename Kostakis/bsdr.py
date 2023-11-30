
def bsdr():
    res = {6: [(1, 2), (5, 9)], 5: [(2, 3), (7, 6)]} #same_distances(find_path())
    sorted_res = dict(sorted(res.items()))
    sd_pos=list(sorted_res.values())[0]
    f_p = sd_pos[0]
    s_p = sd_pos[1]
    f_d = find_path(f_p[0],f_p[1])
    s_d = find_path(s_p[0],s_p[1])
    
    if same_distances(find_path(f_p[0],f_p[1]))==same_distances(find_path(s_p[0],s_p[1]))=={}:
        if list(f_d.values())[0] < list(s_d.values())[0]:
            return s_p #Κανουμε return s_p διοτι εν συνεχεια θελουμε να διαγραφει απο το dictionary της find_path αφου το f_p αποτελει καταλληλοτερη επιλογη
        elif list(f_d.values())[0] > list(s_d.values())[0]:
            return f_p
    else: 
        print('ισες και δευτερες αποστασεις επιστρεφω s_p')
        return s_p #να επιδιορθωθει



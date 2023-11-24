find_path.py

matrix = [[1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 1, 1, 1], [1, 1, 1, 0, 1, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1]]
start_x = 2
start_y = 3
end_x = 3
end_y = 5
dimension_x = 4
dimension_y = 6

def find_path():
    current_x = start_x
    current_y = start_y
    for i in range (-1,2):
        for p in range(-1,2):
            distance = (((end_x - (current_x  + i))**2 + (end_y - (current_y + p))**2)**0.5)
            d = {}
            d.update({(current_x  + i, current_y + p): distance})
            

            



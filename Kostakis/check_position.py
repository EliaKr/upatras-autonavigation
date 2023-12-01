def check_position(current_x,current_y,end_x,end_y):
    if current_x!=end_x or current_y!=end_y:
        return True
    elif current_x==end_x and current_y==end_y:
        return False 

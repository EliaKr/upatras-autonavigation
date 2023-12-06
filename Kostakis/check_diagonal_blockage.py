def check_diagonal_blockage(done_moves,current_x=start_x,current_y=start_y):
    if matrix[current_x + 1][current_y]==1 and matrix[current_x][current_y + 1]==1:
        return (current_x + 1 , current_y + 1)
    if matrix[current_x + 1][current_y]==1 and matrix[current_x][current_y - 1]==1:
        return (current_x + 1, current_y - 1)
    if matrix[current_x - 1 ][current_y]==1 and matrix[current_x][current_y + 1]==1:
        return (current_x - 1,current_y + 1)
    if matrix[current_x - 1][current_y]==1 and matrix[current_x][current_y - 1]:
        return (current_x - 1 , current_y - 1)



import datetime
def savefile(matrix):
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H-%M-%S") 
    with open(f"matrix_{formatted_datetime}.txt", 'w', encoding = 'utf-8' ) as f:
        f.write(str(matrix))
    print (f.name)

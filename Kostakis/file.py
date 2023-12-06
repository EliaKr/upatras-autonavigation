import datetime
def file(matrix):
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H-%M-%S") 
    f = open(f"my_file_{formatted_datetime}.txt", 'a', encoding = 'utf-8' )
    f.write(str(matrix))
    f.close
    print (f.name)



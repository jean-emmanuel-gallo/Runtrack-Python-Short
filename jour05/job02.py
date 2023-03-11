def draw_rectangle(width, height):

    print("+{}+".format("-" * (width-4)))
    

    for i in range(height-4):
        print("|{}|".format(" " * (width-4)))
        

    print("+{}+".format("-" * (width-4)))


draw_rectangle(10, 6)
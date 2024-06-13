#takes in x and y coordinates, and returns the indicies for that point
def coords_to_ind(x,y):
    return (x-1+8*(y-1))

#takes in indicies for board state and returns coordinates
def ind_to_coords(ind):
    return((ind%8)+1, (ind//8)+1)

#converts chess piece coordinates to pixel coordinates on page
def coords_to_pygame_coords(x,y):
    return(30+x*80, 30+y*80)

#converts pixel coordinate on page to chess coordinates
def pygame_coords_to_coords(x,y):
    return((x+50)//80, (y+50)//80)


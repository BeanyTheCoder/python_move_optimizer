def move(*directions):
    x = 0
    y = 0
    
    # vector coordinates for each cardinal direction
    ref = {
        "NORTH": (0, 1),
        "SOUTH": (0, -1),
        "EAST": (1, 0),
        "WEST": (-1, 0)
    }
    
    # iterate and sum up x and y values
    for i in directions:
        x += ref[i][0]
        y += ref[i][1]
        
    # translate each x and y value to appropriate direction(eg: x = -1 and y = 2, would be ["WEST", "NORTH", "NORTH"])    
    return (
        ["NORTH"] * y +
        ["SOUTH"] * -y +
        ["EAST"] * x +
        ["WEST"] * -x 
    )
        
# test
print(move("NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST", "EAST", "EAST", "NORTH", "WEST"))
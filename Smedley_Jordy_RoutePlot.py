# Step 1: Read the route instruction files 

def read_file(filename): 
    with open(filename, 'r') as file: 
        instructions = file.read().splitlines() 
    return instructions 

# Step 2: Plot the route on a 12x12 grid 

def plot_route(route): 
    grid = [[' ' for _ in range(12)] for _ in range(12)] 
    x, y = 0, 0 
    for direction in route: 
        if direction == 'UP': 
            y -= 1 
        elif direction == 'DOWN': 
            y += 1 
        elif direction == 'LEFT': 
            x -= 1 
        elif direction == 'RIGHT': 
            x += 1 
        if x < 0 or x >= 12 or y < 0 or y >= 12: 
            print("Route is outside the grid!") 
            return 
        grid[y][x] = 'X'   
    for row in grid: 
        print(' '.join(row)) 
      
# Step 3: Print the coordinates of the route 

def print_coordinates(route): 
    x, y = 0, 0 
    coordinates = [] 
    for direction in route: 
        coordinates.append((x, y)) 
        if direction == 'UP': 
            y -= 1 
        elif direction == 'DOWN': 
            y += 1 
        elif direction == 'LEFT': 
            x -= 1 
        elif direction == 'RIGHT': 
            x += 1 
    print("Coordinates of the route:", coordinates) 

# Step 4: Ask for the next route or stop 

while True: 
    filename = input("Enter the filename of the route instruction file (or 'STOP' to finish): ") 
    if filename == 'STOP': 
        break 
    route = read_file(filename) 
    plot_route(route) 
    print_coordinates(route) 

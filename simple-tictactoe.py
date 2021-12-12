# Project available at https://hyperskill.org/projects/73

def print_board():
    print("---------")
    print(f'| {cells[0]} {cells[1]} {cells[2]} |')
    print(f'| {cells[3]} {cells[4]} {cells[5]} |')
    print(f'| {cells[6]} {cells[7]} {cells[8]} |')
    print("---------")
    
def check_wins(cells):
    # def horizontal_check(cells):
    global wins
    wins = []
    horizontal_step = 3
    for cell in range(0, len(cells), horizontal_step):
        cell_sublist = []
        cell_sublist = cells[cell:cell+3]
        wins.append(cell_sublist)

    # def vertical_check(cells):
    vertical_step = 3
    for start in range(3):
        cell_sublist = []
        for cell in range(start, len(cells), vertical_step):
            cell_sublist.append(cells[cell])
        wins.append(cell_sublist)

    # def backward_check(cells):
    diagonal_step = 4
    backward_diagonal = []
    for cell in range(0, len(cells), diagonal_step):
        backward_diagonal.append(cells[cell])
    wins.append(backward_diagonal)

    # def forward_check(cells):
    diagonal_step = 2
    forward_diagonal = []
    for cell in range(2, len(cells)-2, diagonal_step):
        forward_diagonal.append(cells[cell])
    wins.append(forward_diagonal)    
    return wins

def status_check(wins):
    global status
    global status_count
    status = ""
    status_count = 0

    for win in wins:
        if len(win) == 3 and type(win) == list:
            if win == ['X','X','X']:
                status = "X wins"
                status_count += 1
            elif win == ['O','O','O']:
                status = "O wins"
                status_count += 1
    
    return status, status_count

def user_input():
    global cells
    global user_index
    global X_turn
    try:    
        x, y = [int(coord.strip()) for coord in input("Enter the coordinates: ").split()] # user input x and y coordinates as integers
        user_coord = (x, y)  # convert user coordinates to a Tuple
        
        if not (0 <= x <= 3) or not (0 <= y <= 3):
            print("Coordinates should be from 1 to 3!")
            user_input()
        else:
            coordinates = []
            for row in range(1,4):
                for column in range(1,4):
                    coordinates.append((row,column))
                        
            user_index = coordinates.index(user_coord)
            
            for index, move in enumerate(cells):

                if cells[user_index] == ' ':
                    switch_player()
                    print_board()
                    check_wins(cells)  # Run check_wins to append each (row x 3)/(column x 3)/(diagonal x 2) to a list
                    status_check(wins)  # Run status_check to count number of wins and save status in variable 'status'
                    break
                elif user_index == index:
                    print('This cell is occupied! Choose another one!')

    except ValueError:
        print('You should enter numbers!')
        user_input()
      
def switch_player():
    global turn
    
    if turn % 2 != 0:
        cells[user_index] = 'X'
        turn += 1
    else:
        cells[user_index] = 'O'
        turn += 1
        
#### Execute the game####
if __name__ == "__main__":
    # Print an empty board by storing each position in the 'cells' variable as 9 empty spaces
    input_cells = list('_________')
    cells = [' ' if cell == '_' else cell for cell in input_cells]

    # Print the 9x9 empty board
    print_board()

    # Start the game by running the While Loop
    # # Run the logical sequence of game states in the following order:
    turn = 1  
    status = None
    while True: 
        if status == "X wins" or status == "O wins":
            check_wins(cells)
            status_check(wins)
            print(status)
            break
        elif abs(cells.count('X') - cells.count('O')) == 1 and cells.count(' ') == 0:
            print("Draw")
            break
        else:
            user_input()







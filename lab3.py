import math
def new_board(): 
    board = {}
    return board 

def is_free(board, x, y):
    if (x, y) in board.keys(): 
        return False
    else:
        return True 

def place_piece(board, x, y, player):    
    if is_free(board, x, y) == True:            
        board[(x, y)] = player           
        return True
    else:
        return False

def get_piece(board, x, y):                 
    if (x, y) in board:
        return board[(x, y)]
    else:
        return False

def remove_piece(board, x, y): 
    if (x, y) in board:                
        del board[(x, y)]               
        return True
    else:
        return False

def move_piece(board, x1, y1, x2, y2):      
    player = get_piece(board, x1, y1)
    if player == False:
        return False
    else:
        remove_piece(board, x1, y1)
        return place_piece(board, x2, y2, player)

def count(board, axis, rowcol, player):
    if axis not in ["column", "row"]:
        raise ValueError("invalid")
    
    count = 0

    if axis == "column":
        for cord, piece in board.items():
            if cord[0] == rowcol and piece == player:
                count += 1
    elif axis == "row":
        for cord, piece in board.items():
            if cord[1] == rowcol and piece == player:
                count += 1
    return count

def nearest_piece(board, x, y):

    nearest_distance = float('inf')
    nearest_cord = None

    for (bx, by) in board.keys(): 

        if (bx, by) == (x, y):
            nearest_cord = (x, y)
        elif x != bx or y != by:
            dx = x - bx
            dy = y - by
            hyp = math.sqrt((dx ** 2) + (dy ** 2))
            if hyp < nearest_distance:      
                nearest_distance = hyp
                nearest_cord = (bx, by)
    if nearest_cord == None:
        return False
    return nearest_cord

board = new_board()



def factorial(n, k):
    if k > n or k < 0:
        raise ValueError("k can't be greater than n or less than 0")
    elif k == 0: 
        return 1 
    else:
        return n * factorial(n - 1, k - 1)
    
def numerator(k):
    if k == 0:
        return 1
    else:
        return k * numerator(k - 1)
    

def choose(n, k):
    if k == n or k == 0:
        res = 1
    elif k > n - k:
        res =  factorial(n, n - k) // numerator(n - k) 
    else:
        res = factorial(n, k) // numerator(k)
    return res

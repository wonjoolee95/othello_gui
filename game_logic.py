
# _author = Won Joo Lee

class FullBoardError(Exception):
    '''
    an error for when the board is completely full
    '''
    pass

class InvalidMoveError(Exception):
    '''
    an error for when the move is invalid
    '''
    pass

class NoMoreValidMoveLeft(Exception):
    '''
    an error for when the current player does not have any more valid move left;
    note that this is NOT ONLY when the board is full, since a player
    may NOT have any valid move left despite the board still having empty spots
    '''
    pass


class Othello:
    '''
    the main Othello class, which contains all the functions required
    to run the game
    '''
    def __init__(self, game_settings: list): 
        self._rows = int(game_settings[0])
        self._columns = int(game_settings[1])
        self._turn = game_settings[2][0]
        self._upper = game_settings[3][0]
        self._win_type = game_settings[4]
        self._board = []
        self._black_score = 0
        self._white_score = 0

    def create_board(self) -> None:
        ''' creates the game board using given number of rows and columns '''
    
        for row in range(self._rows):
            self._board.append([])
            for column in range(self._columns):
                self._board[row].append('.')
        self._set_starting_pieces()
                
    def _set_starting_pieces(self) -> None:
        ''' sets the starting upper pieces on the board '''
        if self._upper == 'B':
            given_color = 'B'
            other_color = 'W'
        else:
            given_color = 'W'
            other_color = 'B'
        upper_pieces = (int(len(self._board)/2) - 1,
                        int(len(self._board[0])/2) -1,
                        int(len(self._board[0])/2))
        lower_pieces = (int(len(self._board)/2),
                        int(len(self._board[0])/2) -1,
                        int(len(self._board[0])/2))
        updated_board = self._board
        updated_board[upper_pieces[0]][upper_pieces[1]] = given_color
        updated_board[lower_pieces[0]][lower_pieces[2]] = given_color
        updated_board[upper_pieces[0]][upper_pieces[2]] = other_color
        updated_board[lower_pieces[0]][lower_pieces[1]] = other_color

        self._board = updated_board

    
    def display_board(self) -> None:
        ''' prints the board onto the console '''
        for row in range(len(self._board)):
            for column in range(len(self._board[row])):
                print(self._board[row][column], end = ' ')
            print()

    def return_turn(self, revert: bool) -> str:
        ''' retuns the string value of current player '''
        if self._turn == 'B':
            current_turn = 'BLACK'
        else:
            current_turn = 'WHITE'

        if revert == True:
            if current_turn == 'BLACK':
                return 'WHITE'
            else:
                return 'BLACK'

        else:
            return current_turn


    def return_row(self) -> int:
        return self._rows

    def return_column(self) -> int:
        return self._columns

    def display_turn(self) -> str:
        ''' displays the current turn '''
        return 'TURN: {}'.format(self._turn)
            
    def switch_turn(self) -> None:
        ''' switches the turn '''
        if self._turn == 'B':
            self._turn = 'W'
        else:
            self._turn = 'B'

    def return_board(self) -> 'board':
        return self._board
            
    def place_piece(self, move: list, test: bool) -> None:
        '''
        places the piece on the board and checks if that move is valid;
        if the move is valid, this function also flips the appropriate pieces
        on the board (the MAIN function of the game)
       
        the logic behind it:
        1. create a copy of the current game board
        2. places the given move onto the copy board
        3. checks if that move is connected to any opposite player's piece,
        since the move will be invalid if that piece is not connected to any other pieces
        4. if connected to some opposite player's piece, the function creates
        a list of DIRECTIONS (N, E, S, W, NE, NS, SW, SE)
        5. with the list of directions, a for loop goes on and flips
        all the appropriate pieces
        '''
        if self._turn == 'B':
            current_turn = 'B'
            opposite_turn = 'W'
        else:
            current_turn = 'W'
            opposite_turn = 'B'
        if (move[0] > 0 and move[0] < len(self._board)+1) and (move[1] > 0 and move[1] < len(self._board[0])+1):

            if self._board[move[0]-1][move[1]-1] != '.':
                raise InvalidMoveError

            #print(' went to here!')
            
            updated_board = []
            for row in range(len(self._board)):
                updated_board.append([])
                for column in range(len(self._board[row])):
                    updated_board[row].append(self._board[row][column])

            updated_board[move[0]-1][move[1]-1] = self._turn
  


            connected = []
            if move[0] > 1:
                if self._board[move[0]-2][move[1]-1] == opposite_turn:
                    connected.append('flip north')
            if move[1] < 4:
                if self._board[move[0]-1][move[1]] == opposite_turn:
                    connected.append('flip east')
            if move[1] > 1:
                if self._board[move[0]-1][move[1]-2] == opposite_turn:
                    connected.append('flip west')
            if move[0] < 4:
                if self._board[move[0]][move[1]-1] == opposite_turn:
                    connected.append('flip south')
            if move[0] > 1 and move[1] > 1:
                if self._board[move[0]-2][move[1]-2] == opposite_turn:
                    connected.append('flip northwest')
            if move[0] > 1 and move[1] < 4:
                if self._board[move[0]-2][move[1]] == opposite_turn:
                    connected.append('flip northeast')
            if move[0] < 4 and move[1] < 4:
                if self._board[move[0]][move[1]] == opposite_turn:
                    connected.append('flip southeast')
            if move[0] < 4 and move[1] > 1:
                if self._board[move[0]][move[1]-2] == opposite_turn:
                    connected.append('flip southwest')


            if len(connected) == 0:
                raise InvalidMoveError

            #print(connected)
            
            flipped_pieces = False
            for direction in connected:
                
                if direction == 'flip north':
                    end_piece_exists = False
                    for i in range(move[0]-2, -1, -1):
                        if updated_board[i][move[1]-1] == current_turn:
                            end_piece_exists = True
                            end_piece = i
                            #print('worked1')
                            #print(move[0]-1)
                            #print(end_piece)
                            break
                    #print('worked2')
                    if end_piece_exists == True:
                        flipped_pieces = True
                        for j in range(move[0]-1, end_piece, -1):
                            #print('worked3')
                            #print(j)
                            updated_board[j][move[1]-1] = current_turn


                if direction == 'flip east':
                    end_piece_exists = False
                    for i in range(move[1], len(self._board[0])):
                        #print(i)
                        if updated_board[move[0]-1][i] == current_turn:
                            end_piece_exists = True
                            end_piece = i
                            #print('end piece= ', end_piece)
                            break
                    if end_piece_exists == True:
                        flipped_pieces = True
                        for j in range(move[1], end_piece):
                            updated_board[move[0]-1][j] = current_turn


                if direction == 'flip west':
                    end_piece_exists = False
                    for i in range(move[1]-2, -1, -1):
                        if updated_board[move[0]-1][i] == current_turn:
                            end_piece_exists = True
                            end_piece = i
                            #print(end_piece)
                            break
                    if end_piece_exists == True:
                        flipped_pieces = True
                        for j in range(move[1]-2, end_piece, -1):
                            updated_board[move[0]-1][j] = current_turn


                if direction == 'flip south':
                    end_piece_exists = False
                    for i in range(move[0], len(self._board)):
                        if updated_board[i][move[1]-1] == current_turn:
                            end_piece_exists = True
                            end_piece = i
                            #print(end_piece)
                            break
                    if end_piece_exists == True:
                        flipped_pieces = True
                        for j in range(move[0], end_piece):
                            updated_board[j][move[1]-1] = current_turn


                if direction == 'flip northeast':
                    counter = 0
                    #print('northeast')
                    end_piece_exists = False
                    for i in range(move[0]-2, -1, -1):
                        #print(i, counter)
                        counter += 1
                        if move[1]-1+counter > len(self._board[0])-1:
                            break
                        if updated_board[i][move[1]-1+counter] == current_turn:
                            end_piece_exists = True
                            end_piece = i
                            #print('end piece= ', end_piece)
                            #print('couter= ', counter)
                            break
                    if end_piece_exists == True:
                        flipped_pieces = True
                        counter = 0
                        for j in range(move[0]-2, end_piece, -1):
                            counter += 1
                            updated_board[j][move[1]-1+counter] = current_turn


                if direction == 'flip northwest':
                    counter = 0
                    #print('northest: ')
                    end_piece_exists = False
                    for i in range(move[0]-2, -1, -1):
                        #print(i, counter)
                        counter += 1
                        if move[1]-1-counter < 0:
                            break
                        if updated_board[i][move[1]-1-counter] == current_turn:
                            end_piece_exists = True
                            end_piece = i
                            #print('end piece: {}'.format(end_piece))
                            #print('counter: {}'.format(counter))
                            break
                    if end_piece_exists == True:
                        flipped_pieces = True
                        counter = 0
                        for j in range(move[0]-2, end_piece, -1):
                            counter += 1
                            updated_board[j][move[1]-1-counter] = current_turn
                            self._board = updated_board

                if direction == 'flip southeast':
                    counter = 0
                    #print('southeast: ')
                    end_piece_exists = False
                    for i in range(move[0], len(self._board)):
                        counter += 1
                        #print(i, move[1]-1+counter)
                        if move[1]-1+counter > len(self._board[0])-1:
                            break
                        if updated_board[i][move[1]-1+counter] == current_turn:
                            #print('worked')
                            end_piece_exists = True
                            end_piece = i
                            break
                    if end_piece_exists == True:
                        flipped_pieces = True
                        counter = 0
                        for j in range(move[0], end_piece):
                            counter += 1
                            updated_board[j][move[1]-1+counter] = current_turn


                if direction == 'flip southwest':
                    counter = 0
                    #print('southwest: ')
                    end_piece_exists = False
                    for i in range(move[0], len(self._board)):
                        counter += 1
                        if move[1]-1-counter < 0:
                            break
                        if updated_board[i][move[1]-1-counter] == current_turn:
                            end_piece_exists = True
                            end_piece = i
                            break
                    if end_piece_exists == True:
                        flipped_pieces = True
                        counter = 0
                        for j in range(move[0], end_piece):
                            counter += 1
                            updated_board[j][move[1]-1-counter] = current_turn
 
            if test == False:

                if flipped_pieces == True:
##                    print('VALID')
                    self._board = updated_board

                elif flipped_pieces == False:
                    raise InvalidMoveError

            elif test == True:

                if flipped_pieces == False:
                    raise InvalidMoveError

 

        else:
            raise InvalidMoveError
        
        
                    


    def check_if_valid_move_left(self) -> bool:
        ''' raises NoMoreValidMoveLeft error if there is no more valid move left '''
        empty_spots = []
        valid_move_left = False
        for row in range(len(self._board)):
            for column in range(len(self._board[row])):
                if self._board[row][column] == '.':
                    empty_spots.append((row, column))
                    
        for spot in empty_spots:
            #print(spot)
            try:
                self.place_piece([spot[0]+1, spot[1]+1], test = True)
            except InvalidMoveError:
                #print('failed')
                pass
            else:
                #print('didnt fail; so it will break!')
                valid_move_left = True
                break

        if valid_move_left == False:
            return False
        
        
            


    def display_score(self) -> str:
        ''' prints the score onto the console '''
        self._black_score = 0
        self._white_score = 0
        for row in range(len(self._board)):
            for column in range(len(self._board[row])):
                if self._board[row][column] == 'B':
                    self._black_score += 1
                if self._board[row][column] == 'W':
                    self._white_score += 1
        return 'B:{:2} W:{:2}'.format(self._black_score, self._white_score)

    def determine_winner(self) -> str:
        ''' prints the winner, according to the winning condtion, onto the console '''
        if self._win_type == '>':
            if self._black_score > self._white_score:
                return 'WINNER: BLACK'
            elif self._black_score < self._white_score:
                return 'WINNER: WHITE'
            elif self._black_score == self._white_score:
                return 'WINNER: NONE'
        elif self._win_type == '<':
            if self._black_score > self._white_score:
                return 'WINNER: WHITE'
            elif self._black_score < self._white_score:
                return 'WINNER: BLACK'
            elif self._black_score == self._white_score:
                return 'WINNER: NONE'
        else:
            return 'something went wrong!'
            
        

    def check_board_full(self) -> FullBoardError:
        ''' raises FullBoardError if the board if full '''
        
        board_has_space = False
        for row in range(len(self._board)):
            for column in range(len(self._board[row])):
                if self._board[row][column] == '.':
                    board_has_space = True
        if board_has_space == False:
            raise FullBoardError


        
        
            
        

# PRACTICES
# 3 1
# 2 1
# 1 2
# 4 3   <<<<<
        
    

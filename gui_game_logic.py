
##  _author = Won Joo Lee

import tkinter



DEFAULT_FONT = ('Helvetica', 14)

class OthelloGUI:
    '''
    GUI class for Othello
    '''

    def __init__(self, GameState: 'Othello Class') -> None:
        '''
        creates the tkinter window, draws all the widgets
        '''

        self._winner_exists = False

        self._GameState = GameState
        self._GameState.create_board()

        self._root_window = tkinter.Tk()

        self._canvas = tkinter.Canvas(
            master = self._root_window, width = 600, height = 600,
            background = 'blue')

        self._canvas.grid(
            row = 4, column = 0, columnspan = 3, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.E + tkinter.S + tkinter.W)

        full_version_label = tkinter.Label(
            master = self._root_window,
            text = 'FULL VERSION',
            font = ('Helvetica', 10))
        full_version_label.grid(
            row = 0, column = 0, columnspan = 3,
            padx = 10, pady = 1,
            sticky = tkinter.N + tkinter.E + tkinter.S + tkinter.W)

        self._gamestate_variable = tkinter.StringVar()
        self._gamestate_variable.set('')
        self._gamestate_label = tkinter.Label(
            master = self._root_window,
            textvariable = self._gamestate_variable,
            font = ('Helvetica', 10))
        self._gamestate_label.grid(
            row = 1, column = 0, columnspan = 3,
            padx = 10, pady = 1,
            sticky = tkinter.N + tkinter.E + tkinter.S + tkinter.W)

        self._gamestate2_variable = tkinter.StringVar()
        self._gamestate2_variable.set('')
        self._gamestate2_label = tkinter.Label(
            master = self._root_window,
            textvariable = self._gamestate2_variable,
            font = ('Helvetica', 10))
        self._gamestate2_label.grid(
            row = 2, column = 0, columnspan = 3,
            padx = 10, pady = 1,
            sticky = tkinter.N + tkinter.E + tkinter.S + tkinter.W)

        self._winner_variable = tkinter.StringVar()
        self._winner_variable.set('')
        self._winner_label = tkinter.Label(
            master = self._root_window,
            textvariable = self._winner_variable,
            font = DEFAULT_FONT)
        self._winner_label.grid(
            row = 3, column = 0, columnspan = 3,
            padx = 10, pady = 1,
            sticky = tkinter.N + tkinter.E + tkinter.S + tkinter.W)
        

        self._score_variable = tkinter.StringVar()
        self._score_variable.set('SCORE')
        self._score_label = tkinter.Label(
            master = self._root_window,
            textvariable = self._score_variable,
            font = DEFAULT_FONT)

        self._score_label.grid(
            row = 5, column = 0, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.E + tkinter.S + tkinter.W)

        self._turn_variable = tkinter.StringVar()
        self._turn_variable.set('TURN')
        self._turn_label = tkinter.Label(
            master = self._root_window,
            textvariable = self._turn_variable,
            font = DEFAULT_FONT)

        self._turn_label.grid(
            row = 5, column = 1, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.E + tkinter.S + tkinter.W)

        self._validity_variable = tkinter.StringVar()
        self._validity_variable.set('VALIDITY CHECK')
        self._validity_label = tkinter.Label(
            master = self._root_window,
            textvariable = self._validity_variable,
            font = DEFAULT_FONT)

        self._validity_label.grid(
            row = 5, column = 2, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.E + tkinter.S + tkinter.W)



        self._draw_board()



        self._canvas.bind('<Configure>', self._on_canvas_resized)
        self._canvas.bind('<Button-1>', self._on_canvas_clicked)

        self._root_window.rowconfigure(0, weight = 0)
        self._root_window.rowconfigure(1, weight = 0)
        self._root_window.rowconfigure(2, weight = 0)
        self._root_window.rowconfigure(3, weight = 0)
        self._root_window.rowconfigure(4, weight = 1)
        self._root_window.rowconfigure(5, weight = 0)
        self._root_window.columnconfigure(0, weight = 1)
        self._root_window.columnconfigure(1, weight = 1)
        self._root_window.columnconfigure(2, weight = 1)

    def _draw_board(self) -> None:
        '''
        draws the game board onto the canvas
        '''
        self._canvas.delete(tkinter.ALL)
        self._row_size = (self._canvas.winfo_height() / self._GameState.return_row()) / (self._canvas.winfo_height())
        for row in range(self._GameState.return_row()):
            self._canvas.create_line(0, self._row_size * self._canvas.winfo_height(),
                                     self._canvas.winfo_width(), self._row_size * self._canvas.winfo_height())
            self._row_size += (self._canvas.winfo_height() / self._GameState.return_row()) / (self._canvas.winfo_height())

        self._column_size = (self._canvas.winfo_width() / self._GameState.return_column()) / (self._canvas.winfo_width())
        for column in range(self._GameState.return_column()):
            self._canvas.create_line(self._column_size * self._canvas.winfo_width(), 0,
                                     self._column_size * self._canvas.winfo_width(), self._canvas.winfo_height())
            self._column_size += (self._canvas.winfo_width() / self._GameState.return_column()) / (self._canvas.winfo_width())


        self._row_size = (self._canvas.winfo_height() / self._GameState.return_row()) / (self._canvas.winfo_height())
        self._column_size = (self._canvas.winfo_width() / self._GameState.return_column()) / (self._canvas.winfo_width())


        for row in range(len(self._GameState.return_board())):
            for column in range(len(self._GameState.return_board()[row])):
                if self._GameState.return_board()[row][column] == 'B':
                    self._canvas.create_oval(
                        self._row_size * (row) * self._canvas.winfo_width(),
                        self._column_size * (column) * self._canvas.winfo_height(),
                        self._row_size * (row + 1) * self._canvas.winfo_width(),
                        self._column_size * (column + 1) * self._canvas.winfo_height(),
                        fill = 'black')
                if self._GameState.return_board()[row][column] == 'W':
                    self._canvas.create_oval(
                        self._row_size * (row) * self._canvas.winfo_width(),
                        self._column_size * (column) * self._canvas.winfo_height(),
                        self._row_size * (row + 1) * self._canvas.winfo_width(),
                        self._column_size * (column + 1) * self._canvas.winfo_height(),
                        fill = 'white')

        self._score_variable.set(self._GameState.display_score())
        self._turn_variable.set(self._GameState.display_turn())
        
                        

        

    def _on_canvas_resized(self, event: tkinter.Event) -> None:
        '''
        calls _draw_board() functions when canvas is resized
        '''
        self._draw_board()
        

    def _on_canvas_clicked(self, event: tkinter.Event) -> None:
        '''
        handles canvas clicks by implementing the move with game_logic module
        and handles errors/acceptance
        '''
        if self._winner_exists == False:
        # checks if the game is over
            move = []
            row_count = 0
            row_size = self._canvas.winfo_height() / self._GameState.return_row()
    ##        print('X and Y: {}, {}'.format(event.x, event.y))
    ##        print('Row Size {}'.format(row_size))
            for row in range(1, self._GameState.return_row()+1):
    ##            print('Row_count * row_size: {}'.format(row_count * row_size))
    ##            print('Row_count+1 * row_size: {}'.format((row_count+1)*row_size))
                if event.y > (row_count * row_size) and event.y < ((row_count+1) * row_size):
                    move.append(row)
                row_count += 1

            column_count = 0
            column_size = self._canvas.winfo_width() / self._GameState.return_column()
            for column in range(1, self._GameState.return_column()+1):
                if event.x > (column_count * column_size) and event.x < ((column_count+1) * column_size):
                    move.append(column)
                column_count += 1

##            print(move)
                
            try:
                self._GameState.place_piece([move[1], move[0]], test = False)
                self._gamestate2_variable.set('')
            except:
                self._validity_variable.set('INVALID')
            else:
                self._validity_variable.set('VALID')
                self._GameState.switch_turn()
                self._draw_board()
                
                try:
                    self._GameState.check_board_full()
                except:
                    self._gamestate_variable.set(
                        'BOARD IS FULL. GAME WILL NOW END')
                    self._winner_variable.set(self._GameState.determine_winner())
                    self._winner_exists = True
                else:
                    if self._GameState.check_if_valid_move_left() == False:
                        self._gamestate2_variable.set(
                            'PLAYER {} DOES NOT HAVE ANY VALID MOVE LEFT. '
                            'TURN WILL REVERT TO PLAYER {}.'.format(
                                self._GameState.return_turn(revert = False),
                                self._GameState.return_turn(revert = True)))
                        self._GameState.switch_turn()
                        self._turn_variable.set(self._GameState.display_turn())
                        
                        if self._GameState.check_if_valid_move_left() == False:
                            self._gamestate2_variable.set(
                                'BOTH PLAYERS DO NOT ANY VALID MOVE LEFT. '
                                'GAME WILL NOW END.')
                            self._winner_variable.set(self._GameState.determine_winner())
                            self._winner_exists = True
        else:
            self._turn_variable.set('GAME IS OVER!')
            self._validity_variable.set('')
 


                    
                        
                    
            

        
                
        
        
        
    def start(self) -> None:
        '''
        startts the window
        '''
        self._root_window.mainloop()





            
    

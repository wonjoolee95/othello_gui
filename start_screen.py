
##  _author = Won Joo Lee

import tkinter
import game_logic
import gui_game_logic


DEFAULT_FONT = ('Helvetica', 14)





class GameSettings:
    '''
    GUI class for game settings
    '''

    def __init__(self) -> None:
        '''
        creates the tkinter window, draws all the widgets
        '''
        self._dialog_window = tkinter.Tk()
        self._dialog_window.geometry('450x700')


        self._game_settings = []

        self._instruction_text = tkinter.StringVar()
        self._instruction_text.set(
            'Welcome to the GUI version of Othello!\n\n'
            'Please specify your desired game settings: ')

        instruction_label = tkinter.Label(
            master = self._dialog_window,
            textvariable = self._instruction_text,
            font = DEFAULT_FONT)

        instruction_label.grid(
            row = 1, column = 0, columnspan = 2,
            padx = 50, pady = 50,
            sticky = tkinter.N + tkinter.E + tkinter.S + tkinter.W)


        full_version_label = tkinter.Label(
            master = self._dialog_window,
            text = 'FULL VERSION',
            font = DEFAULT_FONT)

        full_version_label.grid(
            row = 0, column = 0, columnspan = 2,
            padx = 10, pady = 20,
            sticky = tkinter.N + tkinter.E + tkinter.S + tkinter.W)
        


        ########################################################

        

        ####### ROW #######
                   
        row_label = tkinter.Label(
            master = self._dialog_window,
            text = 'Number of rows: ',
            font = DEFAULT_FONT)

        row_label.grid(
            row = 2, column = 0,
            padx = 50, pady = 20,
            sticky = tkinter.N + tkinter.E + tkinter.S + tkinter.W)

        
        self._row_choice = tkinter.StringVar()
        self._row_option = ('4', '6', '8', '10', '12', '14', '16')
        self._row_menu = tkinter.OptionMenu(
            self._dialog_window, self._row_choice, *self._row_option)
        self._row_menu.grid(
            row = 2, column = 1,
            padx = 50, pady = 20,
            sticky = tkinter.N + tkinter.E + tkinter.S + tkinter.W)


        ####### COLUMN #######

        column_label = tkinter.Label(
            master = self._dialog_window,
            text = 'Number of Columns: ',
            font = DEFAULT_FONT)

        column_label.grid(
            row = 3, column = 0,
            padx = 50, pady = 20,
            sticky = tkinter.N + tkinter.E + tkinter.S + tkinter.W)

        self._column_choice = tkinter.StringVar()
        self._column_option = ('4', '6', '8', '10', '12', '14', '16')
        self._column_menu = tkinter.OptionMenu(
            self._dialog_window, self._column_choice, *self._column_option)
        self._column_menu.grid(
            row = 3, column = 1,
            padx = 50, pady = 20,
            sticky = tkinter.N + tkinter.E + tkinter.S + tkinter.W)

        ####### First Player #######

        first_player_label = tkinter.Label(
            master = self._dialog_window,
            text = 'First Player: ',
            font = DEFAULT_FONT)

        first_player_label.grid(
            row = 4, column = 0,
            padx = 50, pady = 20,
            sticky = tkinter.N + tkinter.E + tkinter.S + tkinter.W)

        self._first_player_choice = tkinter.StringVar()
        self._first_player_option = ('Black', 'White')
        self._first_player_menu = tkinter.OptionMenu(
            self._dialog_window, self._first_player_choice,
            *self._first_player_option)

        self._first_player_menu.grid(
            row = 4, column = 1,
            padx = 50, pady = 20,
            sticky = tkinter.N + tkinter.E + tkinter.S + tkinter.W)

        ####### Upper-Left Piece #######

        upper_left_piece_label = tkinter.Label(
            master = self._dialog_window,
            text = 'Upper Left Piece: ',
            font = DEFAULT_FONT)

        upper_left_piece_label.grid(
            row = 5, column = 0,
            padx = 50, pady = 20,
            sticky = tkinter.N + tkinter.E + tkinter.S + tkinter.W)

        self._upper_left_piece_choice = tkinter.StringVar()
        self._upper_left_piece_option = ('Black', 'White')
        self._upper_left_piece_menu = tkinter.OptionMenu(
            self._dialog_window, self._upper_left_piece_choice,
            *self._upper_left_piece_option)

        self._upper_left_piece_menu.grid(
            row = 5, column = 1,
            padx = 50, pady = 20,
            sticky = tkinter.N + tkinter.E + tkinter.S + tkinter.W)

        ###### Winning Condition #######

        winning_condition_label = tkinter.Label(
            master = self._dialog_window,
            text = 'Winning Condition',
            font = DEFAULT_FONT)

        winning_condition_label.grid(
            row = 6, column = 0,
            padx = 50, pady = 20,
            sticky = tkinter.N + tkinter.E + tkinter.S + tkinter.W)

        self._winning_condition_choice = tkinter.StringVar()
        self._winning_condition_option = ('>: More Pieces', '<: Less Pieces')
        self._winning_condition_menu = tkinter.OptionMenu(
            self._dialog_window, self._winning_condition_choice,
            *self._winning_condition_option)

        self._winning_condition_menu.grid(
            row = 6, column = 1,
            padx = 50, pady = 20,
            sticky = tkinter.N + tkinter.E + tkinter.S + tkinter.W)

        ########################################################


        start_button = tkinter.Button(
            master = self._dialog_window,
            text = 'Click to Start!',
            font = DEFAULT_FONT,
            command = self._on_start_button)

        start_button.grid(
            row = 7, column = 0, columnspan = 2,
            padx = 50, pady = 20,
            sticky = tkinter.N + tkinter.E + tkinter.S + tkinter.W)


        exit_button = tkinter.Button(
            master = self._dialog_window,
            text = 'Exit',
            font = DEFAULT_FONT,
            command = self._on_exit_button)

        exit_button.grid(
            row = 8, column = 0, columnspan = 2,
            padx = 50, pady = 20,
            sticky = tkinter.N + tkinter.E + tkinter.S + tkinter.W)




        self._dialog_window.rowconfigure(0, weight = 1)
        self._dialog_window.rowconfigure(1, weight = 1)
        self._dialog_window.rowconfigure(2, weight = 1)
        self._dialog_window.rowconfigure(3, weight = 1)
        self._dialog_window.rowconfigure(4, weight = 1)
        self._dialog_window.rowconfigure(5, weight = 1)
        self._dialog_window.rowconfigure(6, weight = 1)
        self._dialog_window.rowconfigure(7, weight = 1)
        self._dialog_window.rowconfigure(8, weight = 1)

        self._dialog_window.columnconfigure(0, weight = 1)
        self._dialog_window.columnconfigure(1, weight = 1)



    def _on_start_button(self) -> None:
        '''
        appends all settings to a list and create a Othello class from
        game_logic module
        '''

        self._game_settings.append(self._row_choice.get())
        self._game_settings.append(self._column_choice.get())
        self._game_settings.append(self._first_player_choice.get())
        self._game_settings.append(self._upper_left_piece_choice.get())
        if self._winning_condition_choice.get() != '':
            self._game_settings.append(self._winning_condition_choice.get()[0])
        else:
            self._game_settings.append('')



        game_setting_all_chosen = True
        for setting in self._game_settings:
            if setting == '':
                self._instruction_text.set(
                    'Please select every setting.')
                game_setting_all_chosen = False
                self._game_settings = []
                break

        

        if game_setting_all_chosen:
            if self._game_settings[0] != self._game_settings[1]:
                self._instruction_text.set(
                    'Number of rows and columns must be equal.')
                self._game_settings = []
            else:
                self._dialog_window.destroy()
                initial_set_up = game_logic.Othello(self._game_settings)
                game = gui_game_logic.OthelloGUI(initial_set_up)
                game.start()
            
                

    def _on_exit_button(self) -> None:
        '''
        exit button
        '''
        self._dialog_window.destroy()

    def start(self) -> None:
        '''
        starts the application
        '''
        self._dialog_window.mainloop()

        
        
    

if __name__ == '__main__':

    app = GameSettings()
    app.start()

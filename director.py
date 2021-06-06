
    def _init_(self):
    
        self._keep_playing = True
        self._move = None
     
    
    def start_game(self):

        self._prepare_game()
        while self._keep_playing:
            self._get_imputs()
            self._do_updates()
            self._do_outputs()

    def _prepare_game():



        for n in range(2):
            name = self._console.read(f"enter name of player {n + 1 }: ")
            player = player(name)
            self._roster.add_player(player)
    
    def _get_inputs(self):

        # display the game board
        
        self._console.write(board)
        # get next player's move
        player = self._roster.get_current()
        self._console.write(f"{player.get_name()}'s turn:")
        guess = self._console.read_number("what is your guess?")
        move = Move(guess)
        player.set_move(move)

    def _do_updates(self):

        player = self._roster.get_current()
        move = player.get_move()
        self._board.apply(player, move)

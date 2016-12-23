import gamer
player1 = gamer.Gamer('Alexey')

while True:
    def is_winner_defined():
        print('is_winner_defined(): This function checks whether the winner is found')
    is_winner_defined()

    def greetings_to_winner():
        print('greetings _to_winner(): This function send greetings to the game winner!')
    greetings_to_winner()

    def get_player_for_next_turn():
        print('get_player_for_next_turn(): This function returns the player who makes a move:', player1)
        return player1

    active_player = get_player_for_next_turn()
    active_player.position = gamer.Gamer.make_turn(active_player)

    def сheck_if_player_loose():
        print ('сheck_if_player_loose(): This function checks if a player loses')
    сheck_if_player_loose()

    def greetings_to_looser():
        print('greetings_to_looser(): This function send greetings to a player looser!')
    greetings_to_looser()

    input ('Press button Enter to start a new loop iteration')


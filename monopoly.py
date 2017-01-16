import gamer
from msvcrt import getch
player1 = gamer.Gamer('Alexey')
player2 = gamer.Gamer('Ivan')
player_list = [player1, player2]

def is_winner_defined():
    print('1.is_winner_defined(): This function checks whether the winner is found')
    return False


def greetings_to_winner():
    print('2.greetings _to_winner(): This function send greetings to the game winner!')


def get_player_for_next_turn():
    global player_list
    _active_player = player_list.pop(0)
    player_list.append(_active_player)
    print('3.get_player_for_next_turn(): This function returns the player who makes a move:\n  ', _active_player.name)
    return _active_player


def check_if_player_loose():
    print('4.check_if_player_loose(): This function checks if a player loses')
    return False


def greetings_to_looser():
    print('5.greetings_to_looser(): This function send greetings to a player looser!')


def was_esc_pressed():
    return getch() == b'\x1b'

if __name__ == '__main__':

    while True:
        print('-----------------------------------------------------')
        if is_winner_defined():
            greetings_to_winner()
        active_player = get_player_for_next_turn()
        active_player.make_turn()
        if check_if_player_loose():
            greetings_to_looser()
        if was_esc_pressed():
            break

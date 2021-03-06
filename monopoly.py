import gamer
from msvcrt import getch
player1 = gamer.Gamer('Alexey')
player2 = gamer.Gamer('Ivan')
player_list = [player1, player2]

def is_winner_defined():
    print('is_winner_defined(): This function checks whether the winner is found')
    return False


def greetings_to_winner():
    print('greetings _to_winner(): This function send greetings to the game winner!')


def get_player_for_next_turn():
    global player_list
    active_player = player_list.pop(0)
    player_list.append(active_player)
    print('get_player_for_next_turn(): This function returns the player who makes a move:\n  ', active_player.name)
    return active_player


def check_if_player_loose():
    print('check_if_player_loose(): This function checks if a player loses')
    return False


def greetings_to_looser():
    print('greetings_to_looser(): This function send greetings to a player looser!')


def was_esc_pressed():
    return getch() == b'\x1b'

if __name__ == '__main__':

    while True:
        print('-----------------------------------------------------')
        if is_winner_defined():
            greetings_to_winner()
        active_player = get_player_for_next_turn()
        active_player.position = gamer.Gamer.make_turn(active_player)
        if check_if_player_loose():
            greetings_to_looser()
        if was_esc_pressed():
            break

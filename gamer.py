import random


def check_if_player_should_skip_turn():
    print ('2G.check_if_player_should_skip_turn(): This function check maybe player should skip turn and return True or False')
    return False


def roll_the_dice():
    print('3G.roll_the_dice(): This function change player position')
    return random.randint(1, 6)


def check_if_new_round_started():
    print('4G.check_if_new_round_started(): This function check maybe new round started and return True or False')
    return False


def add_money_for_new_round():
    print('5G.add_money_for_new_round(): This function change player money')


def change_position_for_new_round():
    print('6G.change_position_for_new_round: This function change player position')


def check_pay_taxes():
    print('7G.check_pay_taxes(): This function check maybe player should to pay taxes and return True or False')
    return False


def reduce_money():
    print('8G.add_money_for_new_round(): This function change player money')


def check_field_is_company():
    print('9G.check_field_is_company(): This function check maybe player position it is a company and return True or False')
    return False

def apply_company_rule():
    print('10G.apply_company_rule(): This function is responsible for everything it refers to the companies')


def check_field_is_penalty():
    print('11G.check_field_is_penalty(): This function check maybe player position it is a penalty and return True or False')
    return False


def apply_penalty_rule():
    print('12G.apply_penalty_rule(): This function is responsible for everything it refers to the penalty')


def check_field_is_lotterey():
    print('13G.check_field_is_lotterey(): This function check maybe player position it is a lotterey and return True or False')
    return False


def apply_lotterey_rule():
    print('14G.apply_lotterey_rule(): This function is responsible for everything it refers to the lotterey')


def check_field_is_jail():
    print('15G.check_field_is_jail(): This function check maybe player position it is a jail and return True or False')
    return False


def apply_jail_rule():
    print('16G.apply_jail_rule(): This function is responsible for everything it refers to the jail')


def check_field_is_chance():
    print('17G.check_field_is_chance(): This function check maybe player position it is a chance and return True or False')
    return False


def apply_chance_rule():
    print('18G.apply_chance_rule(): This function is responsible for everything it refers to the chance')


def check_field_is_stock():
    print('19G.check_field_is_stock(): This function check maybe player position it is a stock and return True or False')
    return False


def apply_stock_rule():
    print('20G.apply_stock_rule(): This function is responsible for everything it refers to the stock')


class Gamer:
    def __init__(self, name, colour=None, position=0, money=15000, skip_course=False, immunity=False, company=None, pay_tax=False):
        self.name = name
        self.colour = colour
        self.position = position
        self.money = money
        self.skip_course = skip_course
        self.immunity = immunity
        self.company = company
        self.pay_tax = pay_tax

    def make_turn(self):
        print('1G.make_turn(): This function returns a new position active_player')


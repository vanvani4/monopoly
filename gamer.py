import game_master
import other


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
        if game_master.GameMaster.check_if_player_should_skip_turn(self):
            other.roll_the_dice()
        if other.check_if_new_round_started():
            other.add_money_for_new_round()
            other.change_position_for_new_round()
        if game_master.GameMaster.check_pay_taxes(self):
            other.reduce_money()
        if other.check_field_is_company():
            other.apply_company_rule()
        if other.check_field_is_penalty():
            other.apply_penalty_rule()
        if other.check_field_is_lotterey():
            other.apply_lotterey_rule()
        if other.check_field_is_jail():
            other.apply_jail_rule()
        if other.check_field_is_chance():
            other.apply_chance_rule()
        if other.check_field_is_stock():
            other.apply_stock_rule()

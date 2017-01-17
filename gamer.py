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
            other.Other.roll_the_dice(self)
        if other.Other.check_if_new_round_started(self):
            other.Other.add_money_for_new_round(self)
            other.Other.change_position_for_new_round(self)
        if game_master.GameMaster.check_pay_taxes(self):
            other.Other.reduce_money(self)
        if other.Other.check_field_is_company(self):
            other.Other.apply_company_rule(self)
        if other.Other.check_field_is_penalty(self):
            other.Other.apply_penalty_rule(self)
        if other.Other.check_field_is_lotterey(self):
            other.Other.apply_lotterey_rule(self)
        if other.Other.check_field_is_jail(self):
            other.Other.apply_jail_rule(self)
        if other.Other.check_field_is_chance(self):
            other.Other.apply_chance_rule(self)
        if other.Other.check_field_is_stock(self):
            other.Other.apply_stock_rule(self)

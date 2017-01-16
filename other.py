import random

class Other:


    def roll_the_dice(self):
        print('1.OT.roll_the_dice(): This function change player position')
        return print("New position", random.randint(1, 6))


    def check_if_new_round_started(self):
        print('2.OT.check_if_new_round_started(): This function check maybe new round started and return True or False')
        return False


    def add_money_for_new_round(self):
        print('3.OT.add_money_for_new_round(): This function change player money')


    def change_position_for_new_round(self):
        print('4.OT.change_position_for_new_round: This function change player position')


    def reduce_money(self):
        print('5.OT.add_money_for_new_round(): This function change player money')


    def check_field_is_company(self):
        print('6.OT.check_field_is_company(): This function check maybe player position it is a company and return True or False')
        return False

    def apply_company_rule(self):
        print('7.OT.apply_company_rule(): This function is responsible for everything it refers to the companies')


    def check_field_is_penalty(self):
        print('8.OT.check_field_is_penalty(): This function check maybe player position it is a penalty and return True or False')
        return False


    def apply_penalty_rule(self):
        print('9.OT.apply_penalty_rule(): This function is responsible for everything it refers to the penalty')


    def check_field_is_lotterey(self):
        print('10.OT.check_field_is_lotterey(): This function check maybe player position it is a lotterey and return True or False')
        return False


    def apply_lotterey_rule(self):
        print('11.OT.apply_lotterey_rule(): This function is responsible for everything it refers to the lotterey')


    def check_field_is_jail(self):
        print('12.OT.check_field_is_jail(): This function check maybe player position it is a jail and return True or False')
        return False


    def apply_jail_rule(self):
        print('13.OT.apply_jail_rule(): This function is responsible for everything it refers to the jail')


    def check_field_is_chance(self):
        print('14.OT.check_field_is_chance(): This function check maybe player position it is a chance and return True or False')
        return False


    def apply_chance_rule(self):
        print('15.OT.apply_chance_rule(): This function is responsible for everything it refers to the chance')


    def check_field_is_stock(self):
        print('16.OT.check_field_is_stock(): This function check maybe player position it is a stock and return True or False')
        return False


    def apply_stock_rule(self):
        print('17.OT.apply_stock_rule(): This function is responsible for everything it refers to the stock')
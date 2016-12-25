class Gamer:
    def __init__(self, name, colour = None, position = 0, money = 15000, skip_course = False, immunity = False, company = None, pay_tax = False):
        self.name = name
        self.colour = colour
        self.position = position
        self.money = money
        self.skip_course = skip_course
        self.immunity = immunity
        self.company = company
        self.pay_tax = pay_tax

    def make_turn(self):
        print('make_turn: This function returns a new position active_player')

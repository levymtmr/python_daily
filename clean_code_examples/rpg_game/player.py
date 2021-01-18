import random
from body import Body


class Player(Body):
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.power = 10
        self.weapon = {"sword": (10, 15)}

    def atack(self):
        hit_point = self.power + random.randint(
            self.weapon["sword"][0], self.weapon["sword"][1]
        )
        return hit_point

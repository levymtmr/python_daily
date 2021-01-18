class Body:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def __str__(self):
        return self.name

    def damage(self, hit_point):
        self.hp -= hit_point

    def is_dead(self):
        if self.hp <= 0:
            return True

    def status(self):
        attributes = {"Name": self.name, "Hp": self.hp}
        print(attributes)

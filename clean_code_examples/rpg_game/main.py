from player import Player
from enemie import Enemie

player = Player(name="levy", hp=100)
spider = Enemie(name="spider", hp=100)

running = True

turn = 0


def fight_loop(turn, player, other):
    running = True
    if turn % 2 == 0:
        print("{} turn: ".format(player.__str__()))
        choose = input("[1] atack [2] inventory [3] status")
        if choose == 1:
            print("Player atack!!\n")
            other.damage(player.atack())
            if other.is_dead():
                print("{} is Dead".format(other.__str__()))
                running = False
        if choose == 3:
            player.status()

    if turn % 2 == 1:
        print("{} Turn: \n".format(other.__str__()))
        print("{} status".format(other.__str__()))
        print(other.status())
        print("Spider Atack!!\n")
        player.damage(10)
        if player.is_dead():
            print("{} is Dead".format(player.__str__()))
            running = False
    return running


while running:
    running = fight_loop(turn, player, spider)
    turn += 1

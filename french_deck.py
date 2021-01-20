import collections
from random import choice

Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    """
    Os métodos nomeados como métodos especiais, realizam um comportamento
    automatico. Ou são desencadeado por certas funções padrões da propria.
    Como len() e get em dicionarios utilizando [] ex: deck[0].
    """

    ranks = [str(n) for n in range(2, 11)] + list("JQKA")  # fileiras
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


suits_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suits_values) + suits_values[card.suit]


deck = FrenchDeck()
print("Total de cartas: ", len(deck))  # metodo __len__ é chamado.
print("Get item [0]", deck[0])  # método getitem é chamado.
print("Get item [2]", deck[2])  # método getitem é chamado.
print("Get item [2]", deck[-1])  # método getitem é chamado.

print("Escolhendo aleatorio com a lib padrao choice", choice(deck))

# Usando o (slicing) fatiamento já atribuido por manipular o método __getitem__()
print("0 a 3", deck[:3])

# retornando apenas os ás
print("comecando no 12 e adicionando a cada 13 cartas", deck[12::13])

# Por implementar o metodo __getitem__ ele tbm pode sofrer interação
for card in deck:
    print(card)

# For na ordem inversa
print("Ordem inversa")
for card in reversed(deck):
    print(card)

# Pelo o fato da classe ser iteravel o operador "in" funciona
print("Q hearts está contido em Card ?", Card("Q", "hearts") in deck)
print("7 beasts está contido em Card ?", Card(7, "beasts") in deck)

print("Ordem crescente de classificação: ")
for card in sorted(deck, key=spades_high):
    print(card)

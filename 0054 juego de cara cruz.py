import random

coin_option = ['Heads - Cara','Tails - Cruz']
random_selection = random.choice(coin_option)

flip_coin = input('Que lado Crees Que Callo: \t||Heads - Cara||\t o \t||Tails - Cruz|| : \n')


if flip_coin.lower() in random_selection.lower():
    print('Felicitaciones Adivinastes el Lanzamiento fue {} '. format(random_selection))
else:
    print('Has Fallado el Turno')

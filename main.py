from player import Player
from secret_number import secret_number
from roulette import roulette
import csv

INVALID_CHOICE = 'Choix non valide. Recommencez.'

players_file = 'players.csv'
players = []

try:
    with open(players_file, 'r') as file:
        reader = csv.reader(file)
        for e in list(reader):
            players.append(Player(e[0], {'nombre secret': int(e[1]), 'roulette': int(e[2])}))
except FileNotFoundError:
    with open(players_file, 'x', newline=''):
        pass
except IndexError:
    pass

print('Bienvenue au PPNUM-Casino')
player = None

while player is None:
    entry = input('R = Reprendre avec un précédent joueur, N = Nouveau joueur, X = Quitter ? ').casefold()
    if entry == 'n':
        name = input('Votre nom (2 caractères minimum) ? ')
        if len(name) > 1:
            player = Player(name)
        else:
            print(INVALID_CHOICE)
    elif entry == 'r':
        for i in range(len(players)):
            print(f'{i} = {players[i].name}')
        name_choice = input('Votre choix ? ')
        try:
            name_choice = int(name_choice)
            player = players[name_choice]
        except (ValueError, IndexError):
            print(INVALID_CHOICE)
    elif entry == 'x':
        exit()
    else:
        print(INVALID_CHOICE)

play = True
while play:
    print('Choisissez votre jeu !')
    entry = input('S = Nombre secret, R = Roulette, X = Quitter ? ').casefold()
    if entry == 'x':
        break
    elif entry == 's':
        player.set_scores(secret_number(), 'nombre secret')
    elif entry == 'r':
        player.set_scores(roulette(), 'roulette')
    else:
        print(INVALID_CHOICE)

    play_choice = input('Rejouer (O/N) ? ').casefold()
    if play_choice != 'o':
        play = False

print('\nRécapitulatif des scores')
print(player)
print("\nMerci d'avoir joué avec nous! À bientôt!")

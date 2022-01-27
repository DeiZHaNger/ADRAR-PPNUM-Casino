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
            players.append(Player(e[0], int(e[1]), {'nombre secret': int(e[2]), 'roulette': int(e[3])}))
except FileNotFoundError:
    with open(players_file, 'x', newline=''):
        pass
except (ValueError, IndexError):
    pass

print('Bienvenue au PPNUM-Casino')
player = None

while player is None:
    entry = input('R = Reprendre avec un précédent joueur, N = Nouveau joueur, X = Quitter ? ').casefold()
    if entry == 'n':
        name = input('Votre nom (2 caractères minimum) ? ')
        if len(name) > 1:
            player = Player(name)
            players.append(player)
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

print(f'Infos joueur\n{player}')

play = True
while play:
    print('\nChoisissez votre jeu !')
    entry = input('S = Nombre secret, R = Roulette, Z = Réinitialiser votre compte, X = Quitter ? ').casefold()
    if entry == 'x':
        break
    elif entry == 'z':
        player.reset_account()
    elif entry == 's':
        score, gain = secret_number(player.money)
        player.set_scores(score, 'nombre secret')
        player.apply_gain(gain)
    elif entry == 'r':
        score, gain = roulette(player.money)
        player.set_scores(score, 'roulette')
        player.apply_gain(gain)
    else:
        print(INVALID_CHOICE)

    play_choice = input('Continuer de jouer (O/N) ? ').casefold()
    if play_choice != 'o':
        play = False

with open(players_file, 'w', newline='') as file:
    writer = csv.writer(file)
    for e in players:
        lst = [e.name, e.money] + list(e.best_scores.values())
        writer.writerow(lst)

print('\n----- Récapitulatif -----')
print(player)
print("\nMerci d'avoir joué avec nous! À bientôt!")

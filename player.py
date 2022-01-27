from abc import ABC


class BasePlayer(ABC):
    def __init__(self):
        self.SCORES = (('nombre secret', 0), ('roulette', 0))
        self.MONEY = 1000


class Player(BasePlayer):
    def __init__(self, name, money=None, best_scores=None):
        super().__init__()
        self.name = name
        self.money = self.MONEY if money is None else money
        self.best_scores = dict(self.SCORES) if best_scores is None else best_scores

    def set_scores(self, score, game):
        self.best_scores[game] = max(self.best_scores[game], score)

    def apply_gain(self, gain):
        self.money += gain

    def reset_account(self):
        self.best_scores = dict(self.SCORES)
        self.money = self.MONEY

    def __repr__(self):
        str_player = f'\t{self.name}\n\t\tSolde : {self.money}$\n\t\tMeilleurs Scores :'
        for key, value in self.best_scores.items():
            str_player += f'\n\t\t\t{key.capitalize()} -> {value}'
        return str_player


if __name__ == '__main__':
    from random import randrange

    sample_player = Player(input('Votre Pseudo ? '))
    print('\n', sample_player)

    for game in sample_player.best_scores:
        input('\nAppuyez sur Entrée pour simuler un jeu')
        print(f'\n{sample_player.name} joue à {game.upper()}...')
        score = randrange(100)
        gain = randrange(2 * sample_player.money) - sample_player.money
        print(f'Il obtient un score de {score}! et {("gagne", "perd")[gain < 0]} {abs(gain)}$')
        sample_player.set_scores(score, game)
        sample_player.apply_gain(gain)

    input('\nAppuyez sur Entrée pour voir les scores')
    print('\n', sample_player)

    input('\nAppuyez sur Entrée pour réinitialiser votre compte')
    sample_player.reset_account()
    print('\n', sample_player)


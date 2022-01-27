from abc import ABC


class BasePlayer(ABC):
    def __init__(self):
        self.SCORES = (('nombre secret', 0), ('roulette', 0))


class Player(BasePlayer):
    def __init__(self, name, best_scores=None):
        super().__init__()
        self.name = name
        self.best_scores = dict(self.SCORES) if best_scores is None else best_scores

    def set_scores(self, score, game):
        self.best_scores[game] = max(self.best_scores[game], score)

    def reset_scores(self):
        self.best_scores = dict(self.SCORES)

    def __repr__(self):
        str_player = f'\t{self.name}\n\t\tMeilleurs Scores :'
        for key, value in self.best_scores.items():
            str_player += f'\n\t\t\t{key.capitalize()} -> {value}'
        return str_player


if __name__ == '__main__':
    from random import randrange

    sample_player = Player(input('Votre Pseudo ? '))
    print('\n', sample_player)
    for game, _score in sample_player.best_scores.items():
        input('\nAppuyez sur Entrée pour simuler un jeu')
        print(f'\n{sample_player.name} joue à {game.upper()}...')
        score = randrange(100)
        print(f'Il obtient un score de {score}!')
        sample_player.set_scores(score, game)
    input('\nAppuyez sur Entrée pour voir les scores')
    print('\n', sample_player)

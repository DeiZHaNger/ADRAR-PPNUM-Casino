from random import randrange


def secret_number() -> int:
    secret = randrange(1000) + 1
    print('\nVous avez 10 tentatives pour deviner le nombre secret (entre 1 et 1000)!\n(Q pour arrêter)')
    tries = 10
    while tries != 0:
        guess = input(f'Tentative n°{11 - tries} : ')
        if guess in ('q', 'Q'):
            tries = 0
            break
        try:
            guess = int(guess)
            if not 1 <= guess <= 1000:
                raise ValueError
        except ValueError:
            print("Ceci n'est pas nombre entre 1 et 1000!\nDommage, vous perdez un essai bêtement!")
            tries -= 1
            continue
        if guess == secret:
            print('Bravo! Vous avez trouvé')
            break
        else:
            print('Dommage! Réessayez')
        tries -= 1

    score = tries * 10
    print(f'Le nombre secret était {secret}. Vous obtenez un score de {score}')

    return score


if __name__ == '__main__':
    secret_number()

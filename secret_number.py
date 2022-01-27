from random import randrange


def secret_number(money=1000) -> tuple[int, int]:
    default_stake = min(100, money)
    max_tries = 10
    victory_bonus = 1000

    print('Vous jouez au Nombre secret.')

    try:
        stake = int(input(f'Fixez votre mise en $ (min 10 / max {money} / par défaut {default_stake}) : '))
        if not 10 <= stake <= money:
            raise ValueError
    except ValueError:
        stake = default_stake

    print(f'Vous misez {stake}$')

    secret = randrange(1000) + 1
    print('\nVous avez 10 tentatives pour deviner le nombre secret (entre 1 et 1000)!\n(X pour arrêter)')

    score = 0
    tries_left = max_tries
    while tries_left != 0:
        tries_left -= 1
        count = max_tries - tries_left

        guess = input(f'Tentative n°{count} : ').casefold()
        if guess == 'x':
            break

        try:
            guess = int(guess)
            if not 1 <= guess <= 1000:
                raise ValueError
        except ValueError:
            print("Ceci n'est pas nombre entre 1 et 1000!\nDommage, vous perdez un essai bêtement!")
            continue

        if guess == secret:
            score += victory_bonus - 50 * (count - 1)
            print('Bravo! Vous avez trouvé')
            break
        else:
            score += max(0, 100 - abs(guess - secret)) // count
            print(f'Dommage! Réessayez! (Score actuel: {score})')

    multiplier = score // 100
    gain = stake * (multiplier - 1)
    print(f'\nLe nombre secret était {secret}.')
    print(f'Vous quittez le nombre secret avec {money + gain}$ et un score de {score}')

    return score, gain


if __name__ == '__main__':
    secret_number()

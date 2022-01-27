from random import randrange
from time import sleep


def roulette(money=1000) -> tuple[int, int]:
    starting_balance = money
    bets = 0

    print('Pariez à la roulette !')
    while money >= 10:
        default_stake = min(100, money)
        print(f'\nVous disposez de {money}$')

        try:
            stake = int(input(f'Fixez votre mise en $ (min 10 / max {money} / par défaut {default_stake}) : '))
            if not 10 <= stake <= money:
                raise ValueError
        except ValueError:
            stake = default_stake

        print(f'Vous misez {stake}$')

        choice = input('\nP = Pair, I = Impair, ou choisissez un nombre entre 1 et 36 (X pour quitter) ? ').casefold()
        multiplier = 0
        draw = randrange(36) + 1
        draw_is_even = (draw % 2 == 0)

        if choice == 'x':
            break
        elif choice == 'p':
            if draw_is_even:
                multiplier = 2
        elif choice == 'i':
            if not draw_is_even:
                multiplier = 2
        else:
            try:
                choice = int(choice)
                if not 1 <= choice <= 36:
                    raise ValueError
                if choice == draw:
                    multiplier = 10
            except ValueError:
                print("Ceci n'est pas un nombre entre 1 et 36!\nDommage, vous perdez votre argent bêtement!")

        print('Tirage en cours...')
        sleep(1)
        print('... Priez...')
        sleep(1)
        print(f'Le numéro gagnant est le {draw} - {("impair", "pair")[draw_is_even]}')
        gain = (multiplier - 1) * stake
        print(f'Vous {("gagnez", "perdez")[gain < 0]} {abs(gain)}$')
        money += gain
        bets += 1

        replay = input('Continuer à miser (O/N) ? ').casefold()
        if replay == 'n':
            break

    gain = money - starting_balance
    score = max(0, bets * gain // 10)
    print(f'\nVous quittez la roulette avec {money}$ et un score de {score}')

    return score, gain


if __name__ == '__main__':
    roulette()

from random import randrange
from time import sleep


def roulette() -> int:
    money = 1000
    bets = 0
    print('Pariez à la roulette, mise de 100$ par essai!\n')
    while True:
        multiplier = 0
        print(f'Vous disposez de {money}$')
        choice = input('Q = Quitter, P = Pair, I = Impair, ou choisissez un nombre entre 1 et 36 ? ').casefold()
        draw = randrange(36) + 1
        draw_is_even = draw % 2 == 0
        if choice == 'q':
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
                print("Ceci n'est pas nombre entre 1 et 1000!\nDommage, vous perdez votre argent bêtement!")

        print('Tirage en cours... Priez...')
        sleep(2)
        print(f'Le numéro est {draw}')
        gain = (multiplier - 1) * 100
        print(f'Vous {("gagnez", "perdez")[gain < 0]} {abs(gain)}$')
        money += gain
        bets += 1

        replay = input('Continuer à miser (O/N) ? ').casefold()
        if replay == 'n':
            break

    score = bets * money // 100
    print(f'Vous quittez la roulette avec {money}$. Un score de {score}')

    return score


if __name__ == '__main__':
    roulette()

import argparse
from math import comb, factorial, pow

def pi0(m, l, r):
    the_sum = 0
    for j in range(0, l-r):
        nominator = pow(-1, j) * factorial(l)
        denominator = factorial(j) * factorial(l-j)
        multiple1 = nominator/denominator

        nominator = factorial(l - r) * factorial(l - j)
        denominator = factorial(l) * factorial(l - r - j)
        multiple2 = pow(nominator/denominator, m)

        the_sum += multiple1 * multiple2

    return the_sum

def pi1(m, l, r):
    n0 = factorial(l) / pow(factorial(l/m), m)
    N = pow(comb(l, r), m)
    return n0/N

def probability_of_failure(players, slots, rejections):
    if players*rejections < slots:
        return 0
    if players*rejections == slots:
        return pi1(m=players, l=slots, r=rejections)
    return pi0(m=players, l=slots, r=rejections)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
                    prog='FailCalc',
                    description='Calculates the probability of failure to schedule a DnD session',
                    )

    parser.add_argument('-p', '--players', type=int, default=7, help='The number of players (including the DM) to gather at the table')
    parser.add_argument('-s', '--slots', type=int, default=3, help='The number of available time slots to choose from')
    parser.add_argument('-r', '--rejections', type=int, default=1, help='The number of time slots when each player cannot make')

    args = parser.parse_args()

    players = args.players
    available_slots = args.slots
    rejections = args.rejections

    p = probability_of_failure(
        players,
        available_slots,
        rejections,
    )

    print(f"For {players} players having conflicts for {rejections} out of {available_slots} available slots,")
    print(f"Probability of failure is {p*100:.3f}%")

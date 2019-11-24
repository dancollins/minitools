#!/usr/bin/env python3
'''
Figures out the load cap values to use when implementing a Pierce oscillator
circuit - such as you might find on pretty much any microcontroller.
'''
import argparse


def calculate(C_load, C_stray):
    '''
    Calculates and displays the calculated load capacitance values.

    :param C_load: Target load capacitance, in pF.
    :param C_stray: Stray capacitance value in the circuit, in pF.
    '''
    values = []

    # There's not many choices, so we'll check all of them!
    for i in range(1, 30):
        # Cl = (C1 * C2) / (C1 + C2) + C_stray
        # Our implementation is symmetrical, so C1 == C2.
        x = int(i ** 2) / (i * 2)
        x += C_stray

        error = C_load - x
        values.append((i, x, error))

    # Sort by the closest match
    values.sort(key=lambda x: abs(x[2]))

    # Print the top 5 options
    print('|  C1, C2 |   C_load |   Error |')
    print('|---------+----------+---------|')

    for val in values[:5]:
        print(f'| {val[0]:>4} pF | {val[1]:>5} pF | {val[2]:>4} pF |')


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('target_load_capacitance', type=int,
                        help='Target in pF')

    parser.add_argument('stray_capacitance', type=int,
                        help='Stray capacitance in pF')

    args = parser.parse_args()

    calculate(args.target_load_capacitance, args.stray_capacitance)


if __name__ == '__main__':
    main()

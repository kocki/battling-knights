#!python
"""Battling Knights."""

__author__ = 'Adam Kochanowski'
__copyright__ = 'Copyright 2020, Adam Kochanowski'
__credits__ = ['BBOXX']
__email__ = 'adam.kochanowski@gmail.com'
__status__ = 'prototype'
__version__ = '0.0.1'

# Standard Library
import json
import sys
import time

# 3rd-party
from battling_knights.battle import Battle

ANIMATE = False
REPORT = False

GAME_START = 'GAME-START'
GAME_END = 'GAME-END'


def battle(file_name, animate=None, report=None):
    """Run battle campaign regarding to directives from file."""
    if report is None:
        report = REPORT
    if animate is None:
        animate = ANIMATE
    state = ''
    in_game = False

    with open(file_name, 'r') as f:
        campaign = Battle()
        line = f.readline().strip()
        while line:
            if line == GAME_END:
                in_game = False

            if in_game:
                knight, direction = line.split(':')
                campaign.move_knight(knight, direction)

            if line == GAME_START:
                in_game = True

            if animate:
                print(25 * '\n', campaign.board.draw())
                time.sleep(.2)

            line = f.readline().strip()

    if report:
        state += campaign.board.draw() + '\n'
        state += campaign.knights_report()
        return state

    return json.dumps(campaign.state())


def main(input_file_path):
    """Maintain program."""
    if not input_file_path:
        return sys.stderr.write('Required parameter: input file path\n')

    print(battle(input_file_path[0]))


if __name__ == '__main__':  # pragma: no cover
    if 'animate' in sys.argv[2:]:
        ANIMATE = True
    if 'report' in sys.argv[2:]:
        REPORT = True

    main(sys.argv[1:2])

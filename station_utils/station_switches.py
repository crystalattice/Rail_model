#!/usr/bin/env python3
"""
station_switches.py

Purpose: Programmatically generate a list of switch names.

Author: Cody Jackson

Date: 1/15/19
################################
Version 0.2
    Added function
Version 0.1
    Initial build
"""

from string import ascii_lowercase


def switch_gen():
    """Generate a list of switches, in the form of 1a, 1b, 2a..."""
    switches = []
    for i in range(1, 11):
        for x in ascii_lowercase[:2]:
            switches.append("{}{}".format(i, x))

    return switches


if __name__ == "__main__":
    print(switch_gen())

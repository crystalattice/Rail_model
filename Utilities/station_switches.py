#!/usr/bin/env python3
"""
station_switches.py

Purpose: Programmatically generate a list of switch names.

Author: Cody Jackson

Date: 1/15/19
################################
Version 0.1
    Initial build
"""

from string import ascii_lowercase

switches = []
for i in range(1, 5):
    for x in ascii_lowercase[:2]:
        switches.append("{}{}".format(i, x))

if __name__ == "__main__":
    print(switches)

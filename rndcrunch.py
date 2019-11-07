#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import sys
import signal 
import argparse

amount = 1000
sequence = "0123456789"
size= 20

parser = argparse.ArgumentParser(description='rndcrunch - Generate random keys')
parser.add_argument('-c', '--count', required=False, dest='count', type=int, default=amount, help=f"The amount of random keys to generate (default: {amount}; use 0 to create an inifinite amount)" )
parser.add_argument('-a', '--alpha', required=False, dest='alpha', type=str, default=sequence, help=f"Alphabet to choose from (default: {sequence})")
parser.add_argument('-l', '--length', required=False, dest='length', type=int, default=size, help=f"Length of generated keys (default: {size})")

args = parser.parse_args()

def signal_handler(sig, frame):
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

produced = 0

while True:
    data = []
    for i in range(args.length):
        data.append(random.choice(args.alpha))

    print("".join(data))
    sys.stdout.flush()
    produced = produced + 1
    if produced == args.count:
        break

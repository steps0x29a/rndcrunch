# rndcrunch
A simple wordlist generator that generates random keys

# Installation
Simply install python3, there should be no additional steps required.

# Why?
Ever tried to crack a WPA-2 key using [crunch](https://sourceforge.net/projects/crunch-wordlist/) and [aircrack-ng](https://www.aircrack-ng.org/)? I tried with my FritzBox! which uses a 20 character numeric key.

When I pipe crunch into aircrack-ng, it will start with `00000000000000000000`, then test `00000000000000000001`, then `00000000000000000002` and so on.
I decided that I wanted randomized keys, so...here goes :)

# Usage
    # Generate 1000 keys of 20 characters chosen randomly from 0123456789
    python3 rndcrunch.py

    # Generate 666 keys of 23 characters chosen randomly from abcdefghijklmnopqrstuvwxyz
    python3 rndcrunch.py -c 666 -l 23 -a abcdefghijklmnopqrstuvwxyz

    # Show help
    python3 rndcrunch.py --help

# Contribute
Feel free!

# Disclaimer
This is a quick and dirty program, nothing you should base production code on or something. I'm not responsible if this blows up in your face :)

Have fun!

# Acknowledgement
I shamelessly 'borrowed' the name from [crunch](https://sourceforge.net/projects/crunch-wordlist/).


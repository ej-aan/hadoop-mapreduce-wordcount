#!/usr/bin/env python
import sys

word_dict = {}

for line in sys.stdin:
    line = line.strip()
    position, word = line.split('\t', 1)
    position = int(position)
    word_dict[position] = word

for position in sorted(word_dict.keys()):
    print('%s\t1' % word_dict[position])

#!/usr/bin/env python
import sys

position = 0

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for word in words:
        print('%s\t%s' % (position, word))
        position += 1

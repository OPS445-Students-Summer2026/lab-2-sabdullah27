#!/usr/bin/env python3

# Author: Syed Abdullah
# Author ID: sabdullah27
# Date Created: 2026/05/25

import sys

if len(sys.argv) > 1:
    timer = int(sys.argv[1])
else:
    timer = 3

while timer != 0:
    print(timer)
    timer = timer - 1
print('blast off!')

"""Demo 3 - Vanilla tqdm with default settings for comparison"""

import sys
from time import sleep
from tqdm import tqdm


t = tqdm(total=50)
for x in range(50):
    sleep(0.02)
    t.update(1)
    if x == 25:
        t.write('info')
    if x == 40:
        t.write('error', file=sys.stderr)

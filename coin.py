#
# Coin
#

import random


class Coin:
    def __init__(self):
        # Coin has no state until it's flipped
        self.state = None

    def flip(self):
        self.state = 'H' if random.random() < 0.5 else 'T'

    def is_heads(self):
        if (self.state == None):
            raise RuntimeError("You haven't flipped the coin yet!")
        return self.state == 'H'


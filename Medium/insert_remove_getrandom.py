import random

class RandomizedSet(object):
    # all = []

    def __init__(self):
        # self.val = val
        # RandomizedSet.all.append(self.val)
        self.all = []

    def insert(self, val: int) -> bool:
        if val in self.all:
            return False
        else:
            self.all.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.all:
            self.all.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.all)
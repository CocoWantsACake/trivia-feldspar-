import random
import trivia
import pytest


class Randrange:
    range_nine = [6, 9, 2, 4, 7, 0, 5, 1, 0, 2, 8, 4, 2, 3, 8, 1, 2, 5, 1, 7, 8, 4, 5, 7, 8, 1, 3, 1, 9, 2, 9, 6, 2, 2, 1, 0, 2, 6, 1, 2, 8, 9, 7, 1, 3, 5, 2, 5, 1, 3]
    ct_nine = 0

    range_five = [6, 6, 6, 1, 3, 1, 6, 4, 1, 2, 4, 6, 1, 2, 3, 4, 2, 3, 1, 1, 6, 1, 6, 6, 3, 4, 6, 4, 4, 2, 6, 4, 2, 5, 5, 4, 6, 4, 1, 6, 5, 5, 5, 5, 1, 2, 3, 3, 4, 4]
    ct_five = 0

    def __call__(self, *args, **kwargs):
        if args[0] == 5:
            res = self.range_five[self.ct_five]
            self.ct_five += 1
            return res

        if args[0] == 9:
            res = self.range_nine[self.ct_nine]
            self.ct_nine += 1
            return res



def test_output_same_as_always(monkeypatch):
    monkeypatch.setattr(random, "randrange", Randrange())
    trivia.

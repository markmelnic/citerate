import os, sys, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import citerate

TEST_SET = [
    [10, 11, 12, 13, 14],
    [25, 2,  3,  4,  15],
    [24, 9,  1,  5,  16],
    [23, 8,  7,  6,  17],
    [22, 21, 20, 19, 18],
]

if __name__ == "__main__":
    for v in citerate.citerator(TEST_SET, x = 2, y = 2):
        print(v)

    for layer in citerate.citerator(TEST_SET, x = 2, y = 2, layer=True):
        print(layer)

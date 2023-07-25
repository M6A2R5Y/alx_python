#!/usr/bin/python3
for a in range(10):
    for j in range(a + 1, 10):
        m = "{:02d}".format(a * 10 + j)
        print(m, end=", " if (a, j) != (8, 9) else "\n",)


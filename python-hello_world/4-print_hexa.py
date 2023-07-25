#!/usr/bin/python3
def aj():
    aj = 1
    while aj <= 98:
        print("{0} = {1}\n".format(aj, hex(aj)), end="")
        aj += 1

if __name__ == "__main__":
    aj()

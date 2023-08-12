#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for line in matrix:
        for cool in range(len(line)):
            if cool == len(line) - 1:
                print("{:d}".format(line[cool]), end="")
            else:
                print("{:d}".format(line[cool]), end="")
        print()
#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    lenargs = len(argv) - 1
    if len(argv) == 1:
        print("{:d} arguments.".format(lenargs))
    elif len(argv) == 2:
        print("{:d} argument:".format(lenargs))
    else:
        print("{:d} arguments:".format(lenargs))
    lenargs = len(argv)
    for i in range(1, lenargs):
        print("{:d}: {}".format(i, argv[i]))

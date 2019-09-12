#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    lenargs = len(argv)
    summ = 0
    for i in range(1, lenargs):
        summ += int(argv[i])
    print("{:d}".format(summ))

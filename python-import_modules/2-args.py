#!/usr/bin/python3
import sys

def main():
    print("{} arguments".format(len(sys.argv) - 1))

    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))

if __name__ == "__main__":
    main()
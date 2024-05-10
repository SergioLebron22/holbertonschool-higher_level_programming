#!/usr/bin/python3
add = __import__("add_0").add

def main():
    a = 1
    b = 2

    print("{} + {} = {}".format(a, b, add(a, b)))

if __name__ == "__main__":
    main()
    
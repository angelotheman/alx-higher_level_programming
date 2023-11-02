#!/usr/bin/python3

if __name__ == '__main__':
    import sys
    args = len(sys.argv) - 1

    if args == 0:
        print("{} arguments.".format(args))
    else:
        print("{} {}:".format(args, "argument" if args == 1 else "arguments"))
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))

#!/usr/bin/python3
import sys
message = ""
if len(sys.argv) == 1:
    message = "argument"
else:
    message = "arguments"
print("{} {}:".format(len(sys.argv), message))
[print("{}: {}".format(x, y)) for x , y in enumerate(sys.argv, start=1)]

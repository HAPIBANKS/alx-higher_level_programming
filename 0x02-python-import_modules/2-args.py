#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    num_args = len(argv)
    if num_args == 0:
        print("0 arguments.")
    else:
        plural = "s" if num_args > 1 else ""
        print("{} argument{}:".format(num_args, plural))
        for i, arg in enumerate(argv, start=1):
            print(f"{i}: {arg}")

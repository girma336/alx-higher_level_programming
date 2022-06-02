#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv)
    if length < 2:
        print("0")
    else:
        sum = 0
        for num in range(1, length):
            sum += int(sys.argv[num])
        print(sum)

#!/usr/bin/python3
# break.py 



def main():
    s = 'this is a string'

    # Print string and skip all s's.
    for c in s:
        if c == 's':
            continue
        print(c, end='')

    print()
    # Print string and stop at first s.
    for c in s:
        if c == 's':
            break
        print(c, end='')

    print()

    # For Loop Else continues after last iterator value.
    for c in s:
        print(c, end='')
    else:
        print("else")


if __name__ == "__main__": main()

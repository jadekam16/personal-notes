import sys

# designed to search for a specific substring within the lines of a file/std input and also print the lines. 
def process_stream(f, name, substring):
    """
    print lines containing substring
    """

    # iterates over each line using enumerate --> provides both line number starting from 1 and line content (line)
    for (line_number, line) in enumerate(f, start=1):
        if substring in line:
            print(f'{name}:{line_number}:{line}', end='')

def main():
    """
    process files given as arguments, if no arguments process stdin
    """
    if len(sys.argv) == 2:
        process_stream(sys.stdin, "<stdin>", sys.argv[1])
    elif len(sys.argv) > 2:
        for pathname in sys.argv[2:]:
            with open(pathname, 'r') as f:
                process_stream(f, pathname, sys.argv[1])


if __name__ == '__main__':
    main()
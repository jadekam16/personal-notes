#!/usr/bin/env python3

import sys

def main():
    """
    TASK

    Write a simple version of the head command in Python,
    that accepts an optional command line argument in the form -n,
    where n is a number, and displays the first n lines from its
    standard input. If the -n option is not used, then the program
    simply displays the first ten lines from its standard input.

    ADDITIONAL TASK:
    Modify the head program from the previous question so that, 
    as well as handling an optional -n argument to specify how many 
    lines, it also handles multiple files on the command line and 
    displays the first n lines from each file, separating them by 
    a line of the form ==> FileName <===
    """
    number = 10
    files=[]
    # if number is inputted with the -n option
    for arg in sys.argv[1:]:
        if arg.startswith('-'):
          # [1] gets the first argument, [1:] means start at the second
          # character and continue to the end of the line
          number = int(arg[1:])
        else:
          files.append(arg)
    
    for filename in files:
       with open(filename, 'r') as f:
          lines = f.readlines()

          print(f"==> {filename} <==")

          for i in range(min(number, len(lines))):
            print(lines[i].strip('\n'))
                
          print()

if __name__ == '__main__':
    main()

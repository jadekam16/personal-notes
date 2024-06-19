#!/bin/sh                               # tells the system that this is code you want to be run 

if test $# -eq 1                        # checks number of command line arguments
then
    start=1
    finish=$1
elif test $# -e1 2
then
    start = $1
    finish = $2
else
    echo "Usage: $0 <n> [<m>]" 1>&2     # error message which goes to stderr
    exit 1
fi

i=$start                                # use first command line argument
while test $i -le $finish               # test is used to test for exit status, -le = less than/equal to
do
    echo $i
    i=$((i + 1))                        # to do arithmetic use $((logic here)): limited arithmetic though, probably faster in python
done
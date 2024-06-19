# Week 3 Lecture Notes

## Shell 

### Exit Status
- when unix programs finish they give OS an exit status 
    - return value of main becomes exist status of C program 
    - in Python, exit status is supplied as an argument to sys.exit 
- usually a small integer (0-4) 
    - non-zero means error occurred 
- if/while statement conditions use exit status 

### Test Command
- peforms a test or combo of test 
    - does/prints nothing
    - returns 0 exit status if success, non-zero if fails 
- avail as '[' instead of test 

### While statements syntax
```
while command 
do 
    body-commands
done
```

**EXAMPLE: PRINTS SEQUENCE OF NUMBERS W/ USER INPUT** 
```
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

i=$start                             # use first command line argument
while test $i -le $finish           # test is used to test for exit status, -le = less than/equal to
do
    echo $i
    i=$((i + 1))                        # to do arithmetic use $((logic here)): limited arithmetic though, probably faster in python
done
```

Note: to run program is ./file (same as python)

### Scripts to get website data 
```
curl website-url | wc
```

### Run a web server 
$ python3 -m https.server 
$ /2041 (to add a port number)

**To get data**:
$ curl https://hostname/endpoint (GET REQUEST)

**EXAMPLE: CHECK FOR CHANGES IN THE WEBPAGE**
```
#!/bin/dash

sleep_seconds=1 

if test $# -eq 2
then
    regex=$1
    url=$2
    email_address=$3
else
    echo "usage: $0 <regex> <url>" 1>&2
    exit 1
fi

while true 
do
    if curl --silent "$url" | grep -E "$regex" 
    then 
        echo "alert from $0"|mail "$email_address"
        exit 0
    fi

    echo -n .
    sleep $sleep_seconds                                # delays the program 
done
```

### For Loop syntax

```
for var in word1 word2 word3
do
    body-commands
done
```
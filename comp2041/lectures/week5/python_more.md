# Python More

## Names and Types
- python associates types with values 
- type function lets us see types: ```type(variable)```

## Python Sequences 
- does not have arrays 
- 3 basic sequence types: lists (can be changed), tuples (cannot be changed), and ranges. 

### Useful Sequence Operations 
- x in s: True if an item of s is equal to x
- x not in s: False if an item of s is equal to x
- s + t: the concatenation of s and t, also s += t
- s * n: equivalent to adding s to itself n times, also s *= n
- s[i]: ith item of s
- s[i:j]: slice of s from i to j
- s[i:j:k]: slice of s from i to j with step k
- len(s): length of s
- min(s): smallest item of s
- max(s): largest item of s
- s.index(x[, i[, j]]): index of the first occurrence of x in s (at or after index i and before index j)
- s.count(x): total number of occurrences of x in s
- s[i] = x: item i of s is replaced by x
- s[i:j] = t slice of s from i to j is replaced by elements of t
- del s[i:j] same as s[i:j] = []
- s[i:j:k] = t the elements of s[i:j:k] are replaced by those of t
- del s[i:j:k] removes the elements of s[i:j:k] from the list
- s.append(x) appends x to the end of the sequence
- s.clear() removes all items from s
- s.copy() creates a shallow copy of s
- s.insert(i, x) inserts x into s at the index given by i
- s.pop() or s.pop(i) retrieves the item at i and also removes it from s
- s.remove(x) remove the first item from s where s[i] is equal to x
- s.reverse() reverses the items of s in place
- s.sort() sort the items of s in place

## Examples 
```
# Python implementation of /bin/echo
import sys
print(' '.join(sys.argv[1:])) # joins the elements of the list into a single string, with each element separated by a space.
```

```
# sum integers supplied as command line arguments
import sys
total = 0
for arg in sys.argv[1:]:
try:
  total += int(arg)
except ValueError:
  print(f"error: '{arg}' is not an integer", file=sys.stderr)
  sys.exit(1)
print("Sum of the numbers is", total)
```

```
# Count the number of lines on standard input.
import sys
lines = sys.stdin.readlines()
line_count = len(lines)
print(line_count, "lines")
```

## Opening Files
```
file = open('data')

# read from file 'data'
file = open('data', 'r')

# read from file 'data'
file = open("results", "w")

# write to file 'results'
file = open('stuff', 'ab')
```

- File objects can be explicitly closed with ```file.close()```

### Reading and writing a file
```
file = open("a.txt", "r")
data = file.read()
file.close()

file = open("a.txt", "w")
file.write(data)
file.close()
``` 

## Exceptions
- Opening a file may fail; always check for exceptions 
```
try:
  file = open('data')
except OSError as e:
  print(e)
```

- OSError is a group of errors. 
- You can do specific errors: 
```
try:
`file = open('data')
except PermissionError:
...

except FileNotFoundError:
.... 
```

## Context Managers 
- The file will be closed when execution leaves the code block, using a context manager.
```
sum = 0
with open("data", "r") as input_file:
for line in input_file:
try:
  sum += int(line.strip())
except ValueError:
  pass
print(sum)
```

### Example Implementation: cp function various versions 
```
OK FOR BIG FILES

# Simple cp implementation for text files using line-based I/O
# and with statement and error handling
import sys
if len(sys.argv) != 3:
  print("Usage:", sys.argv[0], "<infile> <outfile>", file=sys.stderr)
  sys.exit(1)
try:
  with open(sys.argv[1]) as infile:
    with open(sys.argv[2], "w") as outfile:
    for line in infile:
        outfile.write(line)
except OSError as e:
  print(sys.argv[0], "error:", e, file=sys.stderr)
sys.exit(1)
```

```
NOT OK FOR BIG FILES: USING READLINES

# Simple cp implementation for text files using line-based I/O
# reading all lines into array (not advisable for large files)
import sys
if len(sys.argv) != 3:
  print("Usage:", sys.argv[0], "<infile> <outfile>", file=sys.stderr)
  sys.exit(1)
try:
  with open(sys.argv[1]) as infile:
    with open(sys.argv[2], "w") as outfile:
      lines = infile.readlines()
      outfile.writelines(lines)
except OSError as e:
  print(sys.argv[0], "error:", e, file=sys.stderr)
  sys.exit(1)
```

```
# Simple cp implementation using shutil.copyfile
import sys
from shutil import copyfile

if len(sys.argv) != 3:
  print("Usage:", sys.argv[0], "<infile> <outfile>", file=sys.stderr)
  sys.exit(1)
try:
  copyfile(sys.argv[1], sys.argv[2])
except OSError as e:
  print(sys.argv[0], "error:", e, file=sys.stderr)
  sys.exit(1)
```

```
# Simple cp implementation by running /bin/cp
import subprocess
import sys
if len(sys.argv) != 3:
  print("Usage:", sys.argv[0], "<infile> <outfile>", file=sys.stderr)
  sys.exit(1)
p = subprocess.run(['cp', sys.argv[1], sys.argv[2]])
sys.exit(p.returncode)
```

## UNIX FILTER BEHAVIOUR
- fileinput can be used to get UNIX-filter behavior.
- treats all command-line arguments as file names
- opens and reads from each of them in turn
- no command line arguments, then fileinput == stdin
- accepts - as stdin
  
so this is cat in Python:
```
import fileinput
for line in fileinput.input():
  print(line)
```

## USING PYTHON DICTS
```
# Check if we've seen a line read from stdin,
# using a dict.
# Print snap! if a line has been seen previously
# Exit if an empty line is entered

line_count = {}
while True:
try:
  line = input("Enter line: ")
except EOFError:
  break
if line in line_count:
  print("Snap!")
else:
  line_count[line] = 1
```

### Useful Operations
- d[key]: Return the item of d with key key
- del d[key]: Remove d[key] from d. Raises a KeyError if key is not in the map.
- key in d: Return True if d has a key key, else False.
- key not in d: Equivalent to not key in d.
- keys(): Return a new view of the dictionary’s keys
- items(): Return a new view of the dictionary’s items
- get(key[, default]): Return the value for key if key is in the dictionary, else default
- values(): Return a new view of the dictionary’s values.
- update([other]): Update the dictionary with the key/value pairs from other
- setdefault(key[, default]): If key is in the dictionary, return its value. If not, insert and return default.
- clear(): Remove all items from the dictionary.
- copy(): Return a shallow copy of the dictionary.

## SUBPROCESSES
- requires you to import subprocess module to run external programs.
  - subprocess.run(): usually the func used to run external programs.
  - subprocess.Popen(): can be used if lower level cnontrol is necessary

```
$ subprocess.run(['date', '--utc'])
Tue 05 Aug 1997 01:11:01 UTC
```

### Capturing output from External Programs with subprocess 
```
>>> p = subprocess.run(["date"], capture_output=True, text=True)
>>> p.stdout
'Mon 18 Jul 2022 10:27:28 AEST\n'
>>> p.returncode
0
>>> q = subprocess.run(["ls", "no-existent-file"], capture_output=True, text=True)
>>> q.stderr
"ls: cannot access 'no-existent-file': No such file or directory\n"
>>> q.returncode
2
```
- captured output is a byte sequence (binary) by default.
- the option text=True converts it to a string

### Passing input to an External Programs with subprocess 
To send input to a program:

```
>>> message = "I love COMP(2041|9044)\n"
>>> p = subprocess.run(["tr", "a-z", "A-Z"], input=message, capture_output=True, text=True
>>> p.stdout
'I LOVE COMP(2041|9044)\n'
>>> # note, you don't need an external program for this
>>> message.upper()
'I LOVE COMP(2041|9044)\n'
```

### Example - Using Subprocess to Capture 
```
import subprocess
p = subprocess.run(["date"], capture_output=True, text=True)
if p.returncode != 0:
  print(p.stderr)
  exit(1)
weekday, day, month, year, time, timezone = p.stdout.split()
print(f"{year} {month} {day}")
```

### Python and External Commands 
```
Optionally subprocess can pass the command to a shell to evaluate, e.g.:
>>> subprocess.run("sort *.csv | cut -d, -f1,7 >output.txt", shell=True)
```

### Serving Web Pages with Python
```
Python includes a http server - easy to use for development/testing.
>>> server_address = ('', 2041)
>>> handler = http.server.SimpleHTTPRequestHandler
>>> with http.server.HTTPServer(server_address, handler) as h:
... h.serve_forever()

And there is a convenient command-line short cut:
$ echo hello from httpd >hello.txt
$ python3 -m http.server 2041
Serving HTTP on 0.0.0.0 port 2041 (http://0.0.0.0:2041/) ...
127.0.0.1 - - [17/Jul/2023 10:19:00] "GET /hello.txt HTTP/1.1" 200 -

in another terminal
$ curl -s http://0.0.0.0:2041/hello.txt
hello from httpd
```
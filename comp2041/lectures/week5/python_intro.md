# Python Introduction 

**running python**: ```python3 code.py or ./code.py```

using the ```#!/usr/bin/env python3``` makes the program file executable

## Variables
- numeric: int, float 
- Text: str
- Sequence: list, tuple, range 
- Mapping: Dic
- More: Boolean, None, Functions, Class
- More: Set, bytes etc. 

! You cannot have unintialised variables, just give a None type if you have no value yet. 

## Operators 
- Comparison Operators are the same as usual 
- Bitwise Operators are the same as usual:
  - &: and --> Sets each bit to 1 if both bits are 1
  - |: or --> Sets each bit to 1 if one of two bits is 1
  - ^: xor -->  Sets each bit to 1 if only one of two bits is 1
  - -: not --> Inverts all the bits
  - <<: left shift --> Shift left by pushing zeros in from the right, and let the leftmost bits fall off
  - '>>': right shift -->  Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
- Arithmetic Operators are the same as usual 
- Assignment Operators (mostly intuitive) but here are special ones:
  - //= Division (returns int)
  - /= Division (returns float)
- Logical Operators: uses words i.e., and, or, not
- New Operators
  - Identity: x *is* y returns True if both variables are the same object
  - Identity: x *is not* y returns True if both variables are not the same object
  - Membership: x *in* y returns True if a sequence with the specified value is present in the object
  - Membership: x *not in* y returns True if a sequence with the specified value is present in the object
- Boolean Values
  - False is false
  - None is False
  - 0 is false 
  - Empty things are false 
  - Everything else is true

## Control Structures 
- all statements within these must be after a colon *:*
- selection is handled by if -> elif -> else  
  - can also use match -> case (basically switch case)
- iteration is handle by while and for 
  - for value in iterator
    - can use range i.e., for value in range(90 (min), 100 (max), 2 (increment, default is 1))
    - can also do this:
      - ```for _ in range(n): pow *= k```
  - while boolExpr
- can use  ```break``` and ```continue```

## Terminating 
- normal termination: sys.exit(1) 
- abnormal termination: ```assert``` or ```raise```

i.e., ```assert data is not None, "data was None, it shouldn't be"```
or
```
def func (a):
if not isinstance(a, int):
raise TypeError(f"\'{a}\' is not of type <int>")
```

## Code Examples
- Formatting String: ```print(f"this is a formatted string: {string}")```
- Reading Lines:
```
sum = 0
for line in stdin:
  sum += int(line)
  print(f"Sum of the numbers is {sum}")
```
or
```
sum = 0
for line in stdin:
  try:
    sum += int(line)
  except ValueError as e:
    print(e)
print(f"Sum of the numbers is {sum}")
```

## String Manipulation

```
try:
  line = input("Enter some input: ")
except EOFError:
  print("could not read any characters")
  exit(1)

n_chars = len(line)
print(f"That line contained {n_chars} characters")
if n_chars > 0:
  first_char = line[0]
  last_char = line[-1]
print(f"The first character was '{first_char}'")
print(f"The last character was '{last_char}'")
```

## String Comparison 
```
last = None
while True:
  try:
    curr = input("Enter line: ")
  except EOFError:
    print()
    break
  if curr == last:
    print("Snap!")
    break
  last = curr
```

## Exponential Concatenation
```
if len(sys.argv) != 2:
  print(f"Usage: {sys.argv[0]}: <n>")
  exit(1)
n = 0
string = "@"
while n < int(sys.argv[1]):
  string *= 2
  n += 1
print(f"String of 2^{n} = {len(string)} characters created")
```
# Week 7: Python Functions 

- python functions can be defined likeso: 
```
def polly(x, a, b, c):
  return a * x ** 2 + b * x + x
```

- they can be called likeso:
```
polly(3, 5, -3, 6)
```

- you can also set default values, so u can call functions without specifying all parameters 
```
def polly(x, a=1, b=2, c=0):
  ....

polly(3)
```

### Packing/Unpacking operators * and ** allow variable number of arguments 
- packing/unpacking operators * and ** allow variable number of arguments.
  - Use * to pack positional arguments into tuple
  - Use ** to pack keyword arguments into dict

```
def f(*args, **kwargs):
    print('positional arguments:', args)
    print('keywords arguments:', kwargs)

>>> f("COMP", 2041, 9044, answer=42, option=False)
positional arguments: ('COMP', 2041, 9044)
keywords arguments: {'answer': 42, 'option': False}
```

### Main function 
- done likes this:
```
def main():
    ...

if __name__ == "__main__":
    main()
```

### docstrings 
- is a string specified as first statement of function 
- provides documentation 
```
def polly(x, a, b, c):
    """
    calculate quadratic polynomial 
    a -- squared component
    b -- linear component
    c -- offset
    """
    return ... 
```

### variable scope 
- variable is by default local, unless its specified to be 'global' by its keyword.
```
def f():
    x=34
    print(x)

def g():
    global x 
    x=56
    print(x)
```

### list comprehensions
- used to create lists(iterables) concisely
- they can be written as ```expression for value in iterable```
```
>>> [x**3 for x in range(10)] 
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
```
- they can also be written as ```expression for value in iterable if expression2```
```
>>> [x**3 for x in range(10) if x % 2 == 1]
[1, 27, 125, 343, 729]
```

### using lambda
- keyword lambda helps create small anonymous functions 
  - useful for passing functions to other functions
  - allows creation of a function within an expression 
```
>>> f = lambda x: x + 42
>>> type(f)
<class 'function'>
>>> f(12)
54
```
- lambda function body must be a single expression
  - function body can not contain statements such as while, return
  - better to define a named function if body is complex

### enumerate
- returns tuples pairing a count with member of an iterable such as a list 
```
>>> languages = ['C', 'Python', 'Shell', 'Rust']
>>> list(enumerate(languages))
[(0, 'C'), (1, 'Python'), (2, 'Shell'), (3, 'Rust')]
>>> list(enumerate(languages, start=42))
[(42, 'C'), (43, 'Python'), (44, 'Shell'), (45, 'Rust')]
```

- it's like assigning a value to each tuple, it's an i!?

### zip
- returns tuples formed from elements in the same index 
```
>>> languages = ['C', 'Python', 'Shell', 'Rust']
>>> editors = ['vi', 'emacs', 'atom', 'VScode', 'nano']
>>> list(zip(editors, languages))
[('vi', 'C'), ('emacs', 'Python'), ('atom', 'Shell'), ('VScode', 'Rust')]
```

### map
- calls func with arguments(s) taken from iterable(s) such as list(s) and returns functions return values. 
- basically loops thru list, applies the args to each element, then returns the value. 

### filter 
- returns elements of iterables(list) for which the func returns tre for. 
  - jus filters elements fr. 
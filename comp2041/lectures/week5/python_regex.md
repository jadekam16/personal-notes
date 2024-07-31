# Python Regex 
Most of code/info in <regex.py> 

## Python Characters Clsses 

- \d matches any digit, for ASCII: [0-9]
- \D matches any non-digit, for ASCII: [^0-9]
- \w matches any word char, for ASCII: [a-zA-Z_0-9]
- \W matches any non-word char, for ASCII: [^a-zA-Z_0-9]
- \s matches any whitespace, for ASCII: [ \t\n\r\f]
- \S matches any non-whitespace, for ASCII: [^ \t\n\r\f]
- \b matches at a word boundary
- \B matches except at a word boundary
- \A matches at the start of the string, same as ^
- \Z matches at the end of the string, same as $

### Raw Strings
- python raw-string is prefixed with an r (for raw)
  - can prefix with r strings quoted with ' " ''' """ 
- literally means there if theres \n or \t it'll just appear in the string i.e., ```this is a raw string\n```

## Match Objects
- search, match, fullmatch returns a match obj if a match suceeds, None if it fails. 

```
print("Destroy the file system? ")
answer = input()
if re.match(r'yes|ok|affirmative', answer, flags=re.I):
  subprocess.run("rm -r /", Shell=True)
```

where ```flags=re.I``` means ignore case when matching. 

A match obj can provide useful info:

```
>>> m = re.search(r'[aiou].*[aeiou]', 'pillow')
>>> m
<re.Match object; span=(1, 5), match='illo'>
>>> m.group(0)
'illo'
>>> m.span()
(1, 5)
>>>
```

these methods are outlined in <regex.py>. 

### Capturing Parts of a Regex Match 
- brackets are used for grouping in extended regex. 
- *group(n)* method returns part of the sring matched by the nth pair of brackets.

```
>>> m = re.search('(\w+)\s+(\w+)', 'Hello Andrew')
>>> m.groups()
('Hello', 'Andrew')
>>> m.group(1)
'Hello'
>>> m.group(2)
'Andrew'
```

### Non-Capturing Group
- ```(?:...)``` is a non-capturing group.
  - Groups parts of the pattern together.
  - Does not save the matched text.
  - Does not increase the group count.  
  - same group behaviour as (...)
   - Captures the part of the string matched by the group.
   - Saves the matched text, which can be referenced later using backreferences.
   - Increases the group count.
  - doesn't capture the part of the string matched by the group.

### Greedy versus non-Greedy Pattern Matching
- default for pattern matching is **greedy**:
  - starts match the first place it can succeed
  - make the match as long as possible
- ```?``` operator changes pattern matching to **non-greedy**
  - starts match the first place it can succeed
  - make the match as short as possible

```
>>> s = "abbbc"
>>> re.sub(r'ab+', 'X', s)
'Xc'
>>> re.sub(r'ab+?', 'X', s)
'Xbbc'
```

### re.findall
- ```re.findall``` returns a list of the matched strings
```
>>> re.findall(r'\d+', "-5==10zzz200_")
['5', '10', '200']
```

- if regex contains multiple () a list of tuples is returned.
```
>>> re.findall(r'(\d)\d*(\d)', "-5==10zzz200_")
[('1', '0'), ('2', '0')]
>>> re.findall(r'([^,]*), (\S+)', "Hopper, Grace Brewster Murray")
[('Hopper', 'Grace')]
>>> re.findall(r'([A-Z])([aeiou])', "Hopper, Grace Brewster Murray")
[('H', 'o'), ('M', 'u')]
```

### re.split 
- ```re.split``` splits a string where a regex matches.
```
>>> re.split(r'\d+', "-5==10zzz200_")
['-', '==', 'zzz', '_']
```
- like cut in shell script 
```
>>> re.split(r'\s*,\s*', "abc,de, ghi ,jk , mn")
['abc', 'de', 'ghi', 'jk', 'mn']
```

see also the string join function
```
>>> a = re.split(r'\s*,\s*', "abc,de, ghi ,jk , mn")
>>> a
['abc', 'de', 'ghi', 'jk', 'mn']
>>> ':'.join(a)
'abc:de:ghi:jk:mn'
```
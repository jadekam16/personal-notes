# Week 1 Lecture Notes

## Unix Filters
- **Filter**: program that transforms a byte stream (byte stream of text)
- On Unix-like systems, filters are commands that:
    - read bytes from standard input/files
    - perform transformations on the stream
    - write transformed bytes to their standard output
    - most filters work on text, UTF-8 or ASCII
    - most are line-based, some byte-based or character-based


### Using filters 
- Filters usually allow you to give arguments i.e., input files and if you don't give anything, it'll take its arguments from std input. 
``` 
$ filter < input.txt > output.txt 
$ < input.txt filter > output.txt 
$ < input.txt > output.txt filter
```

- When used in combination with each other, become a powerful problem solving kit.
- Connects the output of one program to the input of another program via a pipeline:

```
filter | filter2 | filterN
```

- The **cat.py** file is a simple unix filter that reads the bytes that was given as input.

### Common Filters 

```
$ head filename 
```

gives the first 10 lines of input. 

```
$ tail filename 
```
gives the last 10 lines of input. 

```
$ cat filename 
```
prints everything

```
$ wc filename 
```
gives you numbers of lines, words etc. in the program. 

**! BE WARY OF TABS AND WHITESPACE IN YOUR FILE**
```
$ cat -A filename
```
shows the presence of these.

```
$ cat --help
```
if you want to see all the current methods available for cat. 

**Example: Usage of a filter**
```
$ ./fgrep.py , course.tsv > match.txt
$ wc match.txt
```
where course.tsv is an input file and match.txt is the output file. This counts how many lines after the fgrep filter has been applied to the initial input file. 

A more efficient way...
```
$ ./fgrep.py , course.tsv | wc
```
which eliminates the need for an output file. 

- Available filter which find subsets of files/filter lines (same thing as fgreps above)
```
$ grep Substring file.tsv | wc
```
where substring is whatever string you are searching for. 

- Regular expressions (regex): defining a set of strings.

### Regex Basics 
- Unless a character has a special meaning it matches itself 
    - e.g. a has no special meaning so it matches a.
- 𝑝* denotes zero or more repetitions of 𝑝.
    - e.g. b* matches the empty string and: b, bb, bbb, bbbb …
    - note this is an infinite set of strings
- 𝑝𝑎𝑡𝑡𝑒𝑟𝑛1|𝑝𝑎𝑡𝑡𝑒𝑟𝑛2 denotes the union of 𝑝𝑎𝑡𝑡𝑒𝑟𝑛1 and 𝑝𝑎𝑡𝑡𝑒𝑟𝑛2.
    - e.g perl|python|ruby matches any of: perl, python or ruby
    - | is sometimes called alternation
- Parentheses are used for grouping
    - e.g. c(,c)* matches: c c,c c,c,c c,c,c,c …
        - and (d|e)*(f|g) matches f, g, df, dg, ef, eg, ddf, deg, edf, edg, eef, …
- backslash \ removes any special meaning of the following character
    - e.g. \* matches an * instead of indicating repetition
- Any regular expression can be written using only ()*|\
    - but many syntax features are present for convenience & clarity.

When using grep...
```
$ grep -E 'String|String2' file.tsv
```
where -E means give full regex. 

Another useful example...
```
$ grep -E 'Comput(er|ing)' file.tsv | wc
```
Case Sensitivity
```
$ grep -iE 'Comput(er|ing)' file.tsv | wc
```
the '-i' ignores case. 

### Anchoring Matches 
- regular expressions may be used to match against a whole string
    - e.g re.fullmatch in Python
- regular expressions are often used to match a substring (part of a string)
    - e.g grep prints lines containing a substring matching the regular expression
    - e.g re.search in Python (re.match matches only at start of string)
- when matching part of a string you can limit matches to the start or end of a string (or both)
    - start of the string is denoted by ^ (uparrow)
    - ^hello matches a string starting with hello
    - note ^ has two meanings in regular expressions
    - e.g. ^[abc] matches a or b or c at the start of a string.
    - e.g. [^abc] matches any character except a or b or c (anywhere in the string)
- the end of the string is denoted by $ (dollar)
    - cat$ matches cat at the end of a string.
    - ^cat.*dog$ matches any string starting cat and finishing dog.

### Convenient Regex 
- . (dot) matches any single character.
- Square brackets provide convenient matching of any one of a set of characters.
    - [listOfCharacters] matches any single character from listOfCharacters.
    - e.g. [aeiouAEIOU] matches any (English) vowel.
- A shorthand is available for ranges of characters [𝑓𝑖𝑟𝑠𝑡 − 𝑙𝑎𝑠𝑡]
    - e.g [a-e] [a-z] [0-9] [a-zA-Z] [A-Za-z] [a-zA-Z0-9]
- Square brackets matching can be inverted with an ^
    - [^listOfCharacters] matches any single character except those in listOfCharacters.
    - e.g [^a-e] matches any character except one of the first five lowercase letters
- Other characters lose their special meaning inside bracket expressions.
    - e.g. [^X]*X matches any characters up to and including the first X


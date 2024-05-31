# Tutorial 1 Notes 

## Operating System 
- software that manages hardware of a computer + provides interface to the programs that run on the computer e.g. MacOS, Windows, Unix/Linux 
- to check: ```uname -a```

## Regex and Grep 

### Filters
- transforms input and produces output
- Examples: cat, grep, wc, tr, head/tail, cut, sort, uniq, sed, find, join, paste, tee, and xargs

### Regex 
- patterns used for matching strings w/ text.
  - e.g. checking email address is valid 
  - see if word is in a file 
  - removing unwanted words 

To see more rules: https://jaydenleung.notion.site/Week-01-89402c86a586435895fc69bd5b9e402f

### Grep 
- copies to standard output the lines that match the specified regex
- useful flags:
  -  `-E` matches full POSIX regex***
  - `-i` ignores upper/lower case `grep -i 'h' file.txt`
  - `-v` displays lines that do not match the pattern `grep -v 'h'    file.txt`
  - `-c` print a count of matching lines

**Use this to debug: https://regex101.com/** 

## Exercises 

### Regex 
1. Write a regex to match C preprocessor commands in a C program source file
```
^#
```
2. All lines in a C program with trailing white space (one or more white space at the end of line)
```
\s*$
# \s is a bracket expression that matches any white space character.
```
3. The names "Barry", "Harry", "Larry" and "Parry”
```
^[BHLP]arry$
```
4. A string containing the word "hello" followed, some time later, by the word "world”
```
hello.*world
```
5. The word "calendar" and mis-spellings where 'a' is replaced with 'e' or vice-versa
```
c[ae]l[ae]nd[ae]r
```
6. This regular expression [0-9]*.[0-9]* is intended to match floating point numbers such as '42.5'. Is it appropriate?
- No, because the dot can match any character. The more appropriate regex would be (0|[1-9][0-9]*)\.([0-9]*[1-9]|0) (note the escape on the dot and how the regex accounts for repetitions or 0)

### Grep 
1. Why does grep -E hello seem to be taking a long time to run?
- Because it is waiting for input from stdin.

2. Why won’t grep -E int main program.c work?
- grep -E will attempt to search files main and program.c for lines containing the string int. so u need quotes around 'int main' so it doesn't consider main as a file. 

3. Give five reasons why this attempt to search a file for HTML paragraph and break tags may fail ```grep <p>|<br> index.html```
- <, > and | are part of the shell’s syntax so the shell will interpret them rather than passing them to grep → avoid by wrapping the regex expression with **single or double quotes**.
- grep by itself doesn’t implement | so will need to use **grep -E**.
- The supplied regex expression won’t match the HTML tags if they’re in upper case (e.g. <P></P>) so use **grep -Ei** to make it case-insensitive.
- The supplied regular expression also won't match HTML tags containing spaces, e.g: <p > so account for the whitespaces i.e. grep -Ei **'<\s*(p|br)\s*>'** index.html --> the star is to ensure so one or more spaces matches not just one. 
- The HTML tag may contain attributes, e.g: <p class="lead_para"> so change it to **grep -Ei '<\s*(p|br)[^>]*>'** index.html
  - [^>] = include everything that is not a closing bracket then closing bracket 

4. Write a grep -E command which will print any lines in a file ```ips.txt``` containing an IP addresses in the range 129.94.172.1 to 129.94.172.25 
```
grep -E "129\.94\.172\.([1-9]|1[0-9]|2[0-5])$" ips.txt
```

5. Write a grep -E command which prints position real numbers at the start of the line in ```nums.txt```.
```
grep -E "^(([0-9]|[1-9][0-9]+)\.?[0-9]*)" nums.txt
```
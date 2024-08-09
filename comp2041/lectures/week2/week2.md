# Week 2 Lecture Notes 

## Filters 


## Shell 
- shells are command interpreters 
  - allow interactive users to execute commands 
  - command causes another program to be run 
  - may have a graphical (point-and-click) interface 
- **bash**: most popular used shell for unix-like system 
  - others include: dash, ash, zsh, fish 
- use **dash** for scripts in 2041 
  - implements POSIX standard shell features (POSIX: family of standards for maintaining compatibility among operating systems)
  - scripts wrriten for dash are compatible with bash, zsh & ash

### What Shells DO 
- unix shells have the same basic mode of operation: 
```
loop
  if (interactive) print a prompt 
  read a line of user input 
  apply transformations to line 
  split line into words using whitespace 
  use first word in line as command name
  execute command, passing other words as arguments
end loop
```
- shells can also be run with commands in a file
- shells are programming languages 
- shells have design decisions to suit interacive use:
  - variables don't have to be initialised/declared 
  - not ideal for programming in shell 

### Processing a Shell Input Line 
- series of **transformations** are applied to shell input lines 
  - tilde expansion: e.g. ~z1234567 --> /home/z1234567 
    - when word begins with an unquoted tilde character ~, all characters up to the first unquoted slash are considered a *tilde-predix*. Its the process of converting these abbreviations to the directory names that they stand for. 
  - parameter and variable expansion e.g. $HOME --> /home/z1234567
  - arithmethic expansion: e.g. $((6 * 7)) --> 42 
  - command substitution e.g. $(whoami) --> z1234567
  
### echo
- prints args to stdout 
- mainly used in scripts 
- useful options 
    - -n: do not output a trailing newline 
    - -e: enale interpretation of backlash escapes 
- equivalent to a print statement fr 
```
$ echo Hello Andrew
Hello Andrew
$ echo '\n'
\n
$ echo -e '\n'
$ echo -n Hello Andrew
Hello Andrew$
```

### shell variables 
- do not need to be declared/initialised 
- $name replace with value of variable name 
- name=value assigns value to name, no spaces around = 
- '

### $(command)
- command expansion 
- $(command) is evaluated by running command 
  - stdout is captured from command 
```
$ now="$(date)"
$ echo $now
Sun 23 Jun 1912 02:31:00 GMT
$
```
- so basically, it executes a command and stores the result in the variable. 

### single/double quotes
- single quotes '' group the characters into a single word 
  - no characters interpreted specially inside single quotes 
  - cannot put single quotes in single quotes, can put double quotes 
- double quotes "" group the characters within into a single word 
  - can put single quotes 
  - special characters works here 
```
$ answer=42
$ echo "The answer is $answer."
The answer is 42.
$ echo 'The answer is $answer.'
The answer is $answer.
```

### << 
- <<word called a here document 
  - multi-line string 
```
$ name=Andrew
$ tr a-z A-Z <<END-MARKER
Hello $name
How are you
Good bye
END-MARKER
HELLO ANDREW
HOW ARE YOU
GOOD BYE
```

### arithmetic 
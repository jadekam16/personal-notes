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
  - 
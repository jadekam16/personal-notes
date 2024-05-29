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

- The **cat.py** file is a simple unix file that reads the bytes that was given as input.

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
gives you numbers of lines, words etc. in the program 

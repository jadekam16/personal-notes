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
``` 
$ filter < input.txt > output.txt 
$ < input.txt filter > output.txt 
$ < input.txt > output.txt filter
```

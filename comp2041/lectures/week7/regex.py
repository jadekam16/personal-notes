#!/usr/bin/env python3

# python has builtin regex lib called re 
import re
import sys

def main():
  """
  main functions: search, match, fullmatch
  to use: 
      search(pattern, string, flags)

      where pattern is the regex to search for 
      string is the string to search in 
      flags is an optional set of modifiers

  difference:
    search: finds a match anywhere in the string 
      - return object with information about match or `None` if match fails
    match: only find a match at the beginning of the string
    fullmatch: only finds a match at the beginning and end of the string

  additional functions: sub, findall, split
  to use:
      re.sub(regex, replacement, string, count, flags)
      - return string with anywhere regex matches, substituted by replacement
        
      re.findall(regex, string, flags)
      - return all non-overlapping matches of pattern in string
      - if pattern contains () return part matched by ()  
      - if pattern contains multiple () return tuple

      re.split(regex, string, maxsplit, flags)
      - split string everywhere regex matches

  When Python finds a match, it returns the match object - this has a number 
  of useful attributes:
      - Match.span() - starting and ending index of the match
      - Match.group(0) - the entire match
      - Match.group(N) - capture groups 
  """

  email="jadekam@gmail.com"
  match_object=re.search(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email)

  print("=======> Match Object Methods <=======")
  print(match_object)
  print(match_object.span())
  print(match_object.group(0))

  print("=======> Regex Methods <=======")
  # printing the last number of every line
    

if __name__ == "__main__":
  main()
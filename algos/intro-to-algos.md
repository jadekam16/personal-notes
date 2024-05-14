# Characteristics of Algorithms
1. Input (0 or more)
2. Output (at least 1)
3. Definiteness: every statement you write must be clear 
4. Finiteness: algorithm must terminate at some point 
5. Effectiveness: don't write unnecessary statements

# How to write and analyse an algorithm

## Writing
- no need to write language-specific declarations just yet 

e.g.
Algorithm swap (a, b)
  Begin 
    temp := a;
    a := b;
    b := temp;
  End

- you just need to be able to understand it!
- time analysis: each direct statement = 1 unit of time therefore f(n) = 3 --> O(1)
- space analysis: three vars used (a, b, temp) therefore s(n) = 3 --> O(1)

## Analysing: Important Factors 
1. Time: should be time-efficient i.e., faster 
2. Space: need to know how much memory space it will consume
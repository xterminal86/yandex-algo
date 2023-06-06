#!/usr/bin/python3

import sys;

def canSegment(s, wordDict, memo):
  if len(s) == 0:
      return True

  if s in memo:
      return memo[s]
  for word in wordDict:
      if len(word) > len(s):
          break
      if word == s[:len(word)] and canSegment(s[len(word):], wordDict, memo):
          return True
  memo[s] = False
  return False

def wordBreak(s, wordDict):
  memo = {}
  wordDict.sort(key=lambda x: len(x))
  return canSegment(s, wordDict, memo)


if __name__ == "__main__":
  sys.setrecursionlimit(10**6);

  s = input().rstrip();
  n = int(input().rstrip());

  words = [ "" ] * n;

  for i in range(n):
    words[i] = input().rstrip();

  res = wordBreak(s, words);

  if res == True:
    print("YES");
  else:
    print("NO");

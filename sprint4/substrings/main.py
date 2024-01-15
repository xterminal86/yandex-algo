#!/usr/bin/python3

#
# Формат ввода
# Одна строка, состоящая из строчных латинских букв. Длина строки не превосходит
# 10 000.
#
# Формат вывода
# Выведите натуральное число —– ответ на задачу.
#

################################################################################

def FindLongestSubstring(str):
  #print("");
  charsIndices = {};

  start = 0;
  ind = 0;

  maxLen = 0;

  for c in str:
    #print(f"c = { c }");

    if (c in charsIndices):
      start = max(start, charsIndices[c] + 1);

    maxLen = max(maxLen, (ind - start) + 1);
    #print("  maxLen = ", maxLen);

    charsIndices[c] = ind;

    #print(charsIndices);

    ind += 1;

  return maxLen;

################################################################################

def Tests():
  assert( FindLongestSubstring("awe")      == 3);
  assert( FindLongestSubstring("abcabcbb") == 3);
  assert( FindLongestSubstring("bbbbb")    == 1);
  assert( FindLongestSubstring("pwwkew")   == 3);
  assert( FindLongestSubstring("t")        == 1);
  assert( FindLongestSubstring("azx")      == 3);
  assert( FindLongestSubstring("ysmfzgw")  == 7);
  assert( FindLongestSubstring("fprarfpoz") == 6);

################################################################################

def main():
  str = input().rstrip();
  # Tests();
  ln = FindLongestSubstring(str);
  print(ln);

################################################################################

if __name__ == "__main__":
  main();

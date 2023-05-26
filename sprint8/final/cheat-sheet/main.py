#!/usr/bin/python3

################################################################################

def main():
  s = input().rstrip();

  n = int(input().rstrip());

  words = [ "" ] * n;

  for i in range(n):
    words[i] = input().rstrip();

  print(s);
  print(words);

################################################################################

if __name__ == "__main__":
  main();

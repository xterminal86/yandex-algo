#!/usr/bin/python3

import sys;

def main():
  in_ = sys.stdin.readline().rstrip().lower();

  text = "";

  for c in in_:
    if c.isalnum():
      text += c;

  reversed = text[::-1];

  if text == reversed:
    print("True");
  else:
    print("False");

if __name__ == "__main__":
  main();

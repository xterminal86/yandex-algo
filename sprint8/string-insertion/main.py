#!/usr/bin/python3

import sys;

################################################################################

def main():
  s = sys.stdin.readline().rstrip();
  n = int(input().rstrip());

  tasks = [];

  for i in range(n):
    line = sys.stdin.readline().rstrip().split();
    str = line[0];
    pos = int(line[1]);

    tasks.append( (pos, str) );

  tasks.sort();

  from_ = 0;

  lns = len(s);

  for item in tasks:
    upTo = item[0];
    what = item[1];
    print(f"{ s[from_:upTo] }{ what }", end="");
    from_ = upTo;

  if from_ != lns:
    print(f"{ s[from_:] }", end="");

################################################################################

if __name__ == "__main__":
  main();

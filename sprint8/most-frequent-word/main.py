#!/usr/bin/python3

################################################################################

def main():
  n = int(input().rstrip());

  d = {};

  for i in range(n):
    s = input().rstrip();

    if s not in d:
      d[s] = (1, s);
    else:
      d[s] = (d[s][0] + 1, s);

  print(sorted(d.values(), key=lambda x : (-x[0], x[1]))[0][1]);

################################################################################

if __name__ == "__main__":
  main();

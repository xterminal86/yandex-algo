#!/usr/bin/python3

def main():

  line = input().rstrip().split();
  n = int(line[0]);
  k = int(line[1]);

  mod = pow(10, 9) + 7;

  stairs = [ 0 ] * (n + 1);

  stairs[0] = 1;
  stairs[1] = 1;
  stairs[2] = 1 if k == 1 else 2;

  for i in range(3, n):
    sum = 0;
    for j in range(1, k + 1):
      sum += stairs[i - j];
    stairs[i] = (sum % mod);

  print(stairs[n - 1]);

###############################################################################

if __name__ == "__main__":
  main();

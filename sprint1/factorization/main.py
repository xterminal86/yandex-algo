#!/usr/bin/python3

import math;

def main():
  n = int(input().rstrip());

  if n == 1:
    print(n);
    return;

  square = int(math.sqrt(n));

  nWork = n;

  factors = [];

  while True:

    found = False;

    for i in range(2, square + 1):
      if nWork % i == 0:
        factors.append(i);
        nWork = int(nWork / i);
        found = True;
        break;

    if (found == False):
      if (nWork != 1):
        factors.append(nWork);

      break;

  output = "";

  for f in factors:
    output += f"{ f } ";

  output = output[:-1];

  print(output);

if __name__ == "__main__":
  main();

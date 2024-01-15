#!/usr/bin/python3

#
# Формат ввода
# В единственной строке дано число n (2 ≤ n ≤ 10^9), которое нужно факторизовать.
#
# Формат вывода
# Выведите в порядке неубывания простые множители, на которые раскладывается
# число n.
#

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

################################################################################

if __name__ == "__main__":
  main();

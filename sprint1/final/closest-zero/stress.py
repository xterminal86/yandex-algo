#!/usr/bin/python3

import random;

max = pow(10, 9);

with open("stress.txt", "w") as f:
  f.write("1000000\n");

  str = "";

  for i in range(1000000):
    n = random.randrange(0, max);
    str += f"{ n } ";

  str = str[:-1];

  f.write(str);


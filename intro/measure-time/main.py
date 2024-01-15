#!/usr/bin/python3

import time;

#
# Не помню откуда это.
#
def main():
  ts = time.time();
  i = 0;
  while i < 1000000000:
    i += 1;

  tf = time.time();
  dt = tf - ts;

  print(dt, "seconds");

################################################################################

if __name__ == "__main__":
  main();

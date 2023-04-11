#!/usr/bin/python3

def main():
  n = int(input().rstrip());

  bound = 10000;

  power = 0;

  allPowerResults = [];

  value = 1;

  while value < bound:
    allPowerResults.append(value);

    power += 1;

    value = pow(4, power);

  if n in allPowerResults:
    print("True");
  else:
    print("False");

if __name__ == "__main__":
  main();

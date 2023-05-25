#!/usr/bin/python3

################################################################################

def UnpackString(packedString):
  result = "";

  return result;

################################################################################

def main():
  n = int(input().rstrip());

  for i in range(n):
    packedString = input().rstrip();
    s = UnpackString(packedString);

################################################################################

if __name__ == "__main__":
  main();

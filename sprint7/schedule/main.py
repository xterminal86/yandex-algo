#!/usr/bin/python3


###############################################################################

def main():
  n = int(input().rstrip());

  lessons = [];

  for i in range(n):
    line = input().split();
    lessons.append( (float(line[0]), float(line[1])) );

  print(lessons);

###############################################################################

if __name__ == "__main__":
  main();

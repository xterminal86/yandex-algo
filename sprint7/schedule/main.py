#!/usr/bin/python3

################################################################################

def main():
  n = int(input().rstrip());

  lessons = [];

  for i in range(n):
    line = input().split();
    lessons.append( (float(line[0]), float(line[1])) );

  #print(lessons);
  #print("-"*80);

  lessons.sort(key=lambda x : (x[1], x[0]));

  #print(lessons);

  ans = [ lessons[0] ];

  ln = len(lessons);

  chain = lessons[0];

  for i in range(1, ln):
    if lessons[i][0] >= chain[1]:
      ans.append(lessons[i]);
      chain = lessons[i];

  print(len(ans));

  for item in ans:
    print("{:g} {:g}".format(item[0], item[1]));

###############################################################################

if __name__ == "__main__":
  main();

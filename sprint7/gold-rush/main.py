#!/usr/bin/python3

import heapq;

################################################################################

def main():
  capacity = int(input().rstrip());
  piles = int(input().rstrip());
  data = [];
  for i in range(piles):
    line = input().rstrip().split();
    c = int(line[0]);
    m = int(line[1]);
    data.append( (-c, m) );

  heapq.heapify(data);

  ans = 0;

  stop = False;

  while stop == False:
    if len(data) == 0:
      break;

    item = heapq.heappop(data);

    c = abs( item[0] );
    n = abs( item[1] );

    capacity -= n;

    if capacity >= 0:
      ans += c * n;
    else:
      ans += (c * n) - (-capacity * c);
      stop = True;

  print(ans);

################################################################################

if __name__ == "__main__":
  main();

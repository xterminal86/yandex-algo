#!/usr/bin/python3

import sys;

################################################################################

def main():
  kids         = int(input().rstrip());
  greedFactors = list( map(int, sys.stdin.readline().rstrip().split()) );
  cookies      = int(input().rstrip());
  cookieSizes  = list( map(int, sys.stdin.readline().rstrip().split()) );

  gfs = sorted(greedFactors);
  css = sorted(cookieSizes);
    
  greedInd   = len(gfs) - 1;
  cookiesInd = len(css) - 1;
  
  satisfaction = 0;
  
  while True:
    if (greedInd < 0) or (cookiesInd < 0):
      break;

    maxGreed      = gfs[greedInd];
    maxCookieSize = css[cookiesInd];
  
    if (maxGreed <= maxCookieSize):
      greedInd     += -1;
      cookiesInd   += -1;
      satisfaction += 1;
    else:
      greedInd += -1;    

  print(satisfaction);

################################################################################

if __name__ == "__main__":
  main();

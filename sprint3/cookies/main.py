#!/usr/bin/python3

#
# Формат ввода
# В первой строке записано n —– количество детей.
#
# Во второй —– n чисел, разделённых пробелом, каждое из которых –— фактор
# жадности ребёнка. Это натуральные числа, не превосходящие 1000.
#
# В следующей строке записано число m –— количество печенек.
#
# Далее —– m натуральных чисел, разделённых пробелом —– размеры печенек.
# Размеры печенек не превосходят 1000.
#
# Оба числа n и m не превосходят 10000.
#
# Формат вывода
# Нужно вывести одно число –— количество детей, которые останутся довольными
#

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

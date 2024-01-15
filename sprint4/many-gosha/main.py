#!/usr/bin/python3

#
# Формат ввода
# В первой строчке через пробел записаны два натуральных числа n и k.
#
# Во второй строчке записана строка, состоящая из маленьких латинских букв.
# Длина строки 1 ≤ L ≤ 10^6.
#
# n ≤ L, k ≤ L.
#
# Формат вывода
# Для каждой найденной подстроки выведите индекс начала её первого вхождения
# (нумерация в строке начинается с нуля).
#
# Выводите индексы в любом порядке, в одну строку, через пробел.
#

import sys;

################################################################################

def CalculatePrefixHashes(s, a, mod):
  ln = len(s);
  ph = [0] * (ln + 1);

  for i in range(1, ln + 1):
    ph[i] = (ph[i - 1] * a + ord(s[i - 1])) % mod;

  return ph;

################################################################################

def main():
  base  = 345;
  mod   = 5608713984039443;

  spl = input().rstrip().split();
  n = int(spl[0]);
  k = int(spl[1]);
  s = sys.stdin.readline().rstrip();

  ph = CalculatePrefixHashes(s, base, mod);

  ln = len(s);

  power = pow(base, n, mod);

  ans = {};

  for i in range(ln - n + 1):
    l = i;
    r = l + n;

    hl = ph[l];
    hr = ph[r];

    h = ((hr + mod) - (hl * power)) % mod;

    if h in ans:
      ans[h][1] += 1;
    else:
      ans[h] = [ l, 1 ];

  out = [];

  for key,value in ans.items():
    if (value[1] >= k):
      out.append(value[0]);

  print(*out);

################################################################################

if __name__ == "__main__":
  main();

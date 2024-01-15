#!/usr/bin/python3

#
# Формат ввода
# В единственной строке дано целое число n (0 ≤ n ≤ 10^6).
#
# Формат вывода
# Вычислите значение Fn по модулю 10^9 + 7 и выведите его.
#

def Fib(n):
  if (n == 0) or (n == 1):
    return 1;

  a = 1;
  b = 1;

  mod = pow(10, 9) + 7;

  for i in range(2, n + 1):
    a = (a + b) % mod;
    a, b = b, a;

  return b;

################################################################################

def main():
  n = int(input().rstrip());

  print(Fib(n));

################################################################################

if __name__ == "__main__":
  main();

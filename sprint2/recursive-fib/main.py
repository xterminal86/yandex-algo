#!/usr/bin/python3

#
# Формат ввода
# На вход подаётся n — целое число в диапазоне от 0 до 32
#
# Формат вывода
# Нужно вывести F(n)
#
def main():
  n = int(input().rstrip());

  if (n == 0) or (n == 1):
    print(1);
    return;
  
  ans = 0;

  history = [1, 1, 0];

  ind = 0;
  
  for i in range(2, n + 1):
    history[2] = history[0] + history[1];
    history[0] = history[1];
    history[1] = history[2];    

  print(history[2]);

#################################################################################

if __name__ == "__main__":
  main();
  

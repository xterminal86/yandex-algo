#!/usr/bin/python3

#
# Формат ввода
# В первой строке дано число n (1 ≤ n ≤ 10^5). Затем по одной на строке даны n
# строк, каждая не превышает 10^5 в длину. Суммарная длина всех строк не
# превосходит 10^7.
#
# Формат вывода
# Выведите единственное число — длину наибольшего префикса всех данных строк.
#

################################################################################

def main():
  n = int(input().rstrip());

  strings = [];

  maxLen = 10**5;

  for i in range(n):
    s = input().rstrip();
    ln = len(s);

    if ln < maxLen:
      maxLen = ln;

    strings.append(s);

  counter = 0;

  for i in range(maxLen):
    ch = strings[0][i];
    for j in range(1, n):
      if ch != strings[j][i]:
        print(counter);
        return;

    counter += 1;

  print(counter);

################################################################################

if __name__ == "__main__":
  main();

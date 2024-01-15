#!/usr/bin/python3

#
# Формат ввода
# В первой строке дано число вершин n (1 ≤ n ≤ 10^5) и число рёбер
# m (0 ≤ m ≤ 5 * 10^5). В следующих m строках записаны рёбра в виде пар вершин
# u и v (1 ≤ u, v ≤ n).
#
# Формат вывода
# Если граф является полным, выведите «YES», иначе выведите «NO».
#

################################################################################

def main():
  line = input().rstrip().split();
  vertices = int(line[0]);
  edges    = int(line[1]);

  counter = [ None ] * (vertices + 1);

  for i in range(1, vertices + 1):
    counter[i] = set();

  for i in range(edges):
    line = input().rstrip().split();
    f = int(line[0]);
    t = int(line[1]);

    if f != t:
      counter[f].add(t);
      counter[t].add(f);

  for item in counter:
    if item != None:
      if len(item) != (vertices - 1):
        print("NO");
        return;

  print("YES");

################################################################################

if __name__ == "__main__":
  main();

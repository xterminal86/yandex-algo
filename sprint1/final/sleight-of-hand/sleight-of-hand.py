#!/usr/bin/python3

# contest id = 83947973

#
# Формат ввода
# В первой строке дано целое число k (1 ≤ k ≤ 5).
#
# В четырёх следующих строках задан вид тренажёра -— по 4 символа в каждой
# строке. Каждый символ – либо точка, либо цифра от 1 до 9. Символы одной строки
# идут подряд и не разделены пробелами.
#
# Формат вывода
# Выведите единственное число -— максимальное количество баллов, которое смогут
# набрать Гоша и Тимофей.
#

import sys;

def main():
  fingers = int(input().rstrip()) * 2;
  
  numbersCount = [0] * 10;
  
  for i in range(4):
    line = sys.stdin.readline().rstrip();
    
    for c in line:
      if c != ".":
        ind = int(c) - 1;
        numbersCount[ind] += 1;
  
  score = 0;
  
  for t in range(10):
    if (numbersCount[t] != 0 and numbersCount[t] <= fingers):
      score += 1;
      
  print(score);

################################################################################

if __name__ == "__main__":
  main();

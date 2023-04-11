#!/usr/bin/python3

# contest id = 84452734
#
# Убираем данные в класс для удобства и красивости кода,
# затем переопределяем оператор < в соответствии с условием задачи
# для обеспечения корректности сортировки.
#
# Сложность - как у обычного quicksort'а, O( n * log(n) ) в среднем по палате,
# плюс некоторый выигрыш на отсутствие необходимости копировать отсортированные
# данные в новый массив.
# Ну и естественно на рекурсию жрётся память.
#

################################################################################

class Person:
  _login = "";

  _score   = 0;
  _penalty = 0;

  # ----------------------------------------------------------------------------

  def __init__(self, login, score, penalty):
    self._login = login;
    self._score = score;
    self._penalty = penalty;

  # ----------------------------------------------------------------------------

  def __lt__(self, other):
    if (self._score > other._score):
      return True;
    elif (self._score == other._score):
      if (self._penalty < other._penalty):
        return True;
      elif (self._penalty == other._penalty):
        if (self._login < other._login):
          return True;
        else:
          return False;
      else:
        return False;
    else:
      return False;

  # ----------------------------------------------------------------------------

  def __repr__(self):
    return repr(
      f"<'{ self._login }' "
      f"{ self._score } "
      f"{ self._penalty }>"
    );

################################################################################

def QuickSort(ar, start, end):
  if (end - start) > 0:
    print(f"sorting { ar }");
    print(f"start = { start }, end = { end }");
    pivot, i = start, start;
    print(f"pivot = { pivot }, i = { start }");
    while (i < end):
      if ar[i] < ar[end]:
        print(f"    ar[i] ({ ar[i] }) < ar[end] ({ ar[end] })");
        print(f"    swap: ar[pivot] ({ ar[pivot] }) <=> ar[i] ({ ar[i] })");
        ar[pivot], ar[i] = ar[i], ar[pivot];
        print(f"    now: { ar }");
        print("    pivot += 1");
        pivot += 1;
      print(f"  i += 1");
      i += 1;
    print(f"  swap ar[end] ({ ar[end] }) <=> ar[pivot] ({ ar[pivot] })");
    ar[end], ar[pivot] = ar[pivot], ar[end];
    QuickSort(ar, start, pivot - 1);
    QuickSort(ar, pivot + 1, end);
  else:
    print("(end - start) <= 0");

################################################################################

def main():
  n = int(input().rstrip());

  data = [];

  for i in range(n):
    line = input().rstrip().split();
    p = Person(line[0], int(line[1]), int(line[2]));
    data.append(p);

  d = [ 7, 6, 1, 8, 5 ];
  QuickSort(d, 0, len(d) - 1);
  print(d);

  #QuickSort(data, 0, len(data) - 1);

  #for item in data:
  #  print(item._login);

################################################################################

if __name__ == "__main__":
  main();

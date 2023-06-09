# contest id = 84327734

# Идея в том, чтобы модифицировать бинарный поиск под условие задачи.
# Поскольку массив уже отсортирован, в нём нет повторяющихся значений
# и он лишь сдвинут, то можно подшаманить бинарный поиск, чтобы он выбирал
# нужную половину для поиска.
#
# Возьмём для примера массив:
#
# [ 0 1 2 3 4 ]
#
# и будем искать тройку.
#
# Соответственно у нас может быть два варианта:
#
# 1. Левая граница меньше середины. Это значит, что этот кусок не сдвинут.
#
# [ 2 3 4 0 1 ]
#   l   m   r
#
# Теперь надо проверить входит ли в этот диапазон искомое значение.
# Если да, то можно выкинуть правую часть массива.
# В противном случае выкидываем левую часть.

# 2. Левая граница больше середины. Аналогично предыдущей.
#
# [ 4 0 1 2 3 ]
#   l   m   r
#
# Смотрим, отсортирована ли правая часть, проверяем, входит ли искомое
# значение в правую часть.
# Если нет, то выкидываем и ищем в левой.
# В противном случае в правой.
#
# Сложность - O( log(n) ) т.к. это по прежнему бинарный поиск.
# Сложность двух дополнительных проверок можно считать нулевой.
#

################################################################################

def BinarySearch(array, x):
  left  = 0;
  right = len(array) - 1;

  while (left <= right):
    m = left + (right - left) // 2;

    print(array);
    print(f"  left = { left } right = { right } m = { m }");

    if (array[m] == x):
      return m;

    if (array[m] >= array[left]):
      if (x <= array[m]) and (x >= array[left]):
        right = m - 1;
        print("  right = m - 1");
      else:
        print("  left = m + 1");
        left = m + 1;
    else:
      if (x >= array[m]) and (x <= array[right]):
        print("  left = m + 1");
        left = m + 1;
      else:
        print("  right = m - 1");
        right = m - 1;

  return -1;

################################################################################

def broken_search(nums, target) -> int:
  return BinarySearch(nums, target);

#assert(broken_search([ 0, 1, 2, 3, 4 ], 3) == 3);
assert(broken_search([ 2, 3, 4, 0, 1 ], 3) == 1);
#assert(broken_search([ 3, 4, 0, 1, 2 ], 500) == -1);
#!/usr/bin/python3
#
# Формат ввода
# В первой строке вводится число предметов n, не превышающее 100 и
# грузоподъемность M, не превышающая 10^4.
#
# Далее следуют описания предметов по одному в строке. Каждый предмет
# описывается парой mi, ci, оба числа не превосходят 100 по модулю.
#
# Формат вывода
# Выведите в первой строке единственное число — сколько предметов надо взять.
# Во второй строке перечислите их номера (нумерация с единицы). Если ответов
# несколько, то выведите любой.
#
# Одна из классических задач, известная под названием "0/1 knapsack problem".
# 0/1 означает, что предметы, которые мы кладём в рюкзак, неделимые.
# Т.е. мы можем либо положить предмет, либо нет, мы не можем положить
# часть предмета.
#
# Задача формулируется следующим образом: есть рюкзак вместимостью C,
# и есть набор предметов, каждый из которых обладает определённым весом W
# и некоей "ценностью" V. Необходимо определить какие предметы нужно положить
# в рюкзак, чтобы суммарная ценность предметов была максимальной, при этом
# принимая во внимание максимально возможную вместимость рюкзака.
#
# Очевидно, что для N предметов существует 2^N возможных решений, при этом
# какие-то из них подойдут, а какие-то нет, т.к. не поместятся в рюкзак.
#
# Идея состоит в том, чтобы решить проблему для базовых случаев,
# а потом использовать их как хинты для последующих.
#
# Пусть у нас есть рюкзак вместимостью 5.
# И есть 4 предмета, задаваемых парой (вес, ценность):
#
# 1. (5, 60)
# 2. (3, 50)
# 3. (4, 70)
# 4. (2, 30)
#
# Составим таблицу, где все возможные веса от 0 до вместимости будут идти
# в колонках, а предметы в строках. Тогда в ячейке будет находиться оптимальная
# ценность рюкзака с весом соответствующей колонки. Соответственно,
# поскольку нас интересует максимальная вместимость рюкзака, то наш ответ будет
# находиться в правом нижнем углу таблицы. Распространённый подход к решению
# данной задачи (как и многих других задачи из области динамического
# программирования) подразумевает перевод индексации с 0 на 1 для первого
# элемента, и заполнение нулевых строк и столбцов какими-то значениями,
# необязательно нулями.
# Это не являетcя какой-то магией, а делается исключительно для упрощения
# расчётов в коде, грубо говоря, чтобы не обмазываться везде проверками на выход
# за границу массива. При желании можно адаптировать решение под "классическую"
# индексацию. В данном примере будем использовать рекомендованный подход с
# нумерацией с единицы. Это также позволяет в дальнейшем упростить нахождение
# ответа.
#
#  возможные веса рюкзака
#      0 1 2 3 4 5
#    0
# пр 1
# ед 2
# ме 3
# ты 4
#
# Заполняем нулевую строку и столбец нулями, т.к. в рюкзак вместимостью 0
# мы можем положить 0 предметов из N. Аналогично в рюкзак любой вместимости
# можно положить 0 предметов из 0.
#
#    0 1 2 3 4 5
#  0 0 0 0 0 0 0
#  1 0
#  2 0
#  3 0
#  4 0
#
# Теперь берём первый предмет - (5, 60). До веса 5 мы не можем положить его,
# поэтому значение ценности в ячейках 0 - 4 будет равно 0. И только в 5-й ячейке
# будет записано значение ценности данного предмета - 60.
#
#    0 1 2 3 4 5
#  0 0 0 0 0 0 0
#  1 0 0 0 0 0 60
#  2 0
#  3 0
#  4 0
#
# Таким образом мы рассмотрели решение задачи для одного предмета.
# Теперь добавляем в рассмотрение второй предмет - (3, 50).
# Его вес 3, значит мы не можем доложить его в рюкзак пока его вместимость
# не станет равной трём. Поэтому берём лучший результат из предыдущего решения
# данной проблемы - т.е. из предыдущей строки, там где мы помещали первый предмет.
# Однако как только мы достигли веса 3 у нас появляются варианты. Мы можем либо
# положить данный (т.е. второй) предмет в рюкзак, либо не класть его.
# Если мы кладём второй предмет в рюкзак, то наш вес уменьшается на вес предмета
# и мы должны посмотреть можем ли мы ещё доложить в оставшееся место (если оно
# конечно есть) наилучший вариант с предыдущего шага? Для этого идём в
# предыдущую строку и отсчитываем влево столько колонок, сколько весит наш
# предмет, который мы только что положили (первый пример почему в данных задачах
# смещается индексация с 0 на 1). В нашем примере это будет 3, т.е.
# мы идём в ячейку [1, 3] и отсчитываем 3 от колонок и приходим в [1, 0].
# Т.е. мы смотрим лучшее решение для рюкзака вместимостью 0. Но поскольку там 0,
# то ничего не добавляется.
# Если же мы не кладём второй предмет, то это значит, что мы переносим лучшее
# решение с предыдущего шага в этот, т.е. наш вес рюкзака не изменился, но и
# стоимость также, т.к. мы приняли решение не класть второй предмет, т.е.
# стоимость не выросла. А значит надо взять наилучший вариант с предыдущего шага.
# Таким образом алгоритм получается следующий: для рассматриваемой ячейки
# выбрать максимальную ценность между предыдущим вариантом для данного веса,
# и (текущий предмет) + (лучший вариант для рюкзака с весом, который останется
# после того как мы положим текущий предмет).
# В нашем примере получается для второго предмета мы выбираем между 50 и 0.
# Поскольку 50 больше, то записываем 50.
#
#    0 1 2 3  4 5
#  0 0 0 0 0  0 0
#  1 0 0 0 0  0 60
#  2 0 0 0 50
#  3 0
#  4 0
#
# Переходим в следующую колонку с весом 4. Опять у нас есть варианты.
# Смотрим: кладём текущий предмет, получается 4 - 3 = 1. Значит надо ещё
# посмотреть не было ли найдено решение для рюкзака с весом 1.
#
# [2, 4] -> [1, 4] -> [1, 1] = 0
#
# Нет, тут по-прежнему 0, так что никакой дополнительной ценности нет.
# Если не класть второй предмет, то лучшее решение с предыдущего шага тоже 0,
# поэтому пишем 50.
#
#    0 1 2 3  4  5
#  0 0 0 0 0  0  0
#  1 0 0 0 0  0  60
#  2 0 0 0 50 50
#  3 0
#  4 0
#
# Теперь мы в колонке для веса 5. Теперь есть новая информация: мы можем
# не класть второй предмет и взять вместо этого вариант с предыдущего шага с
# ценностью 60, либо попробовать положить второй предмет и посмотреть можно ли
# засунуть что-нибудь ещё. Отматываем назад, получается:
#
# [2, 5] -> [1, 5] -> [1, 2] = 0
#
# Ничего нового, поэтому между 50 и 60 выбираем 60.
#
#    0 1 2 3  4  5
#  0 0 0 0 0  0  0
#  1 0 0 0 0  0  60
#  2 0 0 0 50 50 60
#  3 0
#  4 0
#
# Ключевой момент: мы "раскручиваем" решение благодаря тому, что наша основная
# проблема (собрать рюкзак максимальной ценности) разбивается на подпроблемы.
# Сначала мы решаем проблему рюкзака для минимально возможных случаев,
# а потом используем эти результаты для быстрого поиска ответа на последующие.
# При переходе к следующему предмету, мы рассматриваем его и все предыдущие,
# но поскольку решение для предыдущих уже найдено путём раскрутки, то ответ
# для данного нового предмета ищется быстро. По крайней мере быстрее чем 2^N.
#
# Добавляем третий предмет (4, 70).
# Аналогично, до веса 4 мы просто переносим результаты с предыдущих шагов
# для соответствующего веса, т.к. предмет с весом 4 в них не участвует.
# Для веса 4 есть два стула: 70 + ([1, 0] = 0) и 50 с предыдущего шага.
# Берём 70.
#
#    0 1 2 3  4  5
#  0 0 0 0 0  0  0
#  1 0 0 0 0  0  60
#  2 0 0 0 50 50 60
#  3 0 0 0 50 70
#  4 0
#
# Для веса 5 имеем 70 + 0 и 60. Берём 70.
#
#    0 1 2 3  4  5
#  0 0 0 0 0  0  0
#  1 0 0 0 0  0  60
#  2 0 0 0 50 50 60
#  3 0 0 0 50 70 70
#  4 0
#
# Идём дальше. Четвёртый предмет (2, 30).
#
#    0 1 2  3  4  5
#  0 0 0 0  0  0  0
#  1 0 0 0  0  0  60
#  2 0 0 0  50 50 60
#  3 0 0 0  50 70 70
#  4 0 0 30
#
# Для веса 3 имеем: 30 + 0 и 50. Берём 50.
#
#    0 1 2  3  4  5
#  0 0 0 0  0  0  0
#  1 0 0 0  0  0  60
#  2 0 0 0  50 50 60
#  3 0 0 0  50 70 70
#  4 0 0 30 50
#
# Для веса 4 имеем: 30 + 0 и 70. Берём 70.
#
#    0 1 2  3  4  5
#  0 0 0 0  0  0  0
#  1 0 0 0  0  0  60
#  2 0 0 0  50 50 60
#  3 0 0 0  50 70 70
#  4 0 0 30 50 70
#
# И наконец для веса 5 имеем: 30 + 50 = 80 и 70. Берём 80, т.е. кладём четвёртый
# предмет и докладываем в рюкзак с оставшейся вместимостью 4 - 2 = 3 наилучший
# результат для рюкзака этого веса, т.е. [4, 5] -> [3, 5] -> [3, 3] = 50.
#
#    0 1 2  3  4  5
#  0 0 0 0  0  0  0
#  1 0 0 0  0  0  60
#  2 0 0 0  50 50 60
#  3 0 0 0  50 70 70
#  4 0 0 30 50 70 80
#
# Таким образом, оптимальный рюкзак будет иметь ценность 80.
# Но ценность не особо интересна сама по себе, наибольший интерес составляют
# предметы, которые туда положили. Это очень легко восстановить, если идти
# с правой нижней ячейки, т.е. с ячейки ответа. Надо всего навсего проверить,
# является ли значение в данной ячейке перенесённым с предыдущего шага, т.е.
# равно ли значение в данной ячейке значению в ячейке в предыдущей строке.
# Если да, то это значит, что мы пришли в рассматриваемую ячейку оттуда,
# и следовательно не положили данный предмет (т.е. тот, который равен текущей
# строке).
# Если же значение не равны, то это значит, что мы пришли в текущую ячейку из
# предыдущей с отмоткой. Т.е. мы положили предмет с индексом текущей строки,
# плюс доложили то, что осталось в оставшееся место с предыдущего шага.
# Таким образом алгоритм восстановления предметов выглядит следующим образом:
#
# i = n;
# j = C;
#
# Пока (i > 0) и (j > 0):
#   Если dp[i][j] == dp[i - 1][j]:
#     i--;
#   Иначе:
#     answer.append(i);
#     j -= item[i].weight;
#     i--;
#
# Таким образом, в примере ответом будут предметы 4 и 2.
#

################################################################################

def PrintMatrix(mtx):
  for line in mtx:
    print(line);

################################################################################

def main():
  line = input().rstrip().split();

  n        = int(line[0]);
  capacity = int(line[1]);

  weights = [ 0 ] * (n + 1);
  values  = [ 0 ] * (n + 1);

  dp = [ [0 for x in range(capacity + 1)] for y in range(n + 1)];

  for i in range(1, n + 1):
    line = input().rstrip().split();
    m = int(line[0]);
    c = int(line[1]);

    weights[i] = m;
    values[i]  = c;

  #print("weights = ", weights);
  #print("values  = ", values);
  #print("-"*80);

  for i in range(n + 1):
    #print(f"i = { i }");
    for w in range(capacity + 1):
      if (i == 0) or (w == 0):
        dp[i][w] = 0;
      elif weights[i] <= w:
        #print(f"  i = { i } w = { w } weights[i] = { weights[i] } (w - weights[i]) = { w - weights[i] }");
        #print(f"  values[i] = { values[i] }");
        dp[i][w] = max(values[i] + dp[i - 1][ w - weights[i] ], dp[i - 1][w]);
      else:
        dp[i][w] = dp[i - 1][w];

    #PrintMatrix(dp);
    #print("-"*80);

  #PrintMatrix(dp);

  i = n;
  j = capacity;

  ans = [];

  while (i > 0) and (j > 0):
    if (dp[i][j] == dp[i - 1][j]):
      i += -1;
    else:
      ans.append(i);
      j = j - weights[i];
      i += -1;

  print(len(ans));
  print(*ans);

################################################################################

if __name__ == "__main__":
  main();

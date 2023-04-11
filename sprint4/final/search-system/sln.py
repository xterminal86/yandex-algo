#!/usr/bin/python3

# contest id = 85177624

# Задание отстой (по крайней мере в моём случае для питона), т.к. чтобы влезть
# в лимиты приходится делать неструктурированное решение.
# Подобный подход приводит к созданию трудноподдерживаемого кода.
#
# Временная сложность наверное не быстрее O(N+M+K),
# где K - кол-во уникальных слов в "документах".
#
# Пространственная - трудно оценить, т.к. тут словарь словарей,
# промежуточный словарь-счётчик для последующего формирования ответа,
# плюс массив для формирования ответа.
# По факту получается, условно,
# sizeof(docsByWords) + sizeof(toSort) + 2 * sizeof(output)
# если предполагать, что toSort и output (как и outSorted) остаются на своих
# местах в управляемой куче.

import sys;
import heapq;

################################################################################

def SortPair(first, second):
  if (second[0] > first[0]):
    return 1;
  elif (second[0] == first[0]):
    if (second[1] < first[1]):
      return 1;

  return -1;

################################################################################

def main():
  outputLimit = 5;

  n = int(input().rstrip());

  docsByWords = {};

  for i in range(n):
    line = sys.stdin.readline().rstrip().split();

    for word in line:
      if word not in docsByWords:
        docsByWords[word] = { i : 1 };
      else:
        if i in docsByWords[word]:
          docsByWords[word][i] += 1;
        else:
          docsByWords[word].update({ i : 1 });

  m = int(input().rstrip());

  for i in range(m):
    line = sys.stdin.readline().rstrip().split();
    query = set(line);

    toSort = {};

    for word in query:
      if word in docsByWords:
        for i, d in docsByWords[word].items():
          if i not in toSort:
            toSort[i] = d;
          else:
            toSort[i] += d;

    output = [];

    for docId, rel in toSort.items():
      output.append((rel, docId));

    #
    # В питоне кортежи сортируются поэлементно: сначала первые элементы,
    # в случае равенства вторые, в случае их равенства третьи и т.д.
    # Минус перед элементом означает сортировать в обратном порядке.
    # Таким образом у нас получается сортировка в обратном порядке по первому
    # элементу кортежа (релевантности) и в прямом по второму (номеру документа),
    # что нам и надо.
    #
    out = heapq.nsmallest(5, output, key=lambda x : ( -x[0], x[1]));

    ans = [];

    for item in out:
      ans.append(item[1] + 1);

    print(*ans);

################################################################################

if __name__ == "__main__":
  main();

#!/usr/bin/python3

# constest id = 88050407

#
# Временная сложность - O(n * m), где n - длина строки,
#                       m - длина остатка строки от рассматриваемой позиции
#                       до конца для поиска по бору. Поиск по бору итеративный,
#                       поэтому его стоимость входит во время работы второго
#                       цикла. Но поскольку по факту у нас всё равно получился
#                       двойной цикл, то время работы квадратичное.
#
# Пространственная - O( sum( len(words) ) + s), где words - кол-во слов словаря,
#                    s - длина массива DP, равная длине исходной строки + 1.
#
#
# Для решения используется динамическое программирование, основная идея которого
# состоит в том, чтобы "раскрутить" решение от некоего базового случая.
# В качестве базового случая в данной задаче используется строка нулевой длины,
# причём взятая с конца.
# Идея состоит в том, чтобы найти цепочку, которая будет составлена от базового
# случая до нулевой позиции массива DP. Если таковая найдётся, то мы можем
# заключить, что исходная строка может быть разбита на слова при помощи данного
# словаря.
#
# Например:
#
# neetcode
# 000000001
#
# neet
# leet
# code
#
# Наша задача выяснить, можем ли мы найти слово из словаря, которое может быть
# пристыковано к индексу базового случая. Если идти с конца строки, то легко
# видеть, что такое слово есть и это слово "code":
#
# neetcode
# 000010001
#
# Аналогично находим слово "neet":
#
# neetcode
# 100010001
#
# Таким образом имеем цепочку:
#
# 100010001
# -   -   -
# 3   2   1
#
# Ответ будет лежать в DP[0] - если нам по итогу работы алгоритма удалось
# записать туда True, значит цепочка собралась.
#
# Можно решить эту задачу "обратным" способом, двигаясь не с конца, а с начала,
# но тогда базовым случаем будет нулевой элемент массива DP, а ответ
# соответственно будет находиться в DP[len(s)].
#
# К сожалению, чтобы влезть в лимиты контеста, мы не можем решать эту задачу
# по-простому через два цикла со слайсами, поэтому будем использовать префиксное
# дерево (бор) для ускорения поиска ответа на вопрос является ли данный кусок
# строки словом из словаря или нет. Для этого сначала добавим все слова словаря
# в бор, а вместо слайсов будем на каждой итерации в рассматриваемой подстроке
# идти по бору и смотреть, не найдётся ли в нём слово от рассматриваемой позиции.
#
# Рассмотрим на примере:
#
# abacaba
#
# abac
# caba
# aba
#
# Префиксное дерево будет иметь вид:
#
#     aba-0
#   /    \
#  O       c-0
#   \
#     caba-0
#
# Далее будем идти с конца и на каждой позиции строки проворачивать поиск в боре.
# Если слово нашлось и следующий за ним элемент на соответстующей позиции в
# массиве DP равен True, значит можно составить звено цепочки, поэтому маркируем
# рассматриваемый элемент массива DP (от индекса которого начинали поиск в боре)
# как True:
#
# abacaba
#
# 00000001
# 00001001 (aba)
# 00011001 (caba)
# 00011001
# 00011001
# 10011001 (aba)
#
# Аналогично брутфорсному решению, эту задачу тоже можно решить "наоборот",
# если двигаться с начала строки и использовать бор с перевёрнутыми словами.
# Тогда поиск от каждой позиции в строке будет идти назад по строке и вперёд по
# "перевёрнутому" бору. Ответ, соответственно, будет также аналогично лежать в
# конце массива DP.
#

import sys;

################################################################################

class Trie:
  _root = {};

  # ----------------------------------------------------------------------------

  def Find(self, word) -> bool:
    head = self._root;
    for char in word:
      if char not in head:
        return False;

      head = head[char];

    if 0 in head:
      return True;

    return False;

  # ----------------------------------------------------------------------------

  def Add(self, string):
    head = self._root;
    ln = len(string);
    for i in range(ln):
      ch = string[i];

      if ch not in head:
        head[ch] = {};

      head = head[ch];

    head.update({ 0 : 0 });

  # ----------------------------------------------------------------------------

  _traverseHead = None;

  def ResetTraverseHead(self):
    self._traverseHead = self._root;

  # ----------------------------------------------------------------------------

  def Traverse(self, ch):
    if ch not in self._traverseHead:
      return False;
    else:
      self._traverseHead = self._traverseHead[ch];
      return True;

  # ----------------------------------------------------------------------------

  def DeleteIntl(self, node, string):
    if len(string) == 0:
      if len(node) != 0:
        return node;
      else:
        return None;

    ch = string[0];
    if ch in node:
      return self.DeleteIntl(node[ch], string[1:]);
    else:
      return node;

  # ----------------------------------------------------------------------------

  def Delete(self, string):
    res = self.DeleteIntl(self._root, string);
    if res == None:
      del self._root[ string[0] ];

  # ----------------------------------------------------------------------------

  def PrintIntl(self, start, indent):
    cur = start;
    spaces = "." * indent;
    if (type(cur) is dict):
      for k,v in cur.items():
        print(f"{ spaces }{ k }");
        self.PrintIntl(cur[k], indent + 2);
        if type(v) is int:
          print("-"*80);

  # ----------------------------------------------------------------------------

  def Print(self):
    print("="*80);
    print("TRIE");
    print("="*80);
    self.PrintIntl(self._root, 0);

  # ----------------------------------------------------------------------------

  def __repr__(self):
    s = (
      f"<class 'Trie' id = { hex( id(self) ).upper().replace('X', 'x') } "
      f"_root = { self._root }>"
    );
    return s;

################################################################################

def PrintDP(dp):
  for item in dp:
    print(1 if (item == True) else 0, end="");
  print("");

################################################################################

def main():
  s = list( input().rstrip() );

  n = int(input().rstrip());

  words = [ "" ] * n;

  t = Trie();

  for i in range(n):
    words[i] = input().rstrip();
    t.Add(words[i]);

  #t.Print();

  dp = [ False ] * (len(s) + 1);

  dp[len(s)] = True;

  for i in range(len(s) - 1, -1, -1):
    t.ResetTraverseHead();
    for j in range(i, len(s)):
      res = t.Traverse(s[j]);

      #
      # Если такой подстроки вообще нет, то идём дальше.
      #
      if res == False:
        break;

      if (0 in t._traverseHead) and (dp[j + 1] == True):
        dp[i] = True;

    #PrintDP(dp);

  if dp[0] == True:
    print("YES");
  else:
    print("NO");

################################################################################

if __name__ == "__main__":
  main();
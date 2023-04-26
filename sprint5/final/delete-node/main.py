#!/usr/bin/python3

# contest id = 86412579
#
# Пространственная сложность - O(1), т.к. мы только свапаем две ноды.
# Аллоцированием временной переменной можно пренебречь.
# Временная - O(2h), где h - высота дерева. Двойка на поиск ноды на замену.
#

import sys;

from typing import Optional

class Node:
  def __init__(self, left=None, right=None, value=0):
    self.right = right
    self.left  = left
    self.value = value

  # --------------------------------------------------------------------------

  def __repr__(self):
    l = None if (self.left  == None) else self.left.value;
    r = None if (self.right == None) else self.right.value;

    return f"< value = { self.value }, left = { l }, right = { r } >";

################################################################################

def PrintTreeIntl(node, level):
  if node != None:
    PrintTreeIntl(node.right, level + 1);
    print(' ' * 2 * level + '-> ' + str(node.value))
    PrintTreeIntl(node.left, level + 1);

################################################################################

def PrintTree(node):
  PrintTreeIntl(node, 0);
  print("="*80);

################################################################################

def FindNodeToReplace(root):
  cur = root;

  while (cur.right != None):
    cur = cur.right;

  return cur;

################################################################################

#
# Будем искать элемент для удаления в дочерних нодах, т.к. мы не можем удалить
# найденную ноду, поскольку у нас нет связи с родительской нодой,
# а нам при удалении надо переназначить связи. Поэтому будем искать элемент
# для удаления рекурсивно и в случае, если он найдётся, связи выставятся
# по цепочке возвратов из рекурсивных вызовов. Также, поскольку требуется
# вернуть новый корень дерева, то в случае ненахождения искомого элемента,
# мы по цепочке возвратов из рекурсии приедем обратно в начало
# и вернём исходный корневой элемент.
#
def RemoveNode(root, key):
  if (root == None):
    return None;

  if (key < root.value):
    root.left = RemoveNode(root.left, key);
  elif (key > root.value):
    root.right = RemoveNode(root.right, key);
  else:
    #
    # Если у ноды 0 или 1 потомок, то её можно спокойно удалить,
    # связав родителя удаляемой ноды с соответствующим ребёнком удаляемой ноды,
    # при этом корректность BST не нарушится.
    #
    if root.left == None:
      tmp = root.right;
      root = None;
      return tmp;
    elif root.right == None:
      tmp = root.left;
      root = None;
      return tmp;

    #
    # Если потомков у искомой ноды 2, то надо найти ноду для замены
    # в соответствии с правилом (либо крайний правый элемент левого поддерева
    # [используется здесь], либо крайний левый элемент правого поддерева).
    # После чего присвоить "удаляемой" ноде значение из ноды на замену,
    # а потом выпилить ноду для замены как листовую.
    # Наверное несколько читерский вариант, т.к. фактического свапа
    # не происходит, и теоретически это может быть проблемой,
    # если операция копирования будет дорогой.
    #
    tmp = FindNodeToReplace(root.left);
    root.value = tmp.value;
    root.left = RemoveNode(root.left, tmp.value);

  return root;

################################################################################

def remove(root, key) -> Optional[Node]:
  res = RemoveNode(root, key);
  return res;

################################################################################

def main():
  n = int(input().rstrip());

  nodes = [ None ] * (n + 1);

  later = [];

  for i in range(n):
    line = list( map(int, sys.stdin.readline().rstrip().split()) );

    ind   = line[0];
    val   = line[1];
    left  = line[2];
    right = line[3];

    if (left == -1) and (right == -1):
      nodes[ind] = Node(None, None, val);
    else:
      later.append([ ind, val, left, right ]);

  while len(later) != 0:
    item = later.pop();

    ind = item[0];
    val = item[1];
    left  = None if (item[2] == -1) else nodes[ item[2] ];
    right = None if (item[3] == -1) else nodes[ item[3] ];

    nodes[ind] = Node(left, right, val);

  PrintTree(nodes[1]);

  toDelete = int(input().rstrip());

  newHead = remove(nodes[1], toDelete);

  PrintTree(newHead);

################################################################################

if __name__ == "__main__":
  main();
#!/usr/bin/python3

#
# Формат ввода
# Напишите функцию, которая определяет, является ли дерево анаграммой.
# На вход подаётся корень дерева.
#
# Инструкцию по работе с Make вы можете найти в конце этого урока
# Формат вывода
# Функция должна вернуть True если дерево является анаграммой. Иначе - False.
#

import sys;

################################################################################

class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.right = right
    self.left = left

################################################################################

def Traverse(root, f):
  if (root == None):
    f.append(-1);
    return;

  Traverse(root.left, f);
  f.append(root.value);
  Traverse(root.right, f);

################################################################################

def solution(root) -> bool:
  PrintTree(root);

  f1 = [];
  f2 = [];

  Traverse(root.left, f1);
  Traverse(root.right, f2);

  f2.reverse();

  print(f1);
  print(f2);
  print(f1 == f2);

  return (f1 == f2);

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

def ReadTree(size) -> Node:
  nodes = [ None ] * size;

  later = [];

  for i in range(size):
    line = sys.stdin.readline().rstrip().split();
    ind = int(line[0]);
    val = int(line[1]);
    left  = line[2];
    right = line[3];

    if (left == "None") and (right == "None"):
      nodes[ind] = Node(val, None, None);
    else:
      later.append([ ind, val, left, right ]);

  while len(later) != 0:
    item = later.pop();

    ind = item[0];
    val = item[1];
    left  = None if (item[2] == "None") else nodes[int(item[2])];
    right = None if (item[3] == "None") else nodes[int(item[3])];

    nodes[ind] = Node(val, left, right);

  return nodes[0];

################################################################################

def main():
  n = int(input().rstrip());

  root = ReadTree(n);

  solution(root);

################################################################################

if __name__ == "__main__":
  main();

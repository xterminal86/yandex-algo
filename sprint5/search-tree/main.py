#!/usr/bin/python3

#
# Формат ввода
# На вход функции подается корень бинарного дерева.
#
# Инструкцию по работе с Make вы можете найти в конце этого урока
# Формат вывода
# Функция должна вернуть True, если дерево является деревом поиска,
# иначе - False.
#

import sys;

class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value;
    self.right = right;
    self.left  = left;

  def __repr__(self):
    l = None if (self.left == None) else hex(id(self.left)).upper().replace('X', 'x');
    r = None if (self.right == None) else hex(id(self.right)).upper().replace('X', 'x');

    return f"< value = { self.value }, left = { l }, right = { r } >";

################################################################################

def FindNode(root, value):
  if (root == None):
    return None;

  if (value < root.value):
    return FindNode(root.left, value);

  if (value == root.value):
    return root;

  if (value > root.value):
    return FindNode(root.right, value);

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

def CheckRoot(rootValue, root, leftDir):
  toProcess = [];

  if (leftDir == True):
    toProcess.append(root.left);
  else:
    toProcess.append(root.right);

  ok = True;

  while len(toProcess) != 0:
    item = toProcess.pop();

    if (item == None):
      continue;

    if (leftDir == True):
      if (item.value >= rootValue):
        ok = False;
        break;
    else:
      if (item.value <= rootValue):
        ok = False;
        break;

    toProcess.append(item.left);
    toProcess.append(item.right);

  return ok;

################################################################################

def solution(root) -> bool:
  toProcess = [];

  toProcess.append(root);

  ok = True;

  rootValue = root.value;

  while len(toProcess) != 0:
    node = toProcess.pop();

    if (node == None):
      continue;

    if (node.left != None):
      if (node.left.value >= node.value):
        ok = False;
        break;

    if (node.right != None):
      if (node.right.value <= node.value):
        ok = False;
        break;

    toProcess.append(node.left);
    toProcess.append(node.right);

  if (ok == False):
    return ok;

  ok = CheckRoot(rootValue, root, True);

  if (ok == True):
    ok = CheckRoot(rootValue, root, False);

  return ok;

################################################################################

def main():
  '''
  node1 = Node(1, None, None);
  node2 = Node(4, None, None);
  node3 = Node(3, node1, node2);
  node4 = Node(8, None, None);
  node5 = Node(5, node3, node4);

  PrintTree(node5);
  assert solution(node5);
  node2.value = 5;
  PrintTree(node5);
  assert not solution(node5);
  '''

  n = int(input().rstrip());

  nodes = [ None ] * n;

  later = [];

  for i in range(n):
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

  PrintTree(nodes[0]);

  res = solution(nodes[0]);

  print(res);

################################################################################

if __name__ == '__main__':
  main();

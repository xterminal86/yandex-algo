#!/usr/bin/python3

import sys;

################################################################################

class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value;
    self.right = right;
    self.left  = left;

  # ----------------------------------------------------------------------------

  def __repr__(self):
    l = None if (self.left == None) else hex(id(self.left)).upper().replace('X', 'x');
    r = None if (self.right == None) else hex(id(self.right)).upper().replace('X', 'x');

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

def Traverse(root, f):
  if (root == None):
    f.append(-1);
    return;

  Traverse(root.left, f);
  f.append(root.value);
  Traverse(root.right, f);

################################################################################

def solution(root1, root2) -> bool:
  PrintTree(root1);
  PrintTree(root2);

  fingerprint1 = [];
  fingerprint2 = [];

  Traverse(root1, fingerprint1);
  Traverse(root2, fingerprint2);

  print(*fingerprint1);
  print(*fingerprint2);

  print(fingerprint1 == fingerprint2);

  return (fingerprint1 == fingerprint2);

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

  root1 = ReadTree(n);

  n = int(input().rstrip());

  root2 = ReadTree(n);

  solution(root1, root2);

################################################################################

if __name__ == '__main__':
  main();
#!/usr/bin/python3

import sys;

################################################################################

class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value;
    self.right = right;
    self.left  = left;

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

Paths = [];

def DrillDown(node, ar):
  global Paths;

  ar.append(node.value);

  if (node.left == None) and (node.right == None):
    copy = ar[:]
    Paths.append(copy);
    return;

  if (node.left != None):
    DrillDown(node.left, ar);
    ar.pop();

  if (node.right != None):
    DrillDown(node.right, ar);
    ar.pop();

################################################################################

def solution(root) -> int:
  global Paths;

  Paths = [];

  lst = [];
  DrillDown(root, lst);

  print(Paths);

  ans = 0;

  for item in Paths:
    rank = len(item) - 1;
    numRes = 0;
    for num in item:
      numRes += num * pow(10, rank);
      rank += -1;
    ans += numRes;

  print(ans);

  return ans;

################################################################################

def main():
  n = int(input().rstrip());
  root = ReadTree(n);
  PrintTree(root);
  solution(root);

################################################################################

if __name__ == "__main__":
  main();
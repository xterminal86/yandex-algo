#!/usr/bin/python3

class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.right = right
    self.left = left

################################################################################

Answer = 0;

def Search(root):
  global Answer;

  if (root == None):
    return;

  if (root.value > Answer):
    Answer = root.value;

  Search(root.left);
  Search(root.right);

################################################################################

def solution(root) -> int:
  global Answer;

  Search(root);

  return Answer;

#
#         2
#        /
#       3
#     /   \
#    1    -5

def test():
  node1 = Node(1)
  node2 = Node(-5)
  node3 = Node(3, node1, node2)
  node4 = Node(2, node3, None)
  assert solution(node4) == 3

if __name__ == '__main__':
  test()


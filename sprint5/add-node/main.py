#!/usr/bin/python3

class Node:
  def __init__(self, left=None, right=None, value=0):
    self.right = right;
    self.left  = left;
    self.value = value;

  # ----------------------------------------------------------------------------

  def __repr__(self):
    l = None if (self.left  == None) else hex(id(self.left)).upper().replace('X', 'x');
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

def InsertNode(root, key):
  if (key < root.value):
    if (root.left == None):
      root.left = Node(None, None, key);
    else:
      InsertNode(root.left, key);
  elif (key >= root.value):
    if (root.right == None):
      root.right = Node(None, None, key);
    else:
      InsertNode(root.right, key);

################################################################################

def insert(root, key) -> Node:
  InsertNode(root, key);
  return root;

################################################################################

def test():
  node1 = Node(None, None, 7);
  node2 = Node(node1, None, 8);
  node3 = Node(None, node2, 7);
  new_head = insert(node3, 6);
  assert new_head is node3;
  assert (new_head.left.value == 6);

if __name__ == '__main__':
    test()
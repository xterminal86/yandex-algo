#!/usr/bin/python3

# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = True;

if LOCAL:
  class Node:  
    def __init__(self, value, nextItem=None):  
      self.Value    = value;
      self.NextItem = nextItem;

#################################################################################
      
def solution(node):
  ptr = node;
  while ptr != None:
    print(ptr.Value);
    ptr = ptr.NextItem;

#################################################################################

def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    solution(node0)
    # Output is:
    # node0
    # node1
    # node2
    # node3

#################################################################################
    
def main():
  test();
  
if __name__ == "__main__":
  main();
  

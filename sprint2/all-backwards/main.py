# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = True

if LOCAL:
    class DoubleConnectedNode:  
        def __init__(self, value, next=None, prev=None):  
            self.value = value  
            self.next = next  
            self.prev = prev

def PrintList(node):
  out = "";

  if node == None:
    return;

  head = node;

  while head != None:    
    if (head.prev == None):
      out += "None";
    else:
      out += f"{ head.prev.value }";

    out += " <- ";

    out += f"{ head.value }";

    out += " -> ";

    if (head.next == None):
      out += "None";
    else:
      out += f"{ head.next.value }";

    out += "\n";
    
    head = head.next;

  print(out);
  
def solution(node):
  res = [];

  head = node;
  
  while head != None:
    res.append(head);
    
    head = head.next;    
  
  last = None;

  newHead = res[-1];
  
  while len(res) != 1:
    prev = res[-1].next;
    
    n = res.pop();
    n.prev = prev;
    n.next = res[-1];
    last = n;

  n = res.pop();
  n.next = None;
  n.prev = last;

  return newHead;

def test():
    node3 = DoubleConnectedNode("node3")
    node2 = DoubleConnectedNode("node2")
    node1 = DoubleConnectedNode("node1")
    node0 = DoubleConnectedNode("node0")

    node0.next = node1

    node1.prev = node0
    node1.next = node2

    node2.prev = node1
    node2.next = node3

    node3.prev = node2

    PrintList(node0);
    
    new_head = solution(node0)

    print("---");
    
    PrintList(new_head);

    assert new_head is node3
    assert node3.next is node2
    assert node2.next is node1 
    assert node2.prev is node3
    assert node1.next is node0 
    assert node1.prev is node2
    assert node0.prev is node1
    

if __name__ == '__main__':
    test()

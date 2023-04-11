#!/usr/bin/python3

import sys;

################################################################################

class MyQueueSized:
  _size  = 0;
  _queue = [];
  
  # ----------------------------------------------------------------------------
  
  def __init__(self, queueSize):
    self._size = queueSize;

  # ----------------------------------------------------------------------------

  def Push(self, x):
    if len(self._queue) == self._size:
      print("error");
      return;

    self._queue.append(x);    

  # ----------------------------------------------------------------------------

  def Pop(self):
    if len(self._queue) == 0:
      print("None");
      return;

    print(self._queue[0]);
    
    self._queue = self._queue[1:];

  # ----------------------------------------------------------------------------

  def Peek(self):
    if len(self._queue) == 0:
      print("None");
      return;

    print(self._queue[0]);

  # ----------------------------------------------------------------------------

  def Size(self):
    return len(self._queue);
  
################################################################################

def main():
  commands  = int(input().rstrip());
  queueSize = int(input().rstrip());

  q = MyQueueSized(queueSize);
  
  for i in range(commands):
    cmd = sys.stdin.readline().rstrip().split();

    if (cmd[0] == "peek"):
      q.Peek();
    elif (cmd[0] == "push"):
      val = int(cmd[1]);
      q.Push(val);
    elif (cmd[0] == "pop"):
      q.Pop();
    elif (cmd[0] == "size"):
      print(q.Size());
    
################################################################################
  
if __name__ == "__main__":
  main();
  

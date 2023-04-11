#!/usr/bin/python3

import sys;

################################################################################

class ListQueue:
  _queue = [];

  # ----------------------------------------------------------------------------
  
  def Get(self):
    if len(self._queue) == 0:
      print("error");
      return;

    print(self._queue[0]);

    self._queue = self._queue[1:];

  # ----------------------------------------------------------------------------

  def Put(self, x):
    self._queue.append(x);

  # ----------------------------------------------------------------------------

  def Size(self):
    return len(self._queue);
    
################################################################################

def main():
  commands  = int(input().rstrip());

  q = ListQueue();
  
  for i in range(commands):
    cmd = sys.stdin.readline().rstrip().split();

    if (cmd[0] == "get"):
      q.Get();
    elif (cmd[0] == "put"):
      val = int(cmd[1]);
      q.Put(val);
    elif (cmd[0] == "size"):
      print(q.Size());
      
################################################################################

if __name__ == "__main__":
  main();
  


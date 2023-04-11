#!/usr/bin/python3

class StackMax:
  _stack  = [];
  _maxVal = None;

  # -----------------------------------------------------------------------------
    
  def Push(self, x):      
    self._stack.append(x);

  # -----------------------------------------------------------------------------

  def Pop(self):
    if len(self._stack) == 0:
      print("error");
      return;
    
    n = self._stack.pop();

    if (n == self._maxVal):
      self._maxVal = None;

  # -----------------------------------------------------------------------------    

  def GetMax(self):
    print(self.FindMax());
  

  # -----------------------------------------------------------------------------
  
  def FindMax(self):
    if (len(self._stack) == 0):
      return None;
    
    val = self._stack[0];

    for i in range(len(self._stack)):
      if (self._stack[i] > val):
        val = self._stack[i];

    return val;

  # -----------------------------------------------------------------------------
  
  def Print(self):
    ln = len(self._stack) - 1;
    while ln >= 0:
      print(self._stack[ln]);
      ln += -1;      

#################################################################################
      
def main():
  s = StackMax();
  
  commands = int(input().rstrip());

  for i in range(commands):
    cmd = input().rstrip().split();

    if cmd[0] == "push":
      val = int(cmd[1]);
      s.Push(val);
    elif cmd[0] == "pop":
      s.Pop();
    elif cmd[0] == "get_max":
      s.GetMax();

#################################################################################
    
if __name__ == "__main__":
  main();
  

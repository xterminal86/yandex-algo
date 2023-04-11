#!/usr/bin/python3

class StackMax:
  _stack    = [];
  _maximums = [];
    
  # -----------------------------------------------------------------------------
    
  def Push(self, x):
    if (len(self._maximums) == 0) or (self._maximums[-1] <= x):
      self._maximums.append(x);
    
    self._stack.append(x);

  # -----------------------------------------------------------------------------

  def Pop(self):
    if len(self._stack) == 0:
      print("error");
      return;
    
    n = self._stack.pop();

    if (n == self._maximums[-1]):
      self._maximums.pop();      

  # -----------------------------------------------------------------------------    

  def GetMax(self):
    if len(self._stack) == 0:
      print("None");
      return;
    
    print(self._maximums[-1]);  
  
  # -----------------------------------------------------------------------------
  
  def Print(self):
    out = ">>\n";
    ln = len(self._stack) - 1;
    while ln >= 0:
      out += f"  { self._stack[ln] }\n";      
      ln += -1;
    out += "<<";
    print(out);

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
  

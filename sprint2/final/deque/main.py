#!/usr/bin/python3

################################################################################

class Deque:
  _maxSize  = 0;
  _size     = 0;
  _buf      = [];
  _headR    = 0;
  _headL    = 0;
  
  # ----------------------------------------------------------------------------
  
  def __init__(self, maxSize):
    self._maxSize = maxSize;

    #
    # size = 3  ->
    # [End] [0][0][0] [Mid] [0][0][0] [End]  ->
    # End + 3 + Mid + 3 + End = 3 * 2 + 1 + 2 = 9 elements
    #
    actualSize  = (maxSize * 2 + 1 + 2);
    
    self._buf   = [None] * actualSize;

    middleIndex = maxSize + 1;
    
    self._headR = middleIndex;
    self._headL = middleIndex;
    
  # ----------------------------------------------------------------------------

  def PushBack(self, x):
    if (self._size == self._maxSize):
      print("error");
      return;
    
    self._buf[self._headR] = x;
    
    self._headR += 1;    
    self._size  += 1;

  # ----------------------------------------------------------------------------

  def PopBack(self):
    if (self._size == 0):
      print("error");
      return;

    self._headR += -1;
    
    res = self._buf[self._headR];
    self._buf[self._headR] = None;
    
    self._size  += -1;

    if (self._size == 0):
      self.ResetHeads();
      
    print(res);
    
  # ----------------------------------------------------------------------------

  def PushFront(self, x):
    if (self._size == self._maxSize):
      print("error");
      return;

    self._headL += -1;
    
    self._buf[self._headL] = x;
    
    self._size += 1;

  # ----------------------------------------------------------------------------

  def PopFront(self):
    if (self._size == 0):
      print("error");
      return;

    res = self._buf[self._headL];
    self._buf[self._headL] = None;
    
    self._headL += 1;
    self._size  += -1;

    if (self._size == 0):
      self.ResetHeads();

    print(res);

  # ----------------------------------------------------------------------------

  def ResetHeads(self):
    self._headR = self._maxSize + 1;
    self._headL = self._maxSize + 1;
    
  # ----------------------------------------------------------------------------

  def Print(self):
    actualSize = self._maxSize * 2 + 1;

    decor = "-"*80;
    
    print(decor);
    print("DEQUE STATE");
    print(decor);

    ind = 0;
    
    for i in self._buf:
      s = f"{ ind }. { i }";      

      if (self._headR == ind and self._headL == ind):
        s += " <= HEAD_R HEAD_L";
      elif (self._headR == ind):
        s += " <= HEAD_R";
      elif (self._headL == ind):
        s += " <= HEAD_L";
      
      print(s);
        
      ind += 1;

    print(decor);
    print("");
    
################################################################################

def ProcessCommand(cmd, myDeque):  
  spl = cmd.split();
  print(spl);
  if (spl[0] == "push_back"):
    val = int(spl[1]);
    myDeque.PushBack(val);

  if (spl[0] == "pop_back"):
    myDeque.PopBack();

  if (spl[0] == "push_front"):
    val = int(spl[1]);
    myDeque.PushFront(val);

  if (spl[0] == "pop_front"):
    myDeque.PopFront();

  myDeque.Print();
  
################################################################################

def main():
  n         = int(input().rstrip());
  dequeSize = int(input().rstrip());

  d = Deque(n);

  d.Print();
  
  for i in range(n):
    cmd = input().rstrip();
    ProcessCommand(cmd, d);  

################################################################################
  
if __name__ == "__main__":
  main();
  

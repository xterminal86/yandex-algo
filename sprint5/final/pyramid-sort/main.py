#!/usr/bin/python3

# contest id = 86487542

# Реализовано на основе псевдокода в теоретическом блоке,
# плюс дополнительный код для printf дебага и прочего.
# Компаратор скопипащен из задачи по сортировке в финалке 3-го спринта.

# Временная сложность - O(nlogn)
# Пространственная    - O(n)

import sys;
import math;

from io import StringIO;

################################################################################

class Person:
  _login   = "";
  _score   = 0;
  _penalty = 0;

  # ----------------------------------------------------------------------------

  def __init__(self, login, score, penalty):
    self._login   = login;
    self._score   = score;
    self._penalty = penalty;

  # ----------------------------------------------------------------------------

  def __lt__(self, other):
    if (self._score > other._score):
      return True;
    elif (self._score == other._score):
      if (self._penalty < other._penalty):
        return True;
      elif (self._penalty == other._penalty):
        if (self._login < other._login):
          return True;
        else:
          return False;
      else:
        return False;
    else:
      return False;

  # ----------------------------------------------------------------------------

  def __repr__(self):
    s = (
      f"< class = 'Person' id = { hex( id(self) ).upper().replace('X', 'x') }\n"
      f"  login   = '{ self._login }'\n"
      f"  score   = { self._score }\n"
      f"  penalty = { self._penalty }\n"
      f">\n"
    );

    return s;

  # ----------------------------------------------------------------------------

  def GetShortRepr(self):
    return f"<'{ self._login }' { self._score } { self._penalty }>";

################################################################################

class MyHeap:
  _data = [ None ];

  # ----------------------------------------------------------------------------

  def __init__(self, lst):
    self._data = [ None ];

    for item in lst:
      self.Add(item);

  # ----------------------------------------------------------------------------

  def Empty(self):
    return len(self._data) == 1;

  # ----------------------------------------------------------------------------

  def SiftDown(self, idx):
    left  = 2 * idx;
    right = 2 * idx + 1;

    ln = len(self._data) - 1;

    if (left > ln):
      return;

    if (right <= ln) and (self._data[left] > self._data[right]):
      indLargest = right;
    else:
      indLargest = left;

    if (self._data[idx] > self._data[indLargest]):
      self._data[idx], self._data[indLargest] = self._data[indLargest], self._data[idx];
      return self.SiftDown(indLargest);

  # ----------------------------------------------------------------------------

  def SiftUp(self, idx):
    if (idx == 1):
      return;

    parentIndex = idx // 2;

    if (self._data[idx] < self._data[parentIndex]):
      self._data[parentIndex], self._data[idx] = self._data[idx], self._data[parentIndex];
      self.SiftUp(parentIndex);

  # ----------------------------------------------------------------------------

  def Add(self, item):
    self._data.append(item);
    self.SiftUp( len(self._data) - 1 );

  # ----------------------------------------------------------------------------

  def Remove(self):
    result = self._data[1];
    self._data[1] = self._data[-1];
    self._data.pop();
    self.SiftDown(1);
    return result;

  # ----------------------------------------------------------------------------

  def Print(self):
    elementsDistance = (80 * 1.5);
    output = StringIO();
    lastRow = -1;
    ind = 0;
    ln = len(self._data);
    for ind in range(1, ln):
      item = self._data[ind];
      row = int( math.floor( math.log(ind, 2) ) );
      if row != lastRow:
        output.write("\n");
      columns = 2**row;
      colWidth = int( math.floor(elementsDistance / columns) );
      obj = None if (item == None) else item.GetShortRepr();
      output.write( str(f"{ obj } ({ ind })").center(colWidth, ' ') );
      lastRow = row;

    print(output.getvalue());
    print("-" * 80);

  # ----------------------------------------------------------------------------

  def __repr__(self):
    str = f"< class = 'MyHeap' id = { hex( id(self) ).upper().replace('X', 'x') }\n";
    str += f"  { self._data }\n";
    str += ">\n";

    return str;

################################################################################

def HeapSort(ar):
  #print(*ar);

  myHeap = MyHeap(ar);

  #myHeap.Print();

  ans = [];

  while not myHeap.Empty():
    e = myHeap.Remove();
    #myHeap.Print();
    ans.append(e._login);

  for item in ans:
    print(item);

################################################################################

def main():
  n = int(input().rstrip());

  persons = [];

  for i in range(n):
    line = sys.stdin.readline().rstrip().split();

    login   = line[0];
    score   = int(line[1]);
    penalty = int(line[2]);

    persons.append( Person(login, score, penalty) );

  HeapSort(persons);

################################################################################

if __name__ == "__main__":
  main();

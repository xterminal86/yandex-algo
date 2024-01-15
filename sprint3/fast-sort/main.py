#!/usr/bin/python3

#
# Формат ввода
# В первой строке задано n — количество чисел для сортировки (n ≤ 1000).
# В следующей строке записаны числа от 0 до n - 1, которые надо разбить на
# блоки.
#
# Формат вывода
# Выведите максимальное количество блоков, на которое можно разбить данные при
# использовании метода Частичной сортировки.
#

import sys;

from enum import Enum;

################################################################################

class State(Enum):
  OFF     = 0
  WORKING = 1
  HALTED  = 2

################################################################################

class Machine:
  _state    = State.OFF;

  _prevNum  = None;
  _curNum   = None;

  _array    = [];
  _curBlock = [ -1, -1 ];

  _blocksCount  = 0;
  _curBlockSize = 0;
  _zero         = 0;
  _maxVal       = -1;

  # ----------------------------------------------------------------------------

  def Start(self, nums):
    self._array  = nums;
    self._maxVal = len(nums) - 1;

    self._curBlock = [ 0, nums[0] ];
    self._curBlockSize = 1;

    self._state = State.WORKING;

  # ----------------------------------------------------------------------------

  def UpdateScanParams(self):
    self._zero = self._curBlock[1] + 1;
    self._curBlock = [ 0, 0 ];
    self._curBlockSize = 1;

  # ----------------------------------------------------------------------------

  def Drive(self):
    if (self._state == State.HALTED):
      return;

    for n in self._array:
      self._prevNum = self._curNum;
      self._curNum  = n;

      if (self._curNum == self._maxVal):
        self._state = State.HALTED;
        self._blocksCount += 1;
        break;

      actual = (self._curNum - self._zero);

      closedBlockSize = (self._curBlock[1] - self._curBlock[0]) + 1;

      if (actual == 0):
        if (self._curBlockSize == closedBlockSize):
          self._blocksCount += 1;
          self.UpdateScanParams();
        else:
          self._curBlockSize += 1;
      else:
        if (self._curBlockSize == closedBlockSize):
          self._blocksCount += 1;
          self.UpdateScanParams();
        else:
          self._curBlockSize += 1;

          if (actual > self._curBlock[1]):
            self._curBlock[1] = actual;

      # self.Print();

  # ----------------------------------------------------------------------------

  def Print(self):
    decor = "-"*80;

    print(decor);
    print(f"_state        = { self._state.name }");
    print(f"_curNum       = { self._curNum }");
    print(f"_prevNum      = { self._prevNum }");
    print(f"_zero         = { self._zero }");
    print(f"_maxVal       = { self._maxVal }");
    print(f"_curBlock     = { self._curBlock }");
    print(f"_curBlockSize = { self._curBlockSize }");
    print(f"_blocksCount  = { self._blocksCount }");
    print(decor);

################################################################################

def Work(nums):

  m = Machine();
  # m.Print();

  m.Start(nums);
  m.Drive();

  return m._blocksCount;

################################################################################

def RunTests(nums):
  assert(Work([ 2, 1, 0, 3 ])                   == 2);
  assert(Work([ 0, 1, 3, 2 ])                   == 3);
  assert(Work([ 3, 6, 7, 4, 1, 5, 0, 2 ])       == 1);
  assert(Work([ 1, 0, 2, 3, 4 ])                == 4);
  assert(Work([ 2, 7, 0, 3, 6, 4, 1, 5, 8, 9 ]) == 3);
  assert(Work([ 3, 1, 2, 0, 4 ])                == 2);
  assert(Work([ 3, 2, 0, 1, 4, 6, 5 ])          == 3);
  assert(Work([ 12, 1, 8, 0, 7, 17, 2, 20,
                 9, 19, 18, 6, 14, 21, 10, 4,
                 23, 5, 3, 15, 13, 11, 22, 16 ]) == 1);

################################################################################

def main():
  n = int(input().rstrip());
  nums = list( map(int, sys.stdin.readline().rstrip().split()) );

  # print(nums);

  ans = Work(nums);

  print(ans);

  # RunTests(nums);

################################################################################

if __name__ == "__main__":
  main();

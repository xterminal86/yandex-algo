#!/usr/bin/python3

from enum import Enum;

################################################################################

class State(Enum):
  OFF      = 0
  WORKING  = 1
  FINISHED = 2

################################################################################

class Machine:
  _packedString : str = "";

  _repeaters = set(
    ("1", "2", "3", "4", "5", "6", "7", "8", "9")
  );

  _state : State = State.OFF;

  # ----------------------------------------------------------------------------

  def Start(self, packedString):
    self._packedString = packedString;
    self._state = State.WORKING;

  # ----------------------------------------------------------------------------

  def Drive(self):
    if (self._state == State.OFF) or (self._state == State.FINISHED):
      return;

    stillPacked = True;

    codeFound = False;
    nextScanStart = 0;

    while stillPacked:
      stillPacked = False;

      ln = len(self._packedString);

      repeatCount = 0;

      intl = "";

      for i in range(nextScanStart, ln):
        ch = self._packedString[i];

        if ch == '[':
          continue;

        if ch in self._repeaters:
          stillPacked = True;
          repeatCount = int(ch);
          intl = "";
          codeFound = True;
          continue;

        if ch == ']':
          self._packedString = self._packedString.replace(
            f"{ repeatCount }[{ intl }]", intl * repeatCount
          );
          break;
        else:
          intl += ch;

          if codeFound == False:
            nextScanStart = i;

    self._state = State.FINISHED;

  # ----------------------------------------------------------------------------

  def GetResult(self) -> str:
    if (self._state != State.FINISHED):
      return "";

    return self._packedString;

  # ----------------------------------------------------------------------------

  def __repr__(self) -> str:
    s = (
      f"<class 'Machine', "
      f"id = { hex( id(self) ).upper().replace('X', 'x') } "
      f"_packedString = '{ self._packedString }' "
      f"_state = { self._state }>"
    );

    return s;

################################################################################

def main():
  n = int(input().rstrip());

  m = Machine();

  strs = [ "" ] * n;

  upTo = 10**6;

  for i in range(n):
    packedString = input().rstrip();
    m.Start(packedString);
    m.Drive();
    strs[i] = m.GetResult();
    ln = len(strs[i]);
    if ln < upTo:
      upTo = ln;

  prefix = "";

  for i in range(upTo):
    ok = True;
    toCheck = strs[0][i];
    for j in range(1, n):
      if strs[j][i] != toCheck:
        ok = False;
        break;

    if ok:
      prefix += strs[0][i];
    else:
      break;

  print(prefix);

################################################################################

if __name__ == "__main__":
  main();

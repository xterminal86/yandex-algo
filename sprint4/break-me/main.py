#!/usr/bin/python3

################################################################################

class StringCounter:
  _digits = [];

  _startChar = 0;
  _endChar   = 0;
  _rankIndex = 0;

  # ----------------------------------------------------------------------------

  def __init__(self, startChar, endChar):
    self._startChar = ord(startChar);
    self._endChar   = ord(endChar);

    self._digits.append(0);

  # ----------------------------------------------------------------------------

  def __repr__(self):
    return repr(
      f"<{ self._digits }, '{ self.ToString() }'>"
    );

  # ----------------------------------------------------------------------------

  def Increment(self):
    self._digits[self._rankIndex] += 1;

    if (self._digits[self._rankIndex] > (self._endChar - self._startChar)):
      self._digits[self._rankIndex] = 0;
      self.Carry();

  # ----------------------------------------------------------------------------

  def Carry(self):
    self._rankIndex += 1;

    if (self._rankIndex == len(self._digits)):
      self._digits.append(0);
    else:
      self._digits[self._rankIndex] += 1;
      if (self._digits[self._rankIndex] > (self._endChar - self._startChar)):
        self._digits[self._rankIndex] = 0;
        self.Carry();

    self._rankIndex = 0;

  # ----------------------------------------------------------------------------

  def ToString(self):
    strRep = "";

    for item in self._digits:
      strRep += chr(item + self._startChar);

    return strRep;

################################################################################

def HornerHash(s, base, mod):
  ln = len(s);

  if (ln == 1):
    return (ord(s) % mod);

  res = ord(s[0]);

  for i in range(1, ln):
    res = ( ord(s[i]) + res * base ) % mod;

  return res;

################################################################################

def TestStringCounter():
  s = StringCounter("a", "z");

  print("Init: ", s);
  print("");

  for i in range(200):
    s.Increment();
    print(s);

  exit(0);

################################################################################

def main():
  #TestStringCounter();

  base = 1000;
  mod  = 123987123;

  s = StringCounter("a", "z");

  d = {};

  collisionCounter = 0;
  maxCollisions = 100;
  passes = 0;

  while (collisionCounter < maxCollisions):
    s.Increment();
    str = s.ToString();
    h = HornerHash(str, base, mod);

    if h not in d:
      d[h] = [ str ];
    else:
      d[h].append(str);
      collisionCounter += 1;
      print(f"got collision { collisionCounter } on pass { passes }");

    passes += 1;

  print("");
  print("collisions list:");
  print("");

  for k,v in d.items():
    if len(v) > 1:
      print(k, v);

################################################################################

if __name__ == "__main__":
  main();

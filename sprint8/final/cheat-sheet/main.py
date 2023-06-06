#!/usr/bin/python3

# constest id = 88002018

# Временная сложность - O(n + k), где n - длина строки, k - время поиска по бору.
# Пространственная - O(n + s), где n - кол-во элементов в боре,
#                    s - длина массива DP, равная длине исходной строки + 1.

import sys;

################################################################################

class Trie:
  _root = {};

  # ----------------------------------------------------------------------------

  def Find(self, word) -> bool:
    head = self._root;
    for char in word:
      if char not in head:
        return False;

      head = head[char];

    if 0 in head:
      return True;

    return False;

  # ----------------------------------------------------------------------------

  def Add(self, string):
    head = self._root;
    ln = len(string);
    for i in range(ln):
      ch = string[i];

      if ch not in head:
        head[ch] = {};

      head = head[ch];

    head.update({ 0 : 0 });

  # ----------------------------------------------------------------------------

  _traverseHead = None;

  def Reset(self):
    self._traverseHead = self._root;

  # ----------------------------------------------------------------------------

  def Traverse(self, ch):
    if ch not in self._traverseHead:
      return False;
    else:
      self._traverseHead = self._traverseHead[ch];
      return True;

  # ----------------------------------------------------------------------------

  def DeleteIntl(self, node, string):
    if len(string) == 0:
      if len(node) != 0:
        return node;
      else:
        return None;

    ch = string[0];
    if ch in node:
      return self.DeleteIntl(node[ch], string[1:]);
    else:
      return node;

  # ----------------------------------------------------------------------------

  def Delete(self, string):
    res = self.DeleteIntl(self._root, string);
    if res == None:
      del self._root[ string[0] ];

  # ----------------------------------------------------------------------------

  def PrintIntl(self, start, indent):
    cur = start;
    spaces = "." * indent;
    if (type(cur) is dict):
      for k,v in cur.items():
        print(f"{ spaces }{ k }");
        self.PrintIntl(cur[k], indent + 2);
        if type(v) is int:
          print("-"*80);

  # ----------------------------------------------------------------------------

  def Print(self):
    print("="*80);
    print("TRIE");
    print("="*80);
    self.PrintIntl(self._root, 0);

  # ----------------------------------------------------------------------------

  def __repr__(self):
    s = (
      f"<class 'Trie' id = { hex( id(self) ).upper().replace('X', 'x') } "
      f"_root = { self._root }>"
    );
    return s;

################################################################################

def PrintDP(dp):
  for item in dp:
    print(1 if (item == True) else 0, end="");
  print("");

################################################################################

def main():
  s = list( input().rstrip() );

  n = int(input().rstrip());

  words = [ "" ] * n;

  t = Trie();

  for i in range(n):
    words[i] = input().rstrip();
    t.Add(words[i]);

  #t.Print();

  dp = [ False ] * (len(s) + 1);

  dp[len(s)] = True;

  for i in range(len(s) - 1, -1, -1):
    t.Reset();
    for j in range(i, len(s)):
      res = t.Traverse(s[j]);

      if res == False:
        break;

      if (0 in t._traverseHead) and (dp[j + 1] == True):
        dp[i] = True;

    #PrintDP(dp);

  if dp[0] == True:
    print("YES");
  else:
    print("NO");

################################################################################

if __name__ == "__main__":
  main();

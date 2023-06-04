#!/usr/bin/python3

import re;

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

    return True;

  # ----------------------------------------------------------------------------

  def Add(self, string):
    head = self._root;
    ln = len(string);
    for i in range(ln):
      ch = string[i];

      if ch not in head:
        head[ch] = {};

      head = head[ch];

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
    for k,v in cur.items():
      print(f"{ spaces }{ k }");
      self.PrintIntl(cur[k], indent + 2);
      if len(cur[k]) == 0:
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
    for word in words:      
      if ( (i + len(word)) <= len(s) ):
        w = s[i : i + len(word)];
        if t.Find("".join(w)):
          dp[i] = dp[i + len(word)];
          
      if dp[i] == True:
        break;
      
  if dp[0] == True:
    print("YES");
  else:
    print("NO");
  
################################################################################

if __name__ == "__main__":
  main();

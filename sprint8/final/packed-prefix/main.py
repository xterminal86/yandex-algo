#!/usr/bin/python3

# contest id = 87791585

#
# Временная сложность - O(n^2), в случае если подана куча длинных одинаковых
#                       строк без "упаковки", в среднем по палате - O(n + p),
#                       где p - длина общего префикса.
# Пространственная    - O(k), где k - кол-во рекурсивных вызовов, равное кол-ву
#                       "закодированных" строк, содержащихся во входной строке.
#

################################################################################

Indent = -2;

def UnpackString(ps, ind, ans, debug=False):
  if debug:
    global Indent;
    Indent += 2;
    spaces = "." * Indent;
    print(f"{ spaces }in = { ps }, ind = { ind }");
  ln = len(ps);
  tmp = [];
  while ind < ln:
    ch = ps[ind];
    if str.isdigit(ch):
      if debug:
        print(f"{ spaces }found repeat { ch } at position { ind }");
      toRepeat = int(ch);
      ind += 2;
      (unpacked, end) = UnpackString(ps, ind, tmp, debug);
      tmp += (toRepeat * unpacked);
      ind = end;
      if debug:
        print(f"{ spaces }so far: { tmp }, i = { ind }");
    elif ch == ']':
      if debug:
        print(f"{ spaces }ret ({ tmp }, { ind + 1 })");
      Indent += -2;
      return (tmp, ind + 1);
    else:
      tmp += ch;
      ind += 1;

  ans += tmp;

################################################################################

def main():
  n = int(input().rstrip());

  unpackedStrings = [ "" ] * n;

  upTo = 10**6;

  for i in range(n):
    ans = [];
    s = input().rstrip();
    packed = list(s);
    UnpackString(packed, 0, ans);
    us = "".join(ans);

    if len(us) < upTo:
      upTo = len(us);

    unpackedStrings[i] = us;

  prefix = "";

  for i in range(upTo):
    letter = unpackedStrings[0][i];
    for j in range(1, n):
      if letter != unpackedStrings[j][i]:
        print(prefix);
        return;

    prefix += letter;

  print(prefix);

################################################################################

if __name__ == "__main__":
  main();

#!/usr/bin/python3

################################################################################

def main():
  line = input().rstrip().split();
  v = int(line[0]);
  e = int(line[1]);

  ans = [ None ] * (v + 1);

  for i in range(e):
    line = input().rstrip().split();
    from_ = int(line[0]);
    to    = int(line[1]);

    if (ans[from_] == None):
      ans[from_] = [ to ];
    else:
      ans[from_].append(to);

  ln = len(ans);

  for i in range(1, ln):
    if ans[i] == None:
      print(0);
    else:
      out = f"{ len(ans[i]) } ";
      for item in ans[i]:
        out += f"{ item } ";
      out = out[:-1];
      print(out);

################################################################################

if __name__ == "__main__":
  main();

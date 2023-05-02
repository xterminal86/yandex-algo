#!/usr/bin/python3

################################################################################

def PrintArray(ar):
  ln = len(ar);
  out = "";
  for x in range(1, ln):
    for y in range(1, ln):
      out += f"{ ar[x][y] } ";
    out += "\n";
  print(out);

################################################################################

def main():
  line = input().rstrip().split();
  vertices = int(line[0]);
  edges    = int(line[1]);

  mtx = [ [0 for x in range(vertices + 1)] for y in range(vertices + 1) ];

  colors = [0] * (vertices + 1);

  for i in range(edges):
    line = input().rstrip().split();
    from_ = int(line[0]);
    to    = int(line[1]);

    mtx[from_][to] = 1;

  PrintArray(mtx);

################################################################################

if __name__ == "__main__":
  main();

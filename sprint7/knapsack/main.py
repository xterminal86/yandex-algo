#!/usr/bin/python3

################################################################################

def PrintMatrix(mtx):
  for line in mtx:
    print(line);

################################################################################

def main():
  line = input().rstrip().split();

  n        = int(line[0]);
  capacity = int(line[1]);

  weights = [ 0 ] * (n + 1);
  values  = [ 0 ] * (n + 1);

  dp = [ [0 for x in range(capacity + 1)] for y in range(n + 1)];

  for i in range(1, n + 1):
    line = input().rstrip().split();
    m = int(line[0]);
    c = int(line[1]);

    weights[i] = m;
    values[i]  = c;

  #print("weights = ", weights);
  #print("values  = ", values);
  #print("-"*80);

  for i in range(n + 1):
    #print(f"i = { i }");
    for w in range(capacity + 1):
      if (i == 0) or (w == 0):
        dp[i][w] = 0;
      elif weights[i] <= w:
        #print(f"  i = { i } w = { w } weights[i] = { weights[i] } (w - weights[i]) = { w - weights[i] }");
        #print(f"  values[i] = { values[i] }");
        dp[i][w] = max(values[i] + dp[i - 1][ w - weights[i] ], dp[i - 1][w]);
      else:
        dp[i][w] = dp[i - 1][w];

    #PrintMatrix(dp);
    #print("-"*80);

  #PrintMatrix(dp);

  i = n;
  j = capacity;

  ans = [];

  while (i > 0) and (j > 0):
    if (dp[i][j] == dp[i - 1][j]):
      i += -1;
    else:
      ans.append(i);
      j = j - weights[i];
      i += -1;

  print(len(ans));
  print(*ans);

################################################################################

if __name__ == "__main__":
  main();

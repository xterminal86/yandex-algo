#!/usr/bin/python3

def Fib(n, m):  
  if (n == 0) or (n == 1):    
    return 1;
  
  ans = 0;

  a = 1;
  b = 1;

  mod = pow(10, m);
  
  ind = 0;
  
  for i in range(2, n + 1):
    a = (a + b) % mod;
    a, b = b, a;
    
  return b;  

################################################################################

def main():
  nums = input().rstrip().split();

  n = int(nums[0]);
  k = int(nums[1]);
  
  print(Fib(n, k));

################################################################################
    
if __name__ == "__main__":
  main();
  

#!/usr/bin/python3

if __name__ == "__main__":
  n  = int(input());
  a1 = input().split();
  a2 = input().split();

  answer = "";

  for i in range(n):
    for j in range(2):
      if j == 0:
        answer += f"{ a1[i] } ";
      else:
        answer += f"{ a2[i] } ";

  answer = answer[:-1];

  print(answer);

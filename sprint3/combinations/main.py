#!/usr/bin/python3

Keys = {
  "2" : "abc",
  "3" : "def",
  "4" : "ghi",
  "5" : "jkl",
  "6" : "mno",
  "7" : "pqrs",
  "8" : "tuv",
  "9" : "wxyz",
};

Answer = [];

################################################################################

def FindCombinations(lst, str):
  global Answer;

  if len(lst) == 0:
    Answer.append(str);
    return;

  for c in lst[0]:
    FindCombinations(lst[1:], str + c);

################################################################################

def main():
  global Keys;
  global Answer;

  str = input().rstrip();

  inData = [];

  for d in str:
    inData.append(Keys[d]);

  FindCombinations(inData, "");

  output = "";

  for item in Answer:
    output += f"{ item } ";

  output = output[:-1];

  print(output);

################################################################################

if __name__ == "__main__":
  main();


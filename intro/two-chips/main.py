#!/usr/bin/python3

def FindChips(chipsList, sumToAchieve):
  for i in range(len(chipsList)):
    for j in range(i + 1, len(chipsList)):
      sum_ = chipsList[i] + chipsList[j];
      if sum_ == sumToAchieve:
        return chipsList[i], chipsList[j];

  return None, None;

if __name__ == "__main__":
  chipsNumber  = int(input());
  chipsCost    = list(map(int, input().split()));
  sumToAchieve = int(input());

  v1, v2 = FindChips(chipsCost, sumToAchieve);

  if (v1 != None):
    print(f"{ v1 } { v2 }");
  else:
    print(f"{ v1 }");

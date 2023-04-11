#!/usr/bin/python3

def FindChips(chipsList, sumToAchieve):
  s = 0;
  e = len(chipsList) - 1;

  while s != e:
    start = chipsList[s];
    end   = chipsList[e];

    sum = start + end;

    if sum == sumToAchieve:
      return start, end;
    elif sum < sumToAchieve:
      s += 1;
    elif sum > sumToAchieve:
      e -= 1;

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

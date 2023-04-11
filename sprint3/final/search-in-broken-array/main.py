#!/usr/bin/python3

import sys;

################################################################################

def BinarySearch(array, x, indStart, indEnd):
  left  = indStart;
  right = indEnd;

  while (left <= right):
    m = left + (right - left) // 2;

    # print("  binary search: left = ", left, " right = ", right, " m = ", m);

    if (m == indEnd):
      break;

    if (int(array[m]) == x):
      return m;

    if (int(array[m]) < x):
      left = m + 1;
    else:
      right = m - 1;

  return -1;

################################################################################

def IsReallyBroken(nums, indStart, indEnd):
  print("  broken? [", nums[indStart], " ... ", nums[indEnd - 1], "]", indStart, indEnd);

  if (indEnd - indStart > 1) and (int(nums[indStart]) > int(nums[indEnd - 1])):
    print("  yes");
    return True;

  print("  no");
  return False;

################################################################################

def IsTargetInside(nums, target, indStart, indEnd):
  print("   ", target, "inside? [", nums[indStart], "...", nums[indEnd - 1], "]", indStart, indEnd);

  if (target <= int(nums[indEnd - 1])) and (target >= int(nums[indStart])):
    print("    yes");
    return True;

  print("    no");
  return False;

################################################################################

def Divide(indStart, indEnd):
  print("  divide", indStart, "-", indEnd);

  blockLen = (indEnd - indStart) + 1;

  blockIndL = [ 0, 0 ];
  blockIndR = [ 0, 0 ];

  if (blockLen == 2):
    blockIndL[0] = indStart;
    blockIndL[0] = indStart + 1;

    blockIndR[0] = indEnd;
    blockIndR[1] = indEnd + 1;
  else:
    d = (indEnd - indStart);
    mid = indStart + d // 2;

    print("  d = ", d, " mid = ", mid);

    blockIndL[0] = indStart;
    blockIndL[1] = mid;

    blockIndR[0] = mid;
    blockIndR[1] = indEnd;

  print("  got blocks", blockIndL, blockIndR);

  return [ blockIndL, blockIndR ];

################################################################################

ShouldStop = False;

def TryToFind(nums, target, interval):
  global ShouldStop;

  print("  try to find", target, "in", interval);

  if (IsReallyBroken(nums, interval[0], interval[1]) == False):
    if (IsTargetInside(nums, target, interval[0], interval[1])):
      print("  searching", nums[interval[0]], "...", nums[interval[1] - 1]);
      ind = BinarySearch(nums, target, interval[0], interval[1]);
      ShouldStop = True;
      return ind;
    else:
      return -1;

  return -2;

################################################################################

def BrokenSearchWrapper(nums, target, tasks):
  global ShouldStop;

  res = -1;

  # cnt = 0;

  while (ShouldStop == False) and (len(tasks) != 0):
    print("tasks so far:", tasks);
    toCheck = tasks.pop();
    print("got task", toCheck);
    res = TryToFind(nums, target, toCheck);

    if (res == -2):
      blocks = Divide(toCheck[0], toCheck[1]);
      tasks.append(blocks[0]);
      tasks.append(blocks[1]);

    # cnt += 1;

    #if (cnt == 8):
    #  exit(0);

  return res;

################################################################################

def broken_search(nums, target) -> int:
  global ShouldStop;

  ShouldStop = False;
  tasks = [];

  if (IsReallyBroken(nums, 0, len(nums)) == False):
    return BinarySearch(nums, target, 0, len(nums));
  else:
    tasks.append([ 0, len(nums) ]);
    return BrokenSearchWrapper(nums, target, tasks);

################################################################################

def main():
  n = int(input().rstrip());
  k = int(input().rstrip());
  arr = sys.stdin.readline().rstrip().split();

  print(k);
  print(arr);

  ans = broken_search(arr, k);

  print(ans);

################################################################################

if __name__ == "__main__":
  main();

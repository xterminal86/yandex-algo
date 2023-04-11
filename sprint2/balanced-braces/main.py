#!/usr/bin/python3

import sys;

OpenBraces = [];

#################################################################################

def ProcessBrace(brace):
  global OpenBraces;
  
  if (brace == "[" or brace == "{" or brace == "("):
    OpenBraces.append(brace);
  elif (brace == "]" or brace == "}" or brace == ")"):
    if len(OpenBraces) == 0:
      return False;

    lastBrace = OpenBraces.pop();
    
    if (lastBrace == "("):
      if (brace != ")"):
        return False;
      
    if (lastBrace == "["):
      if (brace != "]"):
        return False;

    if (lastBrace == "{"):
      if (brace != "}"):
        return False;
      
  return True;

#################################################################################

def BruteForce(sequence):
  toWork = sequence;
  
  while len(toWork) != 0:
    lnStart = len(toWork);
    toWork = toWork.replace("()", "");
    toWork = toWork.replace("[]", "");
    toWork = toWork.replace("{}", "");

    if (len(toWork) == lnStart):
      return False;
    
  return True;

#################################################################################

def StackSolution(sequence):  
  for c in sequence:
    ok = ProcessBrace(c);
    if (ok == False):
      return False;

  if len(OpenBraces) != 0:
    return False;
  
  return True;

#################################################################################
  
def IsCorrect(sequence):
  # return BruteForce(sequence);    
  return StackSolution(sequence);

#################################################################################

def main():
  sequence = sys.stdin.readline().rstrip();
  print(IsCorrect(sequence));

#################################################################################
  
if __name__ == "__main__":
  main();
  

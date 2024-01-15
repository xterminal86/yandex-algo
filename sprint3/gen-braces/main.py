#!/usr/bin/python3

#
# Формат ввода
# На вход функция принимает n — целое число от 0 до 10.
#
# Формат вывода
# Функция должна напечатать все возможные скобочные последовательности заданной
# длины в алфавитном (лексикографическом) порядке.
#

Ans = [];
OpenBraces = [];

################################################################################

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

################################################################################

def IsCorrect(sequence):
  global OpenBraces;

  OpenBraces = [];

  for c in sequence:
    ok = ProcessBrace(c);
    if (ok == False):
      return False;

  if len(OpenBraces) != 0:
    return False;

  return True;

################################################################################

def GenBraces(n, out):
  global Ans;

  if n == 0:
    if (IsCorrect(out)):
      Ans.append(out);
  else:
    GenBraces(n - 1, out + "(");
    GenBraces(n - 1, out + ")");

################################################################################

def main():
  global Ans;

  n = int(input().rstrip());

  out = "";

  GenBraces(n * 2, out);

  for item in Ans:
    print(item);

################################################################################

if __name__ == "__main__":
  main();

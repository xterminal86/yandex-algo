#!/usr/bin/python3

#
# Формат ввода
# В первой строке дано имя из паспорта.
#
# Во второй строке —- имя из базы.
#
# Обе строки состоят из строчных букв английского алфавита. Размер каждой строки
# не превосходит 100 000 символов.
#
# Формат вывода
# Выведите «OK», если человека пропустят, или «FAIL» в противном случае.
#

################################################################################

def main():
  s1 = input().rstrip();
  s2 = input().rstrip();

  print(s1);
  print(s2);

  ln1 = len(s1);
  ln2 = len(s2);

  d = abs(ln1 - ln2);

  if d > 1:
    print("FAIL");
    return;

  offset = ord('a');

  alphabetLetters = 26;

  letters1 = [ 0 ] * alphabetLetters;
  letters2 = [ 0 ] * alphabetLetters;

  upTo = max(ln1, ln2);

  for i in range(upTo):
    if ln1 > i:
      ind1 = ord(s1[i]) - offset;
      letters1[ind1] += 1;
    if ln2 > i:
      ind2 = ord(s2[i]) - offset;
      letters2[ind2] += 1;

  print(letters1);
  print(letters2);

  errors = 0;

  if ln1 == ln2:
    for i in range(ln1):
      if s1[i] != s2[i]:
        errors += 1;

      if errors > 1:
        print("FAIL");
        return;
  else:
    for i in range(alphabetLetters):
      if letters1[i] != letters2[i]:
        errors += 1;

      if errors > 2:
        print("FAIL");
        return;

  print("OK");

################################################################################

if __name__ == "__main__":
  main();

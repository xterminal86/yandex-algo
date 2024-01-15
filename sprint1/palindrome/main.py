#!/usr/bin/python3

#
# Формат ввода
# В единственной строке записана фраза или слово. Буквы могут быть только
# латинские. Длина текста не превосходит 20000 символов.
#
# Фраза может состоять из строчных и прописных латинских букв, цифр, знаков
# препинания.
#
# Формат вывода
# Выведите «True», если фраза является палиндромом, и «False», если не является.
#

import sys;

def main():
  in_ = sys.stdin.readline().rstrip().lower();

  text = "";

  for c in in_:
    if c.isalnum():
      text += c;

  reversed = text[::-1];

  if text == reversed:
    print("True");
  else:
    print("False");

################################################################################

if __name__ == "__main__":
  main();

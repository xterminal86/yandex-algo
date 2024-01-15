#!/usr/bin/python3

#
# Формат ввода
# В первой строке записана строка s, во второй –— строка t. Длины обеих строк
# не превосходят 10^6. Обе строки содержат хотя бы по одному символу и состоят
# только из маленьких латинских букв.
#
# Строки могут быть разной длины.
#
# Формат вывода
# Выведите «YES», если строки равны (согласно вышеописанным правилам), и «NO»
# в ином случае.
#

def Compare(s1, s2):
  if len(s1) != len(s2):
    return False;

  ln = len(s1);

  d1 = {};
  d2 = {};

  for i in range(ln):
    c1 = s1[i];
    c2 = s2[i];

    if c1 not in d1:
      d1[c1] = c2;

      if c2 not in d2:
        d2[c2] = c1;
      else:
        val = d2[c2];

        if val != c1:
          return False;

    else:
      if c2 not in d2:
        return False;

      if d1[c1] != c2:
        return False;

    #print("d1 = ", d1);
    #print("d2 = ", d2);
    #print("");

  return True;

################################################################################

def Tests():
  assert( Compare("mxyskaoghi", "qodfrgmslc") == True  );
  assert( Compare("agg", "xdd")               == True  );
  assert( Compare("agg", "xda")               == False );
  assert( Compare("ukwltcgrvxkjijdlkwhodsaeyjkccdmvdlppwvtbxfliuelcfekehdperadfcxbsodzmtraxex",
                  "vmobscpjfymieinbmoltnxgkdimccnqfnbhhofsryabevkbcakmklnhkjgnacyrxtnzqsjgyky") == True );
  assert( Compare("aba", "xxx")               == False );

################################################################################

def main():
  s1 = input().rstrip();
  s2 = input().rstrip();

  #print(s1);
  #print(s2);

  res = Compare(s1, s2);

  print("YES" if res == True else "NO");

################################################################################

if __name__ == "__main__":
  main();

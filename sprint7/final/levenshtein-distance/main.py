#!/usr/bin/python3

# contest id = 87372693

#
# Поскольку в теории про это ничего нет, то идём в интернет
# и берём информацию оттуда.
#
# Для закрепления материала смотрим ролики с индусами на ютубе.
#
# Временная сложность O(n*m), где n, m - длины соответствующих строк.
# Пространственная  - O(n*m) для хранения матрицы.
#

################################################################################

def main():
  s1 = input().rstrip();
  s2 = input().rstrip();

  n = len(s1);
  m = len(s2);

  dp = [ [0 for _ in range(m + 1)] for _ in range(n + 1)];

  #
  # Отсюда будем "раскручивать" решение.
  #

  #
  # Записываем стоимость трансформации пустой строки в
  # одну из заданных путём вставки символов.
  #
  for i in range(1, n + 1):
    dp[i][0] = i;

  #
  # Записываем стоимость трансформации другой строки из заданных в пустую
  # путём удаления символов.
  #
  for i in range(1, m + 1):
    dp[0][i] = i;

  sc = 0;

  for i in range(1, n + 1):
    for j in range(1, m + 1):
      if s1[i - 1] == s2[j - 1]:
        sc = 0;
      else:
        sc = 1;

      dp[i][j] = min( dp[i - 1][j] + 1,     # delete
                      dp[i][j - 1] + 1,     # insert
                      dp[i - 1][j - 1] + sc # replace
                    );

  print(dp[n][m]);

################################################################################

if __name__ == "__main__":
  main();
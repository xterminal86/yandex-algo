#!/usr/bin/python3

# contest id = 85141287

#
# Реализация "хеш-таблицы" для целочисленных ключей.
# По факту получается массив списков (хотя наверное это всегда так),
# хеш в данном случае тривиальный - само число по модулю.
#
# Коллизии разрешаются методом цепочек, т.к. этот способ мне нравится больше
# и на мой взгляд он более логичен.
#
#
# Временная сложность - O(1), но это в идеале.
#
# Коллизии начнут возникать когда все корзины будут заполнены, а это произойдёт
# когда будут выбраны все элементы из кольца вычетов по модулю
# (100003 в данном случае) при равномерном заполнении, либо если добавлять
# элементы "по кругу" модуля (например в случае модуля 10 - это 2, 12, 22 и т.п.). 
# Соответственно чем больше элементов сверх лимита будет напихано, 
# тем сильнее время поиска будет стремиться в сторону O(n),
# т.к. в худших случаях нам придётся идти линейным поиском по списку
# коллизионных элементов.
#
# Пространственная сложность - размер массива для хранения корзин,
# в данном случае O( sizeof(HashTableItem)*(2^17) ), плюс дополнительные траты
# на список коллизий, которые, опять же, будут расти по мере увеличения
# коллизионных элементов.
# Т.е. в некотором супер-плохом случае будет O( 2^17 ) * n,
# где n - насколько превышен безколлизионный лимит.
#

import sys;

################################################################################

class HashTable:
  _mod = 100003;
  # Knuth constant:
  # alpha = (sqrt(5) - 1) / 2 = 0.6180339887498949
  #
  # total buckets in our case = 2^17
  #
  # s = 2654435769
  # alpha = s / (2^32)
  #
  _bucketsPow = 17;

  _maxBuckets = pow(2, _bucketsPow) + 1;

  _buckets = [ None ] * _maxBuckets;

  # ----------------------------------------------------------------------------

  class HashTableItem:
    _key   = None;
    _value = None;

    def __init__(self, k, v):
      self._key   = k;
      self._value = v;

    def __repr__(self):
      return f"< k = { self._key }, v = { self._value } >";

  # ----------------------------------------------------------------------------

  def __repr__(self):
    return f"< { self._buckets } >";

  # ----------------------------------------------------------------------------

  '''
  def GetBucketIndex(self, hash):
    ind = ((hash * self._s) & self._two32) >> (32 - self._bucketsPow);
    # print(f"  bucket index for { hash } = { ind }");
    return ind;
  '''

  def GetBucketIndex(self, hash):
    return (hash % self._mod);

  # ----------------------------------------------------------------------------

  def Get(self, key):
    ind = self.GetBucketIndex(key);

    valueFound = None;

    if self._buckets[ind] != None:
      for item in self._buckets[ind]:
        if (item._key == key):
          valueFound = item._value;

    return valueFound;

  # ----------------------------------------------------------------------------

  def Put(self, key, value):
    ind = self.GetBucketIndex(key);

    if (self._buckets[ind] == None):
      self._buckets[ind] = [];
    else:
      for item in self._buckets[ind]:
        if (item._key == key):
          item._value = value;
          return;

    self._buckets[ind].append(self.HashTableItem( key, value ));

  # ----------------------------------------------------------------------------

  def Delete(self, key):
    ind = self.GetBucketIndex(key);

    valueFound = None;

    cnt = 0;

    if self._buckets[ind] != None:
      for item in self._buckets[ind]:
        if (item._key == key):
          valueFound = item._value;
          break;

        cnt += 1;

      if (valueFound != None):
        del self._buckets[ind][cnt];
        #self._buckets[ind][cnt] = list();

    return valueFound;

################################################################################

def ProcessCommand(ht, cmdSplit):
  #print("-"*80);
  #print(f"CMD: '{ cmdSplit }'");
  #print("-"*80);

  cmdName = cmdSplit[0];
  if (cmdName == "get"):
    key = int(cmdSplit[1]);
    res = ht.Get(key);
    print(res);
  elif (cmdName == "put"):
    key   = int(cmdSplit[1]);
    value = int(cmdSplit[2]);
    ht.Put(key, value);
  elif (cmdName == "delete"):
    key = int(cmdSplit[1]);
    res = ht.Delete(key);
    print(res);

  # print(ht);

################################################################################

def main():
  ht = HashTable();

  cmds = int(input().rstrip());

  for i in range(cmds):
    line = sys.stdin.readline().rstrip().split();
    ProcessCommand(ht, line);

################################################################################

if __name__ == "__main__":
  main();

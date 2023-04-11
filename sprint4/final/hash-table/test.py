#!/usr/bin/python3

class Item:
  _key = None;
  _value = None;
  
  def __init__(self, k, v):
    self._key   = k;
    self._value = v;
    
  def __repr__(self):
    return f"< k = { self._key }, v = { self._value } >";
    
  def __eq__(self, other):
    return self._key == other._key;
    
lst = [];

for i in range(10):
  i = Item(i, i);
  lst.append(i);
  
print(lst);
print("");

del lst[3];

print(lst);
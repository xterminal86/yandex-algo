#!/usr/bin/python3

import sys;

################################################################################

class Document:
  _words = {};

  _inputIndex = 0;
  _relevance  = 0;

  _lastQuery = set();

  # ----------------------------------------------------------------------------

  def __init__(self, ind, wordsArray):
    self._inputIndex = ind + 1;

    # this is bullshit
    self._words     = {};
    self._lastQuery = set();

    for word in wordsArray:
      if word in self._words:
        self._words[word] += 1;
      else:
        self._words[word] = 1;

  # ----------------------------------------------------------------------------

  def __repr__(self):
    s = (
      f"\n< class 'Document'\n"
      f"  id        = { hex(id(self)).upper().replace('X', 'x') }\n"
      f"  ind       = { self._inputIndex }\n"
      f"  words     = { self._words }\n"
      f"  relevance = { self._relevance } >\n"
    );

    return s;

  # ----------------------------------------------------------------------------

  def __lt__(self, other):
    if (self._relevance > other._relevance):
      return True;
    elif (self._relevance == other._relevance):
      if (self._inputIndex < other._inputIndex):
        return True;

    return False;

  # ----------------------------------------------------------------------------

  def GetWordCount(self, word):
    if word in self._words:
      return self._words[word];
    return 0;

  # ----------------------------------------------------------------------------

  def ProcessQuery(self, words):
    self._relevance = 0;
    self._lastQuery = words;

    for w in self._lastQuery:
      if w in self._words:
        self._relevance += self._words[w];

################################################################################

def main():
  outputLimit = 5;

  n = int(input().rstrip());

  docs = [ None ] * n;

  allWords = set();

  for i in range(n):
    line = sys.stdin.readline().rstrip().split();
    unique = set(line);
    allWords |= unique;
    docs[i] = Document(i, line);

  docsByWords = {};

  for word in allWords:
    docsByWords[word] = {};
    for doc in docs:
      docsByWords[word][doc._inputIndex] = doc.GetWordCount(word);

  #for k,v in docsByWords.items():
  #  print(f"{ k } = { v }");

  #print("="*80);

  m = int(input().rstrip());

  for i in range(m):
    words = sys.stdin.readline().rstrip().split();

    #print(f"query = '{ words }'");

    uniqueWords = set(words);

    #print(f"unique words = '{ uniqueWords }'");

    for w in uniqueWords:
      if w in docsByWords:
        docsMap = docsByWords[w];

        #print(f"    docsMap = { docsMap }");

        for docInd, wordCount in docsMap.items():
          #print(f"  adding word '{ w }' to doc no. { docInd } count = { wordCount }");
          docs[docInd - 1]._relevance += wordCount;

        #print("-"*80);

    docsCopy = docs[:];

    list.sort(docsCopy);

    #print(docsCopy);

    cnt = 0;

    ans = [];

    for item in docsCopy:
      if (item._relevance == 0):
        continue;

      ans.append(item._inputIndex);

      cnt += 1;

      if (cnt >= outputLimit):
        break;

    print(*ans);

    for item in docs:
      item._relevance = 0;

    #print("="*80);

################################################################################

if __name__ == "__main__":
  main();

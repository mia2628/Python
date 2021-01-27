def solution(paragraph, banned):
  words = re.sub('[^\m]', ' ', paragraph).lower().split()
  words = filter(lambda x: x not in banned, words)
  counter = collection.Counter(words)
  print(counter.most_common())

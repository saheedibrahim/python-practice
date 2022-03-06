search = 'Searching for knowledge is what is encouraged'
words = search.split()
print(words)
deleteFirst = words.pop(1)
print(words)
del words[0]
print(words)
words.remove("is")
print(words)
rearrangeWords = sorted(words)
print(rearrangeWords)
rearrangeWords.append('books')
print(rearrangeWords)
rearrangeWords = rearrangeWords + ['schools']
print(rearrangeWords)
rearrangeWords += ['revision']
print(rearrangeWords)
s = " "
newWords = s.join(rearrangeWords)
print(newWords)
def words(phrase):
  sentence = phrase.split()
  ls = []  
  for i in sentence:
	try:
		x = int(i)
	except ValueError:
		word_count = sentence.count(i) 
		ls.append((i,word_count))   
	else:
		word_count = sentence.count(x) 
		ls.append((x,word_count))   
  result = dict(ls)
  return result
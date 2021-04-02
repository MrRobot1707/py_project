from textblob import TextBlob

wrong_word = ["Data Scence", "Mahine Learnin"]
correct_word = []
for i in wrong_word:
	correct_word.append(TextBlob(i))
print("wrong word:",wrong_word)
for i in correct_word:
	print(i.correct(),end="")

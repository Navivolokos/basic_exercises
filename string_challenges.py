# Вывести последнюю букву в слове
word = 'Архангельск'

print(word[-1])



# Вывести количество букв "а" в слове
word = 'Архангельск'
word = word.lower()
print(word.count('а'))
	


# Вывести количество гласных букв в слове
word = 'Архангельск'
word = word.lower()
letter=['а','е','и','о','у','ё','ю','я']
b=[]
for a in word:
	if a in letter:
		b.append(a)
print(len(b))



# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
num_words=len(sentence.split())
print(num_words)

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
words =sentence.split()

for word in words:
	print(f'{word[0]}\n')

# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
# ???
num_words=(sentence.split())
spisok=[]
for word in num_words:
	a=len(word)/len(num_words)
	spisok.append(a)
print(int(sum(spisok)))
	

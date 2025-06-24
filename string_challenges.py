# Вывести последнюю букву в слове
word = 'Архангельск'

print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
word = word.lower()
print(word.count('а'))
	

# Вывести количество гласных букв в слове
"""word = 'Архангельск'
word = word.lower()
letter=['а','е','и','о','у','ё','ю','я']
b=[]
for a in word:
	if a in letter:
		b.append(a)
print(len(b))"""

word = 'Архангельск'
word = word.lower()
letter = 'а, е, и, о, у, ё, ю, я'
num=0
for let in word:
	if let in letter:
		num=num+1
print(num)


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
num_words=len(sentence.split())
print(num_words)

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
words =sentence.split()

for word in words:
	print(f'{word[0]}')

# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
num_words=(sentence.split())
spisok=[]
for word in num_words:
	dlina=len(word)
	#print(dlina)	
	spisok.append(dlina)
sr_summ = int(sum(spisok)/len(spisok))
print(sr_summ)	








	
	
	




	

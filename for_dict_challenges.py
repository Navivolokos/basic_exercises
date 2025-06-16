# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

list={}
for name in students:
    povtor = students.count(name)    
    list[name.get('first_name')] = povtor    
for a in list:
    print(a, ": ", list[a])   
    

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]

list={}
for name in students:
    povtor = students.count(name)    
    list[name.get('first_name')] = povtor
dic =list
max_name=max(dic, key=dic.get)
print("Самое частое имя среди учеников: ", max_name)


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]

for class1 in school_students:   
    list={}
    for name in class1:        
        povtor = class1.count(name)        
        for i in range(len(school_students)):
            list[name.get('first_name')] = povtor
            dic =list
            max_name=max(dic, key=dic.get)                   
    print(f'Самое частое имя в классе {school_students.index(class1)+1}:  {max_name}')
        
# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

for study in school: # перебираем классы
	print(f"В классе {study['class']}: ", end="")
	male_num=0
	female_num=0
	for stud in study['students']: # перебираем студентов
		if is_male.get(stud['first_name'])==False: # если женский пол
			female_num=female_num+1
		if is_male.get(stud['first_name'])==True: # если мужской пол
			male_num=male_num+1
	itog=f"{female_num} девочек и {male_num} мальчиков"
	if male_num+female_num==len(study['students']):
		print(itog)
	
    
print("--------------------------------")
# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}


for study in school: 
    male_num=0
    female_num=0
    for stud in study['students']:
        if is_male.get(stud['first_name'])==False:
            female_num=female_num+1
        if is_male.get(stud['first_name'])==True:
            male_num=male_num+1
        if female_num > male_num:
            itog=f"Больше всего мальчиков"
        if male_num < female_num:
            itog=f"Больше всего девочек"
    print(f"В классе {study['class']}: {itog} ")
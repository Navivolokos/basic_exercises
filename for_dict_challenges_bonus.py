"""
Пожалуйста, приступайте к этой задаче после того, как вы сделали и получили ревью ко всем остальным задачам
в этом репозитории. Она значительно сложнее.


Есть набор сообщений из чата в следующем формате:

```
messages = [
    {
        "id": "efadb781-9b04-4aad-9afe-e79faef8cffb",
        "sent_at": datetime.datetime(2022, 10, 11, 23, 11, 11, 721),
        "sent_by": 46,  # id пользователя-отправителя
        "reply_for": "7b22ae19-6c58-443e-b138-e22784878581",  # id сообщение, на которое это сообщение является ответом (может быть None)
        "seen_by": [26, 91, 71], # идентификаторы пользователей, которые видели это сообщение
        "text": "А когда ревью будет?",
    }
]
```

Так же есть функция `generate_chat_history`, которая вернёт список из большого количества таких сообщений.
Установите библиотеку lorem, чтобы она работала.

Нужно:
1. Вывести айди пользователя, который написал больше всех сообщений.
2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).
5. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).

Весь код стоит разбить на логические части с помощью функций.
"""
import random
import uuid
import datetime

import lorem


def generate_chat_history():
    messages_amount = random.randint(200, 1000)
    users_ids = list(
        {random.randint(1, 10000) for _ in range(random.randint(5, 20))}
    )
    sent_at = datetime.datetime.now() - datetime.timedelta(days=100)
    messages = []
    for _ in range(messages_amount):
        sent_at += datetime.timedelta(minutes=random.randint(0, 240))
        messages.append({
            "id": uuid.uuid4(),
            "sent_at": sent_at,
            "sent_by": random.choice(users_ids),
            "reply_for": random.choice(
                [
                    None,
                    (
                        random.choice([m["id"] for m in messages])
                        if messages else None
                    ),
                ],
            ),
            "seen_by": random.sample(users_ids,
                                     random.randint(1, len(users_ids))),
            "text": lorem.sentence(),
        })
    return messages



def max_senter():
    spisok=generate_chat_history()
    list_user_sent=[]
    for mess in spisok:
        for sent_by, id_user_sent in mess.items():
            if sent_by=="sent_by":
                list_user_sent.append(id_user_sent)
                itog=str(f'ID пользователя, который написал больше всех сообщений {max(set(list_user_sent), key=list_user_sent.count)}')
                return itog
print(max_senter())

def max_answer():
    spisok=generate_chat_history()
    list_user_sent=[]
    for mess in spisok:
        for sent_by, id_user_sent in mess.items():
            if sent_by=="sent_by" and id_user_sent != None:
                list_user_sent.append(id_user_sent)
                itog=str(f'ID пользователя, который получил больше всего ответов {max(set(list_user_sent), key=list_user_sent.count)}')
                return itog
print(max_answer())  

print("--------------------------------------\n\n\n")

def time_mess():
    spisok=generate_chat_history()
    time_sent=[]
    for mess in spisok:
	    for sent_at, time in mess.items():
		    if sent_at=="sent_at":
			    time_sent.append(time)
    time_12=0
    time_12_18=0
    time_18=0
    for times in time_sent:
		
        if times.hour >0< 12:
            time_12= time_12+1 
 
        if times.hour  >12<18:
            time_12_18= time_12_18+1
        if times.hour  >18<24:
            time_18= time_18+1   

    return print(f'Утром: {time_12} Днем: {time_12_18} Вечером: {time_18}')
time_mess()


            
"""id_mess()


spisok=generate_chat_history()
list_user_sent=[]

for mess in spisok:
	for sent_by, id_user_sent in mess.items():
		if sent_by=="sent_by":
			list_user_sent.append(id_user_sent)
	
unique_user_list=list(set(list_user_sent))
print('------------------------------------------')
print('Список уникальных id\n\n')
print(unique_user_list)

	
dic={}

for row in spisok:
	for id_user in unique_user_list:	
		fename =row.get("sent_by")
		name = row.get("seen_by")
		if id_user == fename: 
			dic[id_user]=name
print('------------------------------------------')
print('Список ответов к уникальным id\n\n')
print(dic)"""
	





#if __name__ == "__main__":
    #print(generate_chat_history())
     
    
    
    
    
    

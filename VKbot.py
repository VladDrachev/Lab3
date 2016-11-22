import datetime
import vk
import weather
import time

# Авторезация сессии с помощью access token
session = vk.Session('aae618b5b3fafa26c902ec82fb2b3af223385c9b4160c5aa43f4cd35f92ed0f35436a6c48f476a245e123')

# Объект api
api = vk.API(session)

while (True):
    try:
        # Список последнх сообщения
        messages = api.messages.get()
    except:
        continue
    # Перебор каждого сообщение
    for m in messages[1:]:
        # Если сообщение не прочитано
        if m['read_state'] == 0:

            # id сообщения
            uid = m['uid']

            # Имя пользователя
            user_name = api.users.get(user_ids=uid)[0]['first_name']
            try:
                # id чата
                chat_id = m['chat_id']
            except:
                chat_id = 0
            if chat_id > 0:
                uid = 0

            # Форматированный текст сообщения
            text = m['body']
            text = text.lower()
            text = text.replace(' ', '')

            # Строка с датой и временем
            date_time = datetime.datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')

            # Команды
            # Информация о боте
            if text == 'info':
                api.messages.send(uid=uid, chat_id=chat_id, message=date_time +
                                                                    '\n\n Information:'
                                                                    '\n>VKBot v.0.01, built on November 19 2016 '
                                                                    '\n>Developer: Vlad Drachev')

            # Спиоск команд
            if text == 'commands':
                list_city = 'Список поддерживаемых городов: Ростов-на-Дону, Москва, Санкт-Петербург, Киев, Ереван '
                api.messages.send(uid=uid, chat_id=chat_id, message=date_time + '\n\nCommands:\n1. info\n2. commands'
                                                                                '\n3. привет'
                                                                                '\n4. погода в [название города]\n' +
                                                                    list_city)
            # Приветствие
            if text == 'привет':
                api.messages.send(uid=uid, chat_id=chat_id, message=date_time + '\n\nЗдравствуй, ' + user_name +
                                                                        '!✋')
            # Погода
            if text[0:7:1] == "погодав":
                api.messages.send(uid=uid, chat_id=chat_id, message=str(date_time + '\n\n' +
                                                                        weather.weather_now(text)))
            # Отмечает сообщение как прочитанное
            api.messages.markAsRead(message_ids=m['mid'])
    # Время ожидания 3 секунды
    time.sleep(3)
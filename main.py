from instruction import instruction
import requests
from bs4 import BeautifulSoup
import aiohttp
import asyncio
import time
from threading import Thread

start_time = time.time()


def sinh_pog():
    session = requests.Session()
    """Синхронно вызываем get запрос 100 раз"""

    #Ссылка на сайт
    url='https://www.meteovesti.ru/pogoda_10/29947'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    }

    for i in range(100):
        #Отправляем запрос на сайт с командой получить
        response = session.get(url, headers=headers)

        # просим у сайта вернуть красиво отформатированный текст
        soup = BeautifulSoup(response.text, 'lxml')

        #Парсим класс в котором хранится погода
        data = soup.find('span', class_="_h3 align-top me-1 d-inline-block").text

        print(f'В Бийске{data} градусов')



def mnogopotok_pog():
    """Синхронно вызываем get запрос 100 раз"""

    #Ссылка на сайт
    url='https://www.meteovesti.ru/pogoda_10/29947'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    }

    for i in range(25):
        #Отправляем запрос на сайт с командой получить
        response = requests.get(url, headers=headers)

        # просим у сайта вернуть красиво отформатированный текст
        soup = BeautifulSoup(response.text, 'lxml')

        #Парсим класс в котором хранится погода
        data = soup.find('span', class_="_h3 align-top me-1 d-inline-block").text

        print(f'В Бийске{data} градусов')





async def zapros():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://www.meteovesti.ru/pogoda_10/29947') as response:
            return await response.text()


async def parcer(x):
        html = await zapros()
        soup = BeautifulSoup(html, 'lxml')
        data = soup.find('span', class_="_h3 align-top me-1 d-inline-block").text
        print(f"В Бийске {data} градусов!")



def main():
    instruction()
    metod = int(input(f"Введите значение: "))
    if metod == 1:
        sinh_pog()
        end_time = time.time() - start_time
        print(f'Вермя выполнения {end_time} секунд')

    if metod == 2:
        loop = asyncio.get_event_loop()
        tasks = [loop.create_task(parcer(x)) for x in range(100)]
        loop.run_until_complete(asyncio.wait(tasks))
        end_time = time.time() - start_time
        print(f'Вермя выполнения {end_time} секунд')

    if metod == 3:
        th1 = Thread(target=mnogopotok_pog)
        th2 = Thread(target=mnogopotok_pog)
        th3 = Thread(target=mnogopotok_pog)
        th4 = Thread(target=mnogopotok_pog)

        th1.start()
        th2.start()
        th3.start()
        th4.start()

        th1.join()
        th2.join()
        th3.join()
        th4.join()
        end_time = time.time() - start_time
        print(f'Вермя выполнения {end_time} секунд')






main()



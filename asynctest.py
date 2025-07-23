import asyncio
import time

# синхронный
# def func():
#     print('начинаем')
#     time.sleep(5) # 5 секунд "спим" # ждём в синхронном режиме исполнения функции сна. лишь затем вывод на печать
#     print('завершаем')
#
# func()

# асинхронный
# async def func2():
#     print('начинаем')
#     await asyncio.sleep(5)  # пока ... делаем другие задачи
#     print('завершаем')
#
# asyncio.run(func2())

async def say_hello():
    await asyncio.sleep(1)
    print('Привет')

async def say_goodbye():
    await asyncio.sleep(2)
    print('Пока')

async def main():
    await asyncio.gather(say_hello(), say_goodbye()) # вторая ассинхронная функция
                                                     # не ждёт завершения исполнения
                                                     # первой, а выполняется максимально одновременно (обе запускаются
                                                     # параллельно и сразу)

asyncio.run(main())
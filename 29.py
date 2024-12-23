# 1. Создать 3 функции(сложение, вычитание, умножение) с явной типизацией которые на выходе возвращают словарь.

def add(a: int, b: int) -> dict:
    return {'add': a + b}

print(add(5, 6))



def sub(a: int, b: int) -> dict:
    return {'sub': a - b}

print(sub(5, 6))



def mult(a: int, b: int) -> dict:
    return {'mult': a * b}

print(mult(5, 6))



# 2. Обрабатывать ошибочную запись и записывать ошибки в log файл.

import logging

logging.basicConfig(filename='first.log',
                    filemode='a',
                    format='%(asctime)s || %(name)s || %(levelname)s || %(message)s',
                    level=logging.INFO)


logging.info('yo')
logging.warning('yoo')
logging.error('yooo')
logging.critical('yoooo')
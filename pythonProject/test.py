import logging
import random

logging.basicConfig(format = '%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.DEBUG, filename='test.log', filemode='a+', encoding='utf-8')


def test():
    return random.randint(0, 1)


def request():
    res = test()
    if res:
        logging.debug('Успешно')
        print('Обработка успешного результата')
    else:
        logging.debug('Провал')
        print('Обработка негативного результата')


if __name__ == '__main__':
    request()
def benchmark(func):
    import time

    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end-start))
    return wrapper

#Одна функция
@benchmark
def fetch_webpage():
    import requests
    webpage = requests.get('https://google.com')

#Вторая функция
@benchmark
def fetch_webpage1():
    import requests
    webpage = requests.get('https://yahoo.com')

#Вызвал одну функцию
fetch_webpage()
#Вызвал вторую функцию
fetch_webpage1()
#Они декорируются print -ом из wrapper-а
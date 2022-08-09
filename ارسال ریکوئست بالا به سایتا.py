import random
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import schedule
items = []


def used_list(list=items, rand_num=None):
    if len(list) >= 6:
        list.clear()
        list.append(rand_num)
    elif rand_num in list:
        pass
    else:
        list.append(rand_num)
    return list


def rand_time():
    random.seed()
    time_1 = list(range(1, 50))
    time_2 = list(range(50, 100))
    time_3 = list(range(100, 150))
    time_4 = list(range(150, 200))
    time_5 = list(range(200, 250))
    time_list = [time_5, time_4, time_3, time_2, time_1]
    rand = random.choice(time_list)
    while rand in used_list():
        rand = random.choice(time_list)
    used_list(rand_num=rand)
    return rand


numbers = []


def random_number():
    number_range = list(range(200, 540, 10))
    if len(numbers) >= len(number_range):
        numbers.clear()
        rand = random.choice(number_range)
        numbers.append(rand)
    else:
        rand = random.choice(number_range)
        while rand in numbers:
            rand = random.choice(number_range)
        numbers.append(rand)
    return rand


drivers = ['webdriver.Chrome()', 'webdriver.Firefox()']
used_drivers = []


def random_driver():
    if len(used_drivers) >= len(drivers):
        used_drivers.clear()
        rand = random.choice(drivers)
        used_drivers.append(rand)
    else:
        rand = random.choice(drivers)
        while used_drivers.count(rand) >= 2:
            rand = random.choice(drivers)
        used_drivers.append(rand)
    return eval(rand)


def search():
    for i in range(len(drivers)):
        driver = random_driver()
        driver.implicitly_wait(100)
        driver.maximize_window()
        driver.get('https://www.google.com/')
        driver.implicitly_wait(100)
        btn = driver.find_element(By.NAME, 'q')
        driver.implicitly_wait(100)
        btn.send_keys('web-burger.ir', Keys.ENTER)
        time1 = random.choice(rand_time())
        print(time1)
        s1 = time.sleep(time1)
        driver.implicitly_wait(100)
        site = driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div[1]/div/a').click()
        time2 = random_number()
        print(time2)
        s2 = time.sleep(time2)
        driver.quit()

schedule.every(144).minutes.do(search)

while True:
    schedule.run_pending()
    time.sleep(1)
